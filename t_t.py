#! /usr/bin/env python
# coding: utf-8
# author: ruandao(ljy080829@gmail.com)

import random
import time
import threading


main_t = threading.currentThread()
print 'main : %s ' % main_t.getName()
def worker(n):
    ran = n*random.randint(1,10)
    print threading.currentThread().getName(), ' sleep %s' % ran
    time.sleep(ran)
    print threading.currentThread().getName(), ' Exit'

for i in range(5):
    t = threading.Thread(target=worker,args=(4,))
    #t.setDaemon(True)
    t.start()

l = []
for t in threading.enumerate():
    if t is main_t:
        continue
    l.append(t)

for t in l:
    print t.getName(),

print
for t in l:
    t.join(3)
    print t.getName(), ' join'

