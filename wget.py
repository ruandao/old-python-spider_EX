#! /usr/bin/env python
# coding: utf-8
# author: ruandao(ljy080829@gmail.com)

"""
download 用来下载页面，将页面编码转换为utf-8,以及记录下载页面的一些信息
"""

import time
import urllib
import urllib2
import logging
import chardet



def getNow():
    return time.strftime("%Y-%m-%d,%H-%M-%S",time.localtime(time.time()))

class download(object):
    """
    >>> d = download("http://hao123.com")
    >>> "<!--e5c0a08b-->" in d.getContent()
    True

    """
    def __init__(self, link, client=urllib):
        self.link = link if link.startswith("http://") else "http://" + link
        self.start_time = getNow()
        self.resp = client.urlopen(self.link)
        self.content = self.resp.read()
        self.end_time = getNow()
        self.log()

    def getContent(self):
        """这里要解决编码问题"""
        coding = chardet.detect(self.content)['encoding']
        if coding in ["GB2312","GBK"]:
            coding = "GB18030"
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

        logging.info("",extra=d)


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())

