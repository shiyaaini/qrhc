import json

import requests
from flask import Flask,request
app=Flask(__name__)
@app.route('/',methods=["POST"])
def QQBot():
    p='0'

    if request.get_json().get('message_type') =='group' and request.get_json()['group_id']==928918816:    #判断满足群聊+群号
        print(request.get_json())
        group_id = request.get_json()['group_id']  # 获取群聊号
        message = request.get_json().get('message') #获取群信息
        resp=requests.get("http://127.0.0.1:5900/send_group_msg?group_id={0}&message={1}".format(group_id, message))

    return p
if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1',port=5909)