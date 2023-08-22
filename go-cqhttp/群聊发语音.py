import requests

url="http://127.0.0.1:5900/send_group_msg"
params={
    "group_id":"群号",
    "message":"[CQ:record,file=https://m801.music.126.net/20230403140032/8fb2605d55e17140cefd0ca471a9f373/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/17718433824/acca/41eb/8112/efa4dce840121844afcb957bcb2d4fd1.mp3]"
}
resp=requests.get(url=url,params=params)
print(resp.text)