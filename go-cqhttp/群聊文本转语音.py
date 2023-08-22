import requests
resp=requests.get(url='http://127.0.0.1:5900/send_group_msg?group_id=928918816&message=[CQ:tts,text="how are you"]')
print(resp.text)
