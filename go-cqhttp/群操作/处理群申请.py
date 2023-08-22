import requests
url='http://127.0.0.1:5900/set_group_add_request'
parmers={
    "group_id":928918816,
    "enable":'flase'

}
resp=requests.get(url=url,params=parmers)
print(resp.text)