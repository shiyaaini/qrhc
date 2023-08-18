import flask
from flask import Flask,request
app=Flask(__name__)
@app.route('/index',methods=['GET','POST'])
def index():
    p=flask.request.values
    name=p.get('name')
    age=p.get('age')
    print(name,age)
    return {'name':name,'age':age,"status":200}

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5000)