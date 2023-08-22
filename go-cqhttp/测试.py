import asyncio
import time

async def downloads(j):
    print('开始运行')
    await asyncio.sleep(3)
    print('结束运行')
async def main():
    t=[]
    task=[
        'baidu.com',
        '163.com',
        '4399.com'
    ]
    for i in task:
        p=asyncio.create_task(downloads(i))
        t.append(p)
    await asyncio.wait(t)
if __name__ == '__main__':
    asyncio.run(main())