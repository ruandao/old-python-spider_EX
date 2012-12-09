#! /usr/bin/env python
# coding: utf-8
# author: ruandao(ljy080829@gmail.com)


import time
import threading
from urlparse import urlparse
import urllib2
from ThreadTool import logT

class LinkM:
    """
    用来过滤已经抓取过的链接
    """
    linkDeep        = {}    # 用于记录链接的深度
    record_links    = set() # 用于记录接触过的链接，包括抓取的linkDeep和待抓取的wait_links
    def __init__(self, deep=2,lock = threading.RLock()):
        self.mutex = lock
        self.deep = 2

    def addLink(self, link, deep):
        with self.mutex:
            self.linkDeep[link] = deep
    def extLinks(self,father, children):
        """
        1. 过滤掉不是本域名的链接
        2. 过滤掉已经抓取过的链接
        3. 由于处于多线程环境，去重时需要加锁
        """
        if len(self.linkDeep) == 0 :
            self.addLink(father, 0)
            self.host = urllib2.Request(father).get_host()
        deep = self.linkDeep.get(father)
        deep += 1
        if deep > self.deep:
            return []
        wait_links = []
        # 1
        for link in children:
            host = urllib2.Request(link).get_host()
            if self.host in host:
                wait_links.append(link)

        with self.mutex:
            wait_links = list(set(wait_links) - set(self.record_links))
            for l in wait_links:
                self.linkDeep[l] = deep
            # 更新set
            self.record_links = self.record_links | set(wait_links)
        return wait_links


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())

