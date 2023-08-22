import json

import requests
from group_send_message import *
from flask import Flask,request
app=Flask(__name__)

@app.route('/',methods=["POST"])
def QQBot():
    p='0'

    if request.get_json().get('message_type') =='private' and request.get_json()['user_id']==2106359814:    #判断满足群聊+群号
        print(request.get_json())

        # QQ_name = request.get_json().get('sender').get('nickname')        # 发送者人的昵称叫啥
        QQ_id = request.get_json().get('sender').get('user_id')           # 发送者的QQ号
        Xingxi_text = request.get_json().get('raw_message')               # 发的什么东西
        # message_id=request.get_json().get('message_id')
        print(Xingxi_text)
        send_message(Xingxi_text,QQ_id)

    return p
if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1',port=5909)