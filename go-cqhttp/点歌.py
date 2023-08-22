import requests,json

import requests
from flask import Flask, request

def musices(ms):
    url = "https://music.haom.ren/"
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "content-length": "56",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "cookie": "__vtins__Jg5qguzyKFaykuwf=%7B%22sid%22%3A%20%22a03f6227-be7d-58da-a162-27a5f59299d3%22%2C%20%22vd%22%3A%201%2C%20%22stt%22%3A%200%2C%20%22dr%22%3A%200%2C%20%22expires%22%3A%201680504999721%2C%20%22ct%22%3A%201680503199721%7D; __51uvsct__Jg5qguzyKFaykuwf=1; __51vcke__Jg5qguzyKFaykuwf=d01af7b6-29ad-585e-a5ed-cb11b9da5943; __51vuft__Jg5qguzyKFaykuwf=1680503199725; __51huid__JgLUNAuSdBWFPrAs=53911428-bba5-525b-a9cc-561ada873c97",
        "origin": "https://music.haom.ren",
        "referer": "https://music.haom.ren/?name=%E5%8F%AF%E8%83%BD&type=netease",
        "sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Microsoft Edge\";v=\"110\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63",
        "x-requested-with": "XMLHttpRequest"
    }
    data = {
        'input': ms,
        'filter': 'name',
        'type': 'netease',
        'page': 1
    }
    resp = requests.post(url=url, headers=headers, data=data)
    # print(resp.json())
    musci = resp.json()['data']
    if resp.json() == '':  # 如何列表已经刷完，依然没有找到相对应的歌曲，就结束
        print('终止')
    for i in musci:
        if 'http' in str(i['url']):
            print('作者：' + i['author'])
            print('音乐：' + i['title'])
            print('链接：' + i['url'])
            requests.get(f'http://localhost:5900/send_private_msg?user_id=2106359814&message=[CQ:record,file={i["url"]}]')
            break


app = Flask(__name__)

@app.route('/', methods=["POST"])
def post_data():
    p='0'

    if request.get_json().get('message_type') == 'private':      # 如果是私聊信息状态码，只接收私聊的信息
        # 获取需要的消息
        print(request.get_json())
        QQ_name = request.get_json().get('sender').get('nickname')        # 发送者人的昵称叫啥
        QQ_id = request.get_json().get('sender').get('user_id')           # 发送者的QQ号
        Xingxi_text = request.get_json().get('raw_message')               # 发的什么东西

        # 给go-cqhttp的5700端口提交数据,类似于浏览器访问的形式
        musices(Xingxi_text)
    return p  # 对go-cqhttp进行相应，不然会出现三次重试

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5909)  # 监听本机的5909端口（数据来源于go-cqhttp推送到5909端口的数据）