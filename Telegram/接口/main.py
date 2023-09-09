import flask ,json,time
from flask import Flask,request
import flask_cors
app=Flask(__name__)
flask_cors.CORS(app, supports_credentials=True)
@app.route('/',methods=['GET','POST'])
def index():
    ps=request.get_json()
    text=ps['message']['text']
    if text=='你喜欢我吗':
        return '喜欢'
    else:
        return  '不喜欢'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=3000)