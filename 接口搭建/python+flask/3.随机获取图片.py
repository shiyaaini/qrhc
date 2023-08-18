import flask
from flask import Flask,request
import os,random
app = Flask(__name__)
@app.route('/index',methods=['GET',"POST"])
def index():
    print(flask.request.values.get("city"))
    p=os.listdir(r'./static/image')
    print(p)
    image=p[random.randint(0,9)]
    return {"image":"http://127.0.0.1:5000/static/image/"+image}
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5000)