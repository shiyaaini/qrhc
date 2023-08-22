import requests


url = f"http://127.0.0.1:5900/send_private_msg"
params = {
    "user_id":"2106359814",
    "message":'[CQ:tts,text=你在干什么？]'
}
response = requests.post(url, json=params)
print(response.text)