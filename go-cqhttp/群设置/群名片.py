import requests
url='http://127.0.0.1:5900/set_group_card'
parm={
    'group_id':928918816,
    'user_id':3379727288,
    'card':'你好'
}
resp=requests.get(url=url,params=parm)
print(resp.text)