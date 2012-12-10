#! /usr/bin/env python
# coding: utf-8
# author: ruandao(ljy080829@gmail.com)
"""
LinkM 用来过滤已经抓取过的链接,提取出同一个网站的链接
"""


import time
import threading
from urlparse import urlparse
import urllib2

class LinkM(object):
    """
    LinkM 用来过滤已经抓取过的链接,提取出同一个网站的链接
    >>> lm = LinkM(2)
    >>> lm.extLinks("http://www.hao123.com/desknew.html",["http://pic.hao123.com/image/625851", "http://v.hao123.com/movie/","http://book.hao123.com/","http://www.hao123.com/desknew.html"])
    ['http://www.hao123.com/desknew.html']
    >>> lm.extLinks("http://www.hao123.com/desknew.html",["http://book.hao123.com/","http://www.hao123.com/desknew.html","http://pic.hao123.com/","http://gouwu.hao123.com/sc/","http://xyx.hao123.com/pic_0_0_1_91_0.html","http://www.hao123.com/child","http://www.hao123.com/harcksafe","http://www.hao123.com/stock","http://www.hao123.com/navhtm_navgd","http://hao123.com/stocknew.htm"])
    ['http://www.hao123.com/child', 'http://www.hao123.com/stock', 'http://www.hao123.com/harcksafe', 'http://www.hao123.com/navhtm_navgd']
    """
    linkDeep        = {}    # 用于记录链接的深度
    record_links    = {} # 用于记录接触过的链接，包括抓取的linkDeep和待抓取的wait_links,用来做粗判断
    def __init__(self, deep=0,lock = threading.RLock()):
        self.mutex = lock
        self.deep = deep

    def status(self):
        """
        display finished task number
        """
        return len(self.record_links)

    def addLink(self, link, deep):
        with self.mutex:
            self.linkDeep[link] = deep

    def extLinks(self,father, children):
        """
        1. 过滤掉不是本域名的链接
        2. 过滤掉已经抓取过的链接
        """
        if len(self.linkDeep) == 0 :
            self.addLink(father, 0)
            self.record_links[father]=0
            self.host = urllib2.Request(father).get_host()
        deep = self.linkDeep[father] +1
        if deep > self.deep:
            return []
        wait_links = []
        for link in children:
            host = urllib2.Request(link).get_host()
            # 1
            if self.host in host:
                # 2
                # 粗判断 链接是否访问过
                inRecord = self.record_links.get(link,None)
                if inRecord is None:
                    self.record_links[link] = deep
                    # 精判断
                    with self.mutex:
                        d = self.linkDeep.get(link,None)
                        if d is None:
                            wait_links.append(link)
                            self.addLink(link, deep)

        return wait_links


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())

