
import requests
#同一个音频文件这次发了，下次就不能再发了，发了也是不成功的，机器人要发另外一个音频或者信息才能继续发送
url = "http://localhost:5900/send_private_msg?user_id=2106359814&message=[CQ:record,file=http://m801.music.126.net/20230403205958/c993ff5654bb619890a3fc9c1faff208/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/16672040292/1f33/8dcd/e4ab/fc3c42b47e36e7b5510921aa32d67a78.mp3]"

resp = requests.get(url)
# 打印返回结果
print(resp.json())
