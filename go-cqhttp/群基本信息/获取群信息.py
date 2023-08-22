import requests
from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=["POST"])
def post_data():
    psds='0'
    resp = requests.get("http://127.0.0.1:5900/get_group_info?group_id=928918816")
    print(resp.text)
    return psds
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5909)  #监听本机的5909端口（数据来源于go-cqhttp推送到5701端口的数据）
