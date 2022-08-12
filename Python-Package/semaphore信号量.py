'''
方式1：
sem = asyncio.Semaphore(10)
#...later
async with sem:
    # work with shared resource

方式2：
sem = asyncio.Semaphore(10)
#...later
await sem.acquire()
try:
    # work with shared resource
finally:
    sem.release()
'''

import asyncio
import aiohttp
import time
urls = [f'https://www.cnblogs.com/sitehome/p/{page}' for page in range(1,50+1)]

semaphore = asyncio.Semaphore(10)

async def async_craw(url):
    async with semaphore:
        print('craw url:',url)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                result = await resp.text()
                await asyncio.sleep(5)
                print(f'craw url:{url},{len(result)}')

loop =  asyncio.get_event_loop()
tasks = [loop.create_task(async_craw(url))for url in urls]

if __name__ == "__main__":
    start = time.time()
    loop.run_until_complete(asyncio.wait(tasks))
    print(f'async_craw,cost:{time.time()-start}')
'''
不加信号量：                                                  加信号量：
craw url:https://www.cnblogs.com/sitehome/p/40,70761        craw url:https://www.cnblogs.com/sitehome/p/49,70304
craw url:https://www.cnblogs.com/sitehome/p/46,70053        craw url:https://www.cnblogs.com/sitehome/p/50,70358
async_craw,cost:6.430471420288086                           async_craw,cost:26.565725088119507

'''