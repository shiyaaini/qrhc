
import requests
url="http://127.0.0.1:5900/send_private_msg"
params={
    "user_id":"QQ号",
    "message":"[CQ:video,file=1.mp4]"
}
resp=requests.get(url=url,params=params)
print(resp.text)