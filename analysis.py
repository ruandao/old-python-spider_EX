#! /usr/bin/env python
# coding: utf-8
# author: ruandao(ljy080829@gmail.com)

from bs4 import BeautifulSoup 
from urlparse import urljoin
from ThreadTool import logT
import urllib2

class Analysis:
    """
    Analysis was use to filter content in web page, and log it
    """
    def add(self, content):
        pass
    def getAllLinks(self,base_url, content):
        """
        就是提取页面的所有链接,要绝对链接的
        """

        soup = BeautifulSoup(content)
        links = [ link.get('href') for link in soup.find_all('a') if type(link.get('href'))== type('string') ]
        l = []
        for link in links:
            # 万恶的空格
            link = link.strip()
            link = link.split("#")[0]
            if len(link) == 0:
                continue
            link = urljoin(base_url,link)
            host = urllib2.Request(link).get_host()
            if host is None:
                # 防止像 mailto:jubao@vip.163.com 这样的伪链接
                continue
            l.append(link)
        

        links = l
        return links


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())

