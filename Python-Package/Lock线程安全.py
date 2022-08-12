'''
lock 用于解决线程安全问题

用法1：try-finally模式
import threading

lock = threading。Lock()
lock.acquire()
try:
    #do something
finally:
lock.release()

用法2：with模式
import threading

lock = threading.Lock()
with lock:
 #do something
'''
import threading
import time

lock = threading.Lock()
class Account:
    def __init__(self,balance):
        self.balance = balance
def draw(account,amount):
    with lock:
        if account.balance >= amount:
            print(threading.current_thread().name,'取钱成功')
            time.sleep(2)
            account.balance -= amount
            print(threading.current_thread().name,'余额',account.balance)
        else:
            print(threading.current_thread().name,'取钱失败，余额不足')

if __name__ == "__main__":
    account = Account(1000)
    ta = threading.Thread(name='ta',target=draw,args=(account,800))
    tb = threading.Thread(name='tb',target=draw,args=(account,800))

    ta.start()
    tb.start()
'''
没有lock：                  有lock:
ta tb取钱成功                ta 取钱成功ta 余额 200
取钱成功                     tb 取钱失败，余额不足
tbta 余额  余额-600
 200
'''