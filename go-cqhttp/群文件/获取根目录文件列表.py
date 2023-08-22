import requests
url="http://127.0.0.1:5900/get_group_root_files"
params={
    "group_id":928918816,

}
resp=requests.get(url=url,params=params)
print(resp.text)