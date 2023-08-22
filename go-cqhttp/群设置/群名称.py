import requests
url='http://127.0.0.1:5900/set_group_name'
parm={
    'group_id':928918816,
    'group_name':'浅若红尘'
}
resp=requests.get(url=url,params=parm)
print(resp.text)