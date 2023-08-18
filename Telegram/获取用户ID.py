import requests,json


def get_chat_id(api_token):
    api_url = f'https://api.telegram.org/bot{api_token}/getUpdates'

    response = requests.get(api_url)
    p=json.loads(response.text)
    print(response.text)
    if response.status_code == 200:
        if p["result"]!=[]:

            dlp=[]
            dlg=[]
            group=[]
            for i in p["result"]:
                if 'message' in i:
                    #判断是否为私聊
                    if i["message"]["chat"]["type"]=="private":
                        id=i["message"]['chat']['id']
                        first_name=i['message']['chat']['first_name']
                        last_name=i['message']['chat']['last_name']
                        pr={"id":id,"name":f'{first_name}{last_name}'}
                        if dlp==[]:
                            dlp.append(pr)
                        else:
                            for j in dlp:
                                if j['id']==id:
                                    continue
                                dlp.append(pr)
                    #判断是否为群组
                    elif i['message']['chat']['type']=="supergroup":
                        id=i["message"]['chat']['id']
                        title=i['message']['chat']['title']
                        grs={"id":id,"title":title}
                        if dlg==[]:
                            dlg.append(grs)
                        else:
                            for k in dlg:
                                if k['id']==id:
                                    continue
                                dlg.append(grs)
                    elif i['message']['chat']['type'] == "group":
                        id = i["message"]['chat']['id']
                        title = i['message']['chat']['title']
                        grs = {"id": id, "title": title}
                        if dlg == []:
                            dlg.append(grs)
                        else:
                            for k in dlg:
                                if k['id'] == id:
                                    continue
                                dlg.append(grs)


                elif 'my_chat_member' in i:
                    continue
            psd = {"private": dlp, "supergroup": dlg}
            return psd


        else:
            return {"msg":'暂无群聊或信息'}

if __name__ == "__main__":
    # 请将以下变量替换为您的Telegram Bot API令牌
    bot_api_token = '6469891265:AAFKC2SjxPATJJAR1lswA9dFy34jgsNMrBI'

    chat_id = get_chat_id(bot_api_token)
    print(chat_id)
