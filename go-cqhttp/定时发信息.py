import requests
url="http://192.168.192.149:5900/send_private_msg"
params={
    "user_id": "2106359814",
    "message": "love you"
}
resp=requests.get(url=url,params=params)
print(resp.text)