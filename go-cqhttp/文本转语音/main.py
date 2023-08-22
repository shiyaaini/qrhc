import asyncio
import aiohttp
url=[
    'https://i1.huishahe.com/uploads/tu/201911/9999/1667531d61.jpg',
    'https://i1.huishahe.com/uploads/tu/201911/9999/0c73cbbc49.jpg',
    'https://i1.huishahe.com/uploads/tu/201911/9999/37a6149ecd.jpg'
]
async def downloads(j):
   ht=j.rsplit('/',1)[1]
   print(ht)
   async with aiohttp.ClientSession() as session:
       async with session.get(j) as resp:
            with open(ht,mode='wb') as f:
                f.write(await resp.content.read())
async def main():
    task=[]
    for i in url:
        tf=asyncio.create_task(downloads(i))
        task.append(tf)
    await asyncio.wait(task)
if __name__ == '__main__':
    asyncio.run(main())
