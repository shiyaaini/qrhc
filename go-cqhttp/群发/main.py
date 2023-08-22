import requests,json

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
def sendMessage(user_id):
    for i in user_id:
        url="http://127.0.0.1:5900/send_private_msg"
        data={
            "user_id":i,
            "message":"hello"
        }
        resp=requests.get(url=url,params=data)
        print(resp.text)
user_id=get_friend()
sendMessage(user_id)

