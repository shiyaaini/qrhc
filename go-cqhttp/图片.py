import requests
from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=["POST"])
def post_data():
    psds='0'

    if request.get_json().get('message_type') == 'private':            # 如果是私聊信息状态码
        print(request.get_json())
        # 获取需要的消息
        QQ_name = request.get_json().get('sender').get('nickname')        # 发送者人的昵称叫啥
        QQ_id = request.get_json().get('sender').get('user_id')           # 发送者的QQ号
        Xingxi_text = request.get_json().get('raw_message')               # 发的什么东西
        if '1' in Xingxi_text:           #
            requests.get(url='http://127.0.0.1:5900/send_private_msg?user_id={0}&message={1}'.format(QQ_id, '[CQ:image,file=2.jpg]'))
    return psds
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5909)  #监听本机的5909端口（数据来源于go-cqhttp推送到5701端口的数据）
