'''
Python 创建多线程的方法
1、准备函数
    def my_fun(a,b):
        do_craw(a,b)
2、创建一个线程
    import threading
    t = threading.Thread(target=my_fun,args=(100,200))
3、启动线程
    t.start()
4、等待结束
    t.join()
'''
import requests,time
import threading

urls = [f'https://www.cnblogs.com/#{page}' for page in range(1,50+1)]
def craw(url):
    r = requests.get(url)
    print(url,len(r.text))
def single_tread():
    print('single_tread start')
    for url in urls:
        craw(url)
    print('single_tread end')
def multi_thread():
    print('multi_thread start')
    threads = []
    for url in urls:
        threads.append(threading.Thread(target=craw,args=(url,)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print('multi_thread end')
if __name__ == "__main__":
    start = time.time()
    single_tread()
    print('single_tread cost:',time.time()-start)

    start = time.time()
    multi_thread()
    print('multi_thread cost:', time.time() - start)


'''
单线程：                                     多线程：
https://www.cnblogs.com/#49 70524          https://www.cnblogs.com/#44 70524
https://www.cnblogs.com/#50 70524          https://www.cnblogs.com/#43 70524
single_tread end                           multi_thread end
single_tread cost: 13.145885944366455      multi_thread cost: 0.5871031284332275
'''