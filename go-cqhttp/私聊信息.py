import requests
from flask import Flask, request

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
        print(QQ_id,Xingxi_text)
        # 给go-cqhttp的5700端口提交数据,类似于浏览器访问的形式
        requests.get("http://127.0.0.1:5900/send_private_msg?user_id={0}&message={1}".format(QQ_id, Xingxi_text))    #对方的QQ号，需要发送的信息
    return p  # 对go-cqhttp进行相应，不然会出现三次重试

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5909)  # 监听本机的5909端口（数据来源于go-cqhttp推送到5909端口的数据）