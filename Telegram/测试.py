import flask,json,time
from flask import request,Flask
import flask_cors
app=Flask(__name__)
flask_cors.CORS(app, supports_credentials=True)
@app.route('/')
def hello_world():
    print(flask.request.values)
    p=flask.request.values.get('proplem')
    if p=='你喜欢我吗':
        return '喜欢'
    else:
        return  '不喜欢'
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=8443)