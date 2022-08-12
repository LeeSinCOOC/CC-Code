'''
多进程
1、引入模块
    from multiprocessing import Process
2、建立、启动、结束
    p = Process(target=f,args=('bob',)
    p.start()
    p.join()
3、数据通信
    from multiprocessing import Queue
    q = Queue()
    q.put([42,None,'hello'])
    item = q.get()
4、安全锁
    from multiprocessing import Lock
    lock = Lock()
    with lock():
    #do something
5、池化技术
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor() as executor:
        # 方法1
        results = executor.map(func,[1,2,3])
        # 方法2
        future = executor.submit(func,1)
        result = future.result()
'''
import math,time
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
PRIMES =  [1123413241351]*100
def is_prime(n):
    if n < 2 :
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3,sqrt_n+1,2):
        if n % i == 0:
            return False
    return True
def single_thread():
    for number in PRIMES:
        is_prime(number)

def multi_thread():
    with ThreadPoolExecutor() as pool:
        pool.map(is_prime,PRIMES)

def multi_process():
    with ProcessPoolExecutor() as pool:   # max_workers=1 时速度和单线程一致
        pool.map(is_prime,PRIMES)

if __name__ == "__main__":
    start = time.time()
    single_thread()
    print(f'single_thread,cost:{time.time()-start}')

    start = time.time()
    multi_thread()
    print(f'multi_thread,cost:{time.time() - start}')

    start = time.time()
    multi_process()
    print(f'multi_process,cost:{time.time() - start}')
'''
single_thread,cost:5.584094285964966
multi_thread,cost:5.761045217514038
multi_process,cost:3.040741443634033
'''