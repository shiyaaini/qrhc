import requests
url="http://127.0.0.1:5900/upload_group_file"
params={
    "group_id":928918816,
    "file":"D:\git\dmbf\dmbf\编程文件\go-cqhttp\测试.py",
    "name":"C.py",
    # "folder":"程序" #不传folder值，默认在上传到文件根目录
}
resp=requests.get(url=url,params=params)
print(resp.text)