
#[CQ:video,file=http://baidu.com/1.mp4]
import requests

url="http://127.0.0.1:5900/send_group_msg"
params={
    "group_id":"群号",
    "message":"[CQ:video,file=1.mp4]"
}
resp=requests.get(url=url,params=params)
print(resp.text)