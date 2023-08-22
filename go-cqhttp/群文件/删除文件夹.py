import requests,json
class DLEfolder:
    def __init__(self,group_id):
        self.group_id = group_id
    def get_folderid(self,folder_name):
        url = "http://127.0.0.1:5900/get_group_root_files"
        params = {
            "group_id": self.group_id,

        }
        resp = requests.get(url=url, params=params)
        # print(resp.text)
        resp=json.loads(resp.text)

        # 遍历所有文件信息，判断文件名获取需要删除的文件ID
        for i in resp["data"]["folders"]:
            if i["folder_name"]==folder_name:
                return {"folder_id":i["folder_id"]}
    def deletefolder(self,folder_id):
        url = "http://127.0.0.1:5900/delete_group_folder"
        params = {
            "group_id": self.group_id,
            "folder_id": folder_id, #文件名ID
        }
        resp = requests.get(url=url, params=params)
        print(resp.text)

if __name__ == '__main__':
    group_id =928918816 #群号
    fs = DLEfolder(group_id)
    file_id = fs.get_folderid('程序') #需要删除的文件名
    fs.deletefolder(file_id["folder_id"])