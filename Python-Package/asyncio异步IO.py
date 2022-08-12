'''
import asyncio

# 获取事件循环
loop = asyncio.get_event_loop()

# 定义协程
async def myfunc(url):
    await get_url(url)

# 创建task列表
tasks = [loop.create_task(myfunc(url)) for url in urls]

# 执行爬虫事件列表
loop.run_until_complete(asyncio.wait(tasks))

要用在异步IO编程中，依赖的库必须支持异步IO特性
爬虫应用中，requests不支持异步
需要用aiohttp
'''
import asyncio
import aiohttp
import time
urls = [f'https://www.cnblogs.com/sitehome/p/{page}' for page in range(1,50+1)]


async def async_craw(url):
    print('craw url:',url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            result = await resp.text()
            print(f'craw url:{url},{len(result)}')

loop =  asyncio.get_event_loop()
tasks = [loop.create_task(async_craw(url))for url in urls]

if __name__ == "__main__":
    start = time.time()
    loop.run_until_complete(asyncio.wait(tasks))
    print(f'async_craw,cost:{time.time()-start}')
'''
craw url:https://www.cnblogs.com/sitehome/p/24,70568
craw url:https://www.cnblogs.com/sitehome/p/29,70322
async_craw,cost:0.8837540149688721
'''
