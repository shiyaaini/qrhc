import requests
url='http://127.0.0.1:5900/set_group_portrait'
parm={
    'group_id':928918816,
    'file':'1.jpg'
}
resp=requests.get(url=url,params=parm)
print(resp.text)