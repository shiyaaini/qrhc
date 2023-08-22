import requests,json
class DLEfile:
    def __init__(self,group_id):
        self.group_id = group_id
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
                return {"file_id":i["file_id"],"busid":i["busid"]}
    def deletefile(self,file_id,busid):
        url = "http://127.0.0.1:5900/delete_group_file"
        params = {
            "group_id": self.group_id,
            "file_id": file_id,
            "busid":busid

        }
        resp = requests.get(url=url, params=params)
        print(resp.text)



if __name__ == '__main__':
    group_id =928918816 #群号
    fs = DLEfile(group_id)
    file_id = fs.get_fileid('C.py') #需要删除的文件名
    fs.deletefile(file_id["file_id"],file_id["busid"])