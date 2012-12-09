#! /usr/bin/env python
# coding: utf-8
# author: ruandao(ljy080829@gmail.com)


import time
import urllib
import urllib2


def getNow():
    return time.strftime("%Y-%m-%d,%H-%M-%S",time.localtime(time.time()))

class download(object):
    def __init__(self, link, client=urllib):
        self.link = link
        self.start_time = getNow()
        self.resp = client.urlopen(link)
        self.content = self.resp.read()
        self.end_time = getNow()
    def getContent(self):
        return self.content
    def status(self):
        """
        return link, start_time, end_time, server, http_status, content_size, last_modified
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

        return d


if __name__ == "__main__":
    d = download("http://hao123.com")
    print d.getContent()
    print d.status()
    import doctest
    print(doctest.testmod())

