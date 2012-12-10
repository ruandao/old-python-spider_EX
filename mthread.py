#! /usr/bin/env python
# coding: utf-8
# author: ruandao(ljy080829@gmail.com)
"""
ThreadM 是线程池

如何使用:
    e.g.:
        def worker(task):
            # do for task
            # 如果在执行期间会自动创建新的任务的话
            # 那么直接返回新的任务即可
            new_tasks = [ ... ] 
            return new_tasks
        tm = ThreadM(worker, thread_number) # 添加工作函数,和最大线程数
        tm.add(tasks)        # 添加任务
        tm.join()            # 等待所有任务结束
"""

import threading
import time
from Queue import Empty, Queue as queue


class Queue(queue):
    """custom timeout
    x old style python class not support suport 
    """
    def get(self, block=True, timeout=2):
        TIMEOUT = True
        try:
            return queue.get(self,block,timeout), not TIMEOUT
        except (ValueError,Empty) as e:
            return None, TIMEOUT

class Thread(threading.Thread):
    def __init__(self, worker, task_queue, thread_manage):
        super(Thread,self).__init__()
        self.worker = worker
        self.task_queue = task_queue
        self.thread_manage = thread_manage

    def run(self):
        """
        用time_out来控制线程的关闭,没考虑用休眠线程的方法的原因是比较麻烦
        result = self.worker(task) 来处理衍生任务
        """
        while True:
            task, time_out = self.task_queue.get()
            if time_out:
                self.thread_manage.InActiveOne()
                break
            new_tasks = self.worker(task)
            if new_tasks is not None:
                self.thread_manage.add(new_tasks)
            self.task_queue.task_done()

class ThreadM:
    """Thread manage
    test:
    >>> def w(t):
    ...     print t
    >>> tm = ThreadM(w,2)
    >>> l = [ "one", "two", "three"] 
    >>> tm.add(l)
    one
    two
    three
    """
    def __init__(self,worker, max_thread=10,
                 thread_cls=Thread,queue_cls=Queue,lock=threading.RLock()):
        """
        worker 工人
        task_queue 任务发布者，他可以控制任务超时
        """
        self.worker = worker
        self.task_queue = queue_cls()
        self.thread_cls = thread_cls
        self.max_thread = max_thread

        # 下面是用来控制线程状态的
        self.lock = lock
        self.activeThread = 0

    def add(self, tasks):
        for task in tasks:
            self.task_queue.put(task)

        # 判断是否要新建线程
        len_tasks = self.task_queue.qsize()
        with self.lock:
            avail2Create = self.max_thread - self.activeThread
            if len_tasks > avail2Create:
                startThread = avail2Create
            else:
                startThread = len_tasks

            for i in range(startThread):
                self.ActiveOne()


    def status(self):
        """
        返回当前任务数和线程数
        """
        return self.task_queue.qsize(), self.activeThread

    def InActiveOne(self):
        with self.lock:
            self.activeThread -= 1

    def ActiveOne(self):
        t = self.thread_cls(self.worker, self.task_queue, self)
        t.start()
        with self.lock:
            self.activeThread += 1

    def join(self):
        self.task_queue.join()

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())

