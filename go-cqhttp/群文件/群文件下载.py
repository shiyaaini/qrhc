import requests,json

class Downloadfile:
    def __init__(self,group_id):
        self.group_id = group_id
    #获取文件ID
    def get_fileid(self,file_name):
        url = "http://127.0.0.1:5900/get_group_root_files"
        params = {
            "group_id": self.group_id,

        }
        resp = requests.get(url=url, params=params)
        # print(resp.text)
        resp=json.loads(resp.text)
        # 遍历所有文件信息，判断文件名获取需要删除的文件ID
        for i in resp["data"]["files"]:
            if i["file_name"]==file_name:
                return {"file_id":i["file_id"],"busid":i["busid"],"file_name":i["file_name"]}
    # 获取下载链接
    def download_url(self,ps):
        url=f"http://localhost:5900/get_group_file_url"
        params={
            "group_id":self.group_id,
            "file_id":ps['file_id'],
            "busid":ps['busid'],
        }
        resp=requests.get(url=url,params=params)
        print(resp.text)
        p=json.loads(resp.text)["data"]["url"]
        return p
    #下载文件
    def download_file(self,url,file):
        resp=requests.get(url)
        with open(file['file_name'],'wb') as f:
            f.write(resp.content)
down=Downloadfile(928918816)
# 获取id
file=down.get_fileid('hello.py')
# print(file_id)
# 获取下载url
url=down.download_url(file)
down.download_file(url,file)
