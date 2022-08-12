'''
多线程数据通信的queue.Queue
1、创建队列
    import queue
    q = queue.Queue()
2、添加元素
    q.put(item)
4、获取元素
    item = q.get()
5、查询状态
    5.1 查看元素的多少
        q.qsize()
    5.2 判断是否为空
        q.empty()
    5.3 判断是否已满
        q.full()
'''
import random
import threading
import requests,time
from bs4 import BeautifulSoup
import queue

urls = [f'https://www.cnblogs.com/#p{page}' for page in range(1,50+1)]

def craw(url):
    r = requests.get(url)
    return r.text
def parse(html):
    soup = BeautifulSoup(html,'html.parser')
    links = soup.find_all('a',class_ = 'post-item-title')
    return [(link['href'],link.get_text()) for link in links]

def do_craw(url_queue:queue.Queue,html_queque:queue.Queue):
    while True:
        url = url_queue.get()
        html = craw(url)
        html_queque.put(html)
        print(threading.currentThread().name,f'craw {url}',f'url_queue.size={url_queue.qsize()}')
        time.sleep(random.randint(1,2))
def do_parse(html_queue:queue.Queue,fout):
    while True:
        html = html_queue.get()
        results = parse(html)
        for result in results:
            fout.write(str(result)+'\n')
        print(threading.currentThread().name, f'result size {len(results)}', f'html_queue.size={html_queue.qsize()}')
        time.sleep(random.randint(1, 2))

def main():
    url_queue = queue.Queue()
    html_queue = queue.Queue()
    for url in urls:
        url_queue.put(url)
    for idx in range(3):
        t = threading.Thread(target=do_craw, args=(url_queue, html_queue), name=f'craw{idx}')
        t.start()
    fout = open('tmp.txt', 'w')
    for idx in range(2):
        t = threading.Thread(target=do_parse, args=(html_queue, fout), name=f'parse{idx}')
        t.start()
if __name__ == "__main__":
    main()

