import botpy,re,json
from botpy.types.message import Message
#存储用户信息
def save_user_msg(users):
    # users=json.loads(users)
    with open('config.json','r',encoding='utf-8') as f:
        p=json.load(f)
    if users['code']=="group":
        if p['guild'] == []:
            l={"guild": users['guild'], "guild_name": users['guild_name']}
            if 'channel_id' not in list(l.keys()):

                l['channel_id'] = {users['channel_id']:users['channel_name']}
            p['guild'].append(l)
            with open('config.json', 'w', encoding='utf-8') as f:
                json.dump(p, f, ensure_ascii=False)
            return {"code":200,"msg":"信息保存成功","data":p}
        for i in p['guild']:
            l = {"guild": users['guild'], "guild_name": users['guild_name']}
            #没有此群聊时添加
            if users['guild'] not in i['guild']:
                if 'channel_id' not in list(i.keys()):
                    l['channel_id'][users['channel_id']] = users['channel_name']
                p.append(l)
            #群聊相等添加子频道
            elif users['guild']==i['guild']:
                if users['channel_id'] not in list(i['channel_id'].keys()):
                    i['channel_id'][users["channel_id"]]= users['channel_name']

            with open('config.json','w',encoding='utf-8') as f:
                json.dump(p,f,ensure_ascii=False)
            return {"code":200,"msg":"信息保存成功","data":p}



class MyClient(botpy.Client):
    #接收@的信息
    async def on_at_message_create(self, message: Message):
        print(message)
        #@机器人的前24个字符是不要的
        pattern = r"<@!\d+>\s*(.*)"

        match = re.search(pattern, message.content)
        content=match.group(1)
        # await self.api.post_message(channel_id=message.channel_id, content=content)
        #获取主频道详情信息
        guild = await self.api.get_guild(guild_id=message.guild_id)
        guild_name=guild.get('name')
        #获取子频道信息
        channel=await self.api.get_channel(channel_id=message.channel_id)
        channel_name=channel.get('name')
        df=save_user_msg({"code":"group","guild":message.guild_id,"channel_id":message.channel_id,"guild_name":guild_name,"channel_name":channel_name})
        print(df)
        user_name=message.author.username
        print(f"{guild_name}>>{channel_name}>>{user_name}:{content}")


if __name__ == '__main__':

    intents = botpy.Intents(public_guild_messages=True)
    # intents = botpy.Intents(guild_messages=True)
    client = MyClient(intents=intents)
    client.run(appid=102064226, token='iE4dn9yMvhy1n5NR9g0RFHaNYHVrE0Uo')