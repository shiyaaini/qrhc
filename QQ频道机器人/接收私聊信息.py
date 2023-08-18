import botpy
from botpy.message import DirectMessage
class MyClient(botpy.Client):
    #接收私聊信息
    async def on_direct_message_create(self, message: DirectMessage):
        print(message)
        content=message.content
        username=message.author.username
        print(f"[私聊]{username}:{content}")
        # await self.api.post_dms(guild_id=message.guild_id, content=content)

intents = botpy.Intents(direct_message=True)
client = MyClient(intents=intents)
client.run(appid=102064226, token='siCTn32jdxIqZ2JVUNX2ENbu24bkwbvp')