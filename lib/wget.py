#! /usr/bin/env python
# coding: utf-8
# author: ruandao(ljy080829@gmail.com)

"""
download 用来下载页面，将页面编码转换为utf-8,以及记录下载页面的一些信息
"""

import time
import clientFake
import logging
import chardet


logger_spider = logging.getLogger("spider")
logger_debug  = logging.getLogger("dev")

def getNow():
    return time.strftime("%Y-%m-%d,%H-%M-%S",time.localtime(time.time()))

class download(object):
    """
    >>> d = download("http://hao123.com")
    >>> "<!--e5c0a08b-->" in d.getContent()
    False

    """
    def __init__(self, link, client=clientFake):
        logger_debug.debug("get link:%s",link)
        self.link = link if link.startswith("http://") else "http://" + link
        self.start_time = getNow()
        self.resp = client.urlopen(self.link)
        self.content = self.resp.read()
        self.end_time = getNow()
        self.log()
        logger_debug.debug("get link:%s content-size:%s",link,len(self.content))

    def getContent(self):
        """这里要解决编码问题"""
        coding = chardet.detect(self.content)['encoding']
        if coding in ["GB2312","GBK"]:
            coding = "GB18030"
        elif coding is None:
            return self.content 
        c = self.content.decode(coding)
        c = c.encode("utf-8")
        return c

    def log(self):
        """
        log: link, start_time, end_time, server, http_status, content_size, last_modified
        """
        info = self.resp.info()

        d = {
            "link"              : self.link,
            "start_time"        : self.start_time,
            "end_time"          : self.end_time,
            "server"            : info.getheader("Server"),
            "http_status"       : self.resp.getcode(),
            "content_size"      : info.getheader("Content-Length"),
            "last_modified"     : info.getheader("Last-Modified"),
        }

        logger_spider.info("",extra=d)


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())

