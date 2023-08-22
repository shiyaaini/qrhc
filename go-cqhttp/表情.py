import requests
resp=requests.get(url='http://127.0.0.1:5900/send_private_msg?user_id={0}&message={1}'.format(2106359814,'[CQ:face,id=0]'))
print(resp.text)
