#! /usr/bin/env python
# coding: utf-8
# author: ruandao(ljy080829@gmail.com)
"""
根据链接，抓取一个页面，然后返回提取的新的链接
"""

from wget import download

def workerFactory(analysis,linkm,download = download):
    def worker(link):
        link = link if link.startswith("http://") else "http://" + link
        d = download(link)
        content = d.getContent()

        analysis.filterContent(link,content)
        all_link = analysis.getAllLinks(link, content)
        ext_link = linkm.extLinks(link, all_link)
        return ext_link

    return worker

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())

