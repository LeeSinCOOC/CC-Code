from pymouse import PyMouse
import time
import random
m = PyMouse()
p = m.position()
a = m.screen_size()
len_ = list(range(1360))
hig_ = list(range(760))
for i in range(3600):
    l = random.choice(len_)
    h = random.choice(hig_)
    m.move(l,h)
    cli = m.click(l,h)
    time.sleep(3)
'''print(a)
m.move(196,41)
c = m.click(196,41)
'''
    

