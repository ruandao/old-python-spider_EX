#! /usr/bin/env python
# coding: utf-8
# author: ruandao(ljy080829@gmail.com)


class Spawn:
    """
    线程池
    """
    def __init__(self, thread_Number=10):
        self.Count = thread_Number

    def addTask(self,task):
        pass
    def doTask(self, func):
        pass
    def run(self):
        pass



if __name__ == "__main__":
    import doctest
    print(doctest.testmod())

