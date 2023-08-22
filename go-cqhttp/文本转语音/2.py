import requests,json
from flask import Flask,request
def ms(textss):
    url='https://www.text-to-speech.cn/getSpeek.php'
    headers={
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "content-length": "359",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "cookie": "language=ä¸­æ–‡ï¼ˆæ™®é€šè¯ï¼Œç®€ä½“ï¼‰; voice=zh-CN-XiaoxiaoNeural; kbitrate=riff-48khz-16bit-mono-pcm; role=0; style=sad; speed=0; pitch=0; X_CACHE_KEY=787ede598d820e0a7e459337df4570e0".encode("utf-8").decode("latin1"),
        "origin": "https://www.text-to-speech.cn",
        "pragma": "no-cache",
        "referer": "https://www.text-to-speech.cn/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"}
    data={
        'language': '中文（普通话，简体）',
        'voice': 'zh-CN-XiaoxiaoNeural',
        'text': textss,
        'role': 0,
        'style': 'gentle',  #感情类型
        'rate': 0,
        'pitch': 0,
        'kbitrate': 'audio-48khz-192kbitrate-mono-mp3',
        'silence': '',
        'styledegree': 1.5,
        'user_id': ''
    }
    resp=requests.post(url=url,headers=headers,data=data)
    print(resp.text)
    p=json.loads(resp.text)['download']
    requests.get(f'http://localhost:5900/send_private_msg?user_id=2106359814&message=[CQ:record,file={p}]')
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
        ms(Xingxi_text)
    return p  # 对go-cqhttp进行相应，不然会出现三次重试

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5909)  # 监听本机的5909端口（数据来源于go-cqhttp推送到5909端口的数据）