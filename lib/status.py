#! /usr/bin/env python
# coding: utf-8
# author: ruandao(ljy080829@gmail.com)
"""
程序每隔10秒在屏幕上打印进度信息
"""


import time
import logging
import threading


logger_status= logging.getLogger("intervalStatus")
logger_debug = logging.getLogger("dev")
def intervalStatus(mthread,linkm,queue, timeout=1):
    """
    timeout 指定时间输出内容
    mthread 提供当前的线程数和任务数
    linkm   提供已经完成的任务数
    queue   用来标志任务是否完成
    """
    # 记录展示过几次信息
    count = 0
    while True:
        x,hadWorkThread= queue.get(timeout=timeout)
        if not hadWorkThread: 
            logger_status.info("total status count: %s" % count)
            logger_debug.info("total status count: %s" % count)
            break
        count +=1
        task, thread = mthread.status()
        # record 的记录包括为抓取的和已经抓取的这个网站（或者说子域名下）的记录
        record = linkm.status()
        log_message = "current task: %s    current thread: %s total record: %s link on this site"% (task,thread,record)
        logger_status.info( log_message )
        logger_debug.info( log_message )
        time.sleep(10)

def displayStatus(mthread,linkm,queue):
    t = threading.Thread(target=intervalStatus, args = (mthread,linkm,queue))
    t.start()


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())

