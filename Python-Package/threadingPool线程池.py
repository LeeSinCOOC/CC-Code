'''
ThreadPoolExecutor的使用语法
from concurrent.futures import ThreadPoolExecutor,as_completed
用法1：map函数，注意map的结果和入参是顺序对应的
with ThreadPoolExecutor() as pool:
    results = pool.map(craw,urls)
    for result in results:
        print(result)

用法2：future模式，更强大，注意用as_completed顺序是不定的
with ThreadPoolExecutor() as pool:
    futures = [pool.submit(craw,url) for url in urls]
    for future in futures:
        print(future.result())
    for future in as_completed(futures):
        print(future.result())
'''

import concurrent.futures
from bs4 import BeautifulSoup
import requests
urls = [f'https://www.cnblogs.com/sitehome/p/{page}' for page in range(1,50+1)]

def craw(url):
    r = requests.get(url)
    return r.text
def parse(html):
    soup = BeautifulSoup(html,'html.parser')
    links = soup.find_all('a',class_ = 'post-item-title')
    return [(link['href'],link.get_text()) for link in links]

with concurrent.futures.ThreadPoolExecutor() as pool:
    htmls = pool.map(craw,urls)
    htmls = list(zip(urls,htmls))
    for url,html in htmls:
        print(url,len(html))
print('craw over')
with concurrent.futures.ThreadPoolExecutor() as pool:
    futures = {}
    for url, html in htmls:
        future = pool.submit(parse,html)
        futures[future] = url
    # for future , url in futures.items():
    #     print(url,future.result())
    for future in concurrent.futures.as_completed(futures):
        url = futures[future]
        print(url,future.result())
print('parse over')