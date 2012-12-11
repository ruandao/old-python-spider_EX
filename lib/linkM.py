#! /usr/bin/env python
# coding: utf-8
# author: ruandao(ljy080829@gmail.com)
"""
LinkM 用来过滤已经抓取过的链接,提取出同一个网站的链接
"""


import time
import datetime
import threading
from urlparse import urlparse
import urllib2
import logging

log = logging.getLogger("dev")

class LinkM(object):
    """
    LinkM 用来过滤已经抓取过的链接,提取出同一个网站的链接
    >>> lm = LinkM(2)
    >>> lm.extLinks("http://www.hao123.com/desknew.html",["http://pic.hao123.com/image/625851", "http://v.hao123.com/movie/","http://book.hao123.com/","http://www.hao123.com/desknew.html"])
    []
    >>> lm.extLinks("http://www.hao123.com/desknew.html",["http://book.hao123.com/","http://www.hao123.com/desknew.html","http://pic.hao123.com/","http://gouwu.hao123.com/sc/","http://xyx.hao123.com/pic_0_0_1_91_0.html","http://www.hao123.com/child","http://www.hao123.com/harcksafe","http://www.hao123.com/stock","http://www.hao123.com/navhtm_navgd","http://hao123.com/stocknew.htm"])
    ['http://www.hao123.com/child', 'http://www.hao123.com/harcksafe', 'http://www.hao123.com/stock', 'http://www.hao123.com/navhtm_navgd']
    """
    linkDeep        = {}    # 用于记录链接的深度
    def __init__(self, deep=0,lock = threading.RLock()):
        self.mutex = lock
        self.deep = deep

    def status(self):
        """
        display finished task number
        """
        return len(self.linkDeep)

    def addLink(self, link, deep):
        with self.mutex:
            self.linkDeep[link] = deep

    def extLinks(self,father, children):
        """
        1. 过滤掉不是本域名的链接
        2. 过滤掉已经抓取过的链接
        """
        # caculate cost time on ext not use link
        _start_time = datetime.datetime.now()

        log.debug("extLinks %s children:%-4s  had record:%-4s start",father,len(children),len(self.linkDeep))
        if len(self.linkDeep) == 0 :
            self.addLink(father, 0)
            self.host = urllib2.Request(father).get_host()
        deep = self.linkDeep[father] +1
        log.info("deep: %s link: %s",deep-1, father)
        if deep > self.deep:
            return []
        # 1
        tmp = []
        for link in children:
            host = urllib2.Request(link).get_host()
            if self.host in host:
                tmp.append(link)
        # 2
        wait_links = []
        for link in tmp:
            with self.mutex:
                d = self.linkDeep.get(link,None)
                if d is None:
                    log.debug("extLinks child: %s ",link)
                    wait_links.append(link)
                    self.addLink(link, deep)

        _end_time = datetime.datetime.now()
        _cost_time = _end_time - _start_time
        log.debug("extrace link cost %s seconds %s microsconds",_cost_time.seconds,_cost_time.microseconds)
        log.debug("extLinks %s children:%-4s  had record:%-4s end",father,len(children),len(self.linkDeep))
        return wait_links


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())

