import requests
url='http://127.0.0.1:5900/set_group_ban'
parmers={
    "group_id":928918816,
    "user_id":3379727288,
    "duration":60*60
}
resp=requests.get(url=url,params=parmers)
print(resp.text)