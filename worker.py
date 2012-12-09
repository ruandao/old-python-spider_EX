#! /usr/bin/env python
# coding: utf-8
# author: ruandao(ljy080829@gmail.com)

from wget import download
from analysis import Analysis
from linkM import LinkM
from ThreadTool import logT,displayThreadStatus

def workerFactory(Scratch = download,Analyer = Analysis,linkM = LinkM):
    analyer = Analyer()
    linkFilter = linkM()

    def worker(link):
        logT(link)
        d = Scratch(link)
        content = d.getContent()
        status = d.status()

        all_link = analyer.getAllLinks(link, content)
        ext_link = linkFilter.extLinks(link, all_link)
        return ext_link

    return worker

if __name__ == "__main__":
    from mthread import ThreadM 
    w = workerFactory()
    tm = ThreadM(w)
    tasks = [ "http://data.book.163.com/book/home/009200010009/000BOMbG.html", ]
    tm.add(tasks)
    displayThreadStatus()

