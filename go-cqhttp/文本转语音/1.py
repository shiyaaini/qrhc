import requests
import json,time
import ddddocr,requests
from flask import Flask,request
def musics(us,texts):
    url='https://ttsmaker.com/api/create-tts-order'
    headers={
        "Host": "ttsmaker.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://ttsmaker.com",
        "Cookie": "uuid=a638d202-44ce-49d2-8a7e-9993eedf19f8; Hm_lvt_620f68368c2bc5df0b46b149a685a51c=1680575099; Hm_lpvt_620f68368c2bc5df0b46b149a685a51c=1680575099; __gads=ID=f14904a8405f6c2a-22292377fade00e4:T=1680575634:RT=1680575634:S=ALNI_MaPQQC8NBxrop6ALrkV0k6Y20Hkiw; __gpi=UID=0000057a8a4a8fef:T=1680575634:RT=1680575634:S=ALNI_MZ161uxp6ZFJNh__EJ5pXLLZD0riw; _clck=oma7ot|1|fah|0",

    }
    data={
        "user_uuid_text":"a638d202-44ce-49d2-8a7e-9993eedf19f8",
        "user_input_text":texts,
        "user_select_language_id":"zh-cn",
        "user_select_announcer_id":"204",
        "user_select_tts_setting_audio_format":"mp3",
        "user_select_tts_setting_speed":"1.0",
        "user_select_tts_setting_volume":"0",
        "user_input_captcha_text":us,
        "user_input_paragraph_pause_time":"0"}
    resp=requests.post(url=url,headers=headers,json=data)
    print(resp.text)
    p=json.loads(resp.text).get('auto_stand_url')
    print(p)
    requests.get(f'http://localhost:5900/send_private_msg?user_id=2106359814&message=[CQ:record,file={p}]')
def voies():
    url = 'https://ttsmaker.com/get_captcha?uuid=a638d202-44ce-49d2-8a7e-9993eedf19f8&rand=364550&reload=7&reload=7&reload=7&reload=7'
    headers = {
        "Host": "ttsmaker.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
        "Accept": "image/avif,image/webp,*/*",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate, br",
        "Alt-Used": "ttsmaker.com",
        "Connection": "keep-alive",
        "Referer": "https://ttsmaker.com/zh-cn",
        "Cookie": "uuid=a638d202-44ce-49d2-8a7e-9993eedf19f8; Hm_lvt_620f68368c2bc5df0b46b149a685a51c=1680575099; Hm_lpvt_620f68368c2bc5df0b46b149a685a51c=1680575099; __gads=ID=f14904a8405f6c2a-22292377fade00e4:T=1680575634:RT=1680575634:S=ALNI_MaPQQC8NBxrop6ALrkV0k6Y20Hkiw; __gpi=UID=0000057a8a4a8fef:T=1680575634:RT=1680575634:S=ALNI_MZ161uxp6ZFJNh__EJ5pXLLZD0riw; _clck=oma7ot|1|fah|0",
        "Sec-Fetch-Dest": "image",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Site": "same-origin",
    }
    resp = requests.get(url=url)
    # print(resp.content)
    with open('hello.jpg', 'wb') as f:
        f.write(resp.content)
    time.sleep(2)
    with open('hello.jpg', 'rb') as f:
        img = f.read()
    ocr = ddddocr.DdddOcr()
    us = ocr.classification(img)
    print(us)
    return us
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
        v=voies()
        musics(v,Xingxi_text)
    return p  # 对go-cqhttp进行相应，不然会出现三次重试

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5909)  # 监听本机的5909端口（数据来源于go-cqhttp推送到5909端口的数据）
