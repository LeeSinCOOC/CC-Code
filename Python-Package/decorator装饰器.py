# 传统装饰器
def deco(func):
    def wrapper(*args, **kw):
        print('准备运行任务')
        func(*args, **kw)
        print('成功运行任务')
    return wrapper
@deco
def myfunc():
    print('开始运行任务')

myfunc()
'''
准备运行任务
开始运行任务
成功运行任务
'''

# 使用decorator
from decorator import decorator

@decorator
def deco(func,*args,**kwargs):
    print('准备运行任务')
    func(*args,**kwargs)
    print('成功运行任务')

@deco
def myfunc():
    print('开始运行任务')
myfunc()
'''
准备运行任务
开始运行任务
成功运行任务
'''

# 装饰器传参
import time
@decorator
def warn_slow(func, timelimit=3, *args, **kw):
    t0 = time.time()
    result = func(*args, **kw)
    dt = time.time() - t0
    if dt > timelimit:
        print(f'{func.__name__} took {dt} seconds >>> {timelimit}')
    else:
        print(f'{func.__name__} took {dt} seconds <<< {timelimit}')
    return result

@warn_slow
def preprocess_input_files():
    print('preprocess_input_files')
    time.sleep(2)

@warn_slow(timelimit=2)
def run_calculation():
    print('run_calculation')
    time.sleep(2)
preprocess_input_files()
run_calculation()

'''
preprocess_input_files
preprocess_input_files took 2.0043842792510986 seconds <<< 3
run_calculation
run_calculation took 2.000210762023926 seconds >>> 2
'''