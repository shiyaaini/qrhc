import requests,json,random
def send_message(message,user_id):
    with open('config.json','r',encoding='utf-8') as fs:
        data=json.load(fs)
    if message=="群发":
        data['module']="群发"
        with open('config.json','w',encoding='utf-8') as f:
            json.dump(data,f,ensure_ascii=False)
    elif message=='随机图片':
        url = "http://127.0.0.1:5900/send_private_msg"
        params = {
            "user_id": user_id,
            "message": f"[CQ:image,file={random.randint(1, 13)}.jpg]"
        }
        resp = requests.get(url=url, params=params)
        print(resp.text)
    else:
        if data['module']=="群发":
            user_id=get_friend()
            sendMessage(user_id,message)
            # 清值
            data['module']=''
            with open('config.json','w',encoding='utf-8') as f:
                json.dump(data,f,ensure_ascii=False)


# 获取所有好友列表
def get_friend():
    url="http://127.0.0.1:5900/get_friend_list"
    resp=requests.get(url)
    print(resp.text)
    p=[]
    for i in json.loads(resp.text)['data']:
        nickname=i['nickname']
        remark=i['remark']
        user_id=i['user_id']
        if user_id!=66600000:   #不给babyQ发信息
            p.append(user_id)
    return p
# 发送信息函数
def sendMessage(user_id,message):
    for i in user_id:
        url="http://127.0.0.1:5900/send_private_msg"
        data={
            "user_id":i,
            "message":message
        }
        resp=requests.get(url=url,params=data)
        print(resp.text)




# with open('config.json','r',encoding='utf-8') as fs:
#     data=json.load(fs)
# data['name']='诗雅'
# with open('config.json','w',encoding='utf-8') as f:
#     json.dump(data,f)