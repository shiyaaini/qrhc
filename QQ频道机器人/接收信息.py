import botpy,re
from botpy.types.message import Message

class MyClient(botpy.Client):
    #接收@的信息
    async def on_at_message_create(self, message: Message):
        print(message)
        #@机器人的前24个字符是不要的
        pattern = r"<@!\d+>\s*(.*)"

        match = re.search(pattern, message.content)
        content=match.group(1)
        await self.api.post_message(channel_id=message.channel_id, content=content)
        #获取主频道详情信息
        guild = await self.api.get_guild(guild_id=message.guild_id)
        guild_name=guild.get('name')
        #获取子频道信息
        channel=await self.api.get_channel(channel_id=message.channel_id)
        channel_name=channel.get('name')
        user_name=message.author.username
        print(f"{guild_name}>>{channel_name}>>{user_name}:{content}")
    #接收信息
    async def on_message_create(self, message: Message):
        print(message)
        content=str(message.content)
        print(content)
        await self.api.post_message(channel_id=message.channel_id, content=content)
        #获取主频道详情信息
        guild = await self.api.get_guild(guild_id=message.guild_id)
        guild_name=guild.get('name')
        #获取子频道信息
        channel=await self.api.get_channel(channel_id=message.channel_id)
        channel_name=channel.get('name')
        user_name=message.author.username
        print(f"{guild_name}>>{channel_name}>>{user_name}:{content}")


# intents = botpy.Intents(public_guild_messages=True)
intents = botpy.Intents(guild_messages=True)
client = MyClient(intents=intents)
client.run(appid=102064226, token='siCTn32jdxIqZ2JVUNX2ENbu24bkwbvp')