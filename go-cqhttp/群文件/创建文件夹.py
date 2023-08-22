import requests
url="http://127.0.0.1:5900/create_group_file_folder"
params={
    "group_id":928918816,
    "name":"hello",    #群文件名
    "parent_id":"/"
}
resp=requests.get(url=url,params=params)
print(resp.text)