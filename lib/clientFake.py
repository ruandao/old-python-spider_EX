#! /usr/bin/env python
# coding: utf-8
# author: ruandao(ljy080829@gmail.com)
"""
为了防止服务器面临太多连接时档掉你，你得自己管理下链接池
"""

import urllib3
import logging

logger_debug = logging.getLogger("dev")


headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'  
} 
http = urllib3.PoolManager(num_pools=10,headers=headers)
def setPoolNum(num=10):
    http = urllib3.PoolManager(num_pools=num,headers=headers)


class Info(object):
    def __init__(self,resp):
        self.resp = resp

    def getheader(self, key, default=None):
        s = self.resp
        s.getheader(key,s.getheader(key.lower(),default))
        return s

class Response(object):
    def __init__(self, resp):
        self.resp = resp

    def read(self):
        d = self.resp.data
        return d

    def info(self):
        return Info(self.resp)

    def getcode(self):
        return self.resp.status

    
def urlopen(urlstring):
    resp = http.urlopen("GET",urlstring)
    return Response(resp)




if __name__ == "__main__":
    import doctest
    print(doctest.testmod())

