import requests
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def post_data():
    p='0'
    print(request.get_json())
    if request.get_json().get('notice_type') == 'group_upload':      # 如果是私聊信息状态码，只接收私聊的信息
        url=request.get_json().get('file')['url']
        file_name=request.get_json().get('file')['name']
        resp=requests.get(url)
        with open(file_name ,'wb') as f:
            f.write(resp.content)
    return p  # 对go-cqhttp进行相应，不然会出现三次重试

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5909)  # 监听本机的5909端口（数据来源于go-cqhttp推送到5909端口的数据）