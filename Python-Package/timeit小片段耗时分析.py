from timeit import timeit

def func():
    s = 0
    for i in range(100000):
        s += i
    print(s)

# timeit(函数名_字符串，运行环境_字符串，number=运行次数)
t = timeit('func()', 'from __main__ import func', number=10)
print(t)

'''
4999950000
4999950000
4999950000
4999950000
0.057812399999999986
'''