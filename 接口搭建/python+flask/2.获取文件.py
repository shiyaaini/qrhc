import flask
from flask import Flask,request
app=Flask(__name__)
@app.route('/index',methods=['GET','POST'])
def index():
    return {"image":"http://localhost:5000/static/image/22.jpg"}
@app.route('/file',methods=['GET','POST'])
def file():
    return {"file":"http://localhost:5000/static/file/1.py"}
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5000)