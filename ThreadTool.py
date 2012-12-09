#!/usr/bin/env python
#encoding:utf-8

import threading
import time

def logT(msg):
    #print msg
    name = threading.currentThread().getName()
    with open(name,"a") as f:
        f.write(msg)
        f.write("\n")
def displayThreadStatus(sleeptime=10):
    def status():
        while True:
            time.sleep(sleeptime)
            l = []
            for i in threading.enumerate():
                l.append(i.getName())
            print l

    t = threading.Thread(target=status,name="status Thread")
    t.start()
