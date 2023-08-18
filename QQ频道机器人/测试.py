import botpy
from botpy.types.message import Message

class MyClient(botpy.Client):
    async def on_at_message_create(self, message: Message):
        print(message)
        await self.api.post_message(channel_id=message.channel_id, content="content")

intents = botpy.Intents(public_guild_messages=True)
client = MyClient(intents=intents)
client.run(appid=102064226, token="siCTn32jdxIqZ2JVUNX2ENbu24bkwbvp")