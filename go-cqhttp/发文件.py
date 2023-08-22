import requests
url="http://127.0.0.1:5900/upload_private_file"
parmser={
    "user_id":2106359814,
    "file":"D:\git\dmbf\dmbf\编程文件\go-cqhttp\测试.py",
    "name":"GH.py"
}
resp=requests.get(url=url,params=parmser)
print(resp.text)

