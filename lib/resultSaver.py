#! /usr/bin/env python
# coding: utf-8
# author: ruandao(ljy080829@gmail.com)
"""
Result 是数据库的表对应的模型
SaveMethod 是用来负责将数据存储到sqlite数据库的
"""

from sqlobject import *
import os
import threading

class Result(SQLObject):
    link = StringCol()
    keyword = StringCol()
    content = StringCol()
class SaveMethod(object):
    def __init__(self,dbfile="spider.sqlite3", lock=threading.RLock()):
        self.lock = lock
        dbfile = os.path.abspath(dbfile)
        connection_string = 'sqlite:' + dbfile
        connection = connectionForURI(connection_string)
        # The sqlhub.processConnection assignment means that all classes will, by default, use this connection we've just set up.
        sqlhub.processConnection = connection

        Result.createTable(ifNotExists=True)

    def saveContent(self, dic):
        # just save it
        with self.lock:
            Result(**dic)


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())

