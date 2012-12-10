#! /usr/bin/env python
# coding: utf-8
# author: ruandao(ljy080829@gmail.com)
"""
处理日志格式的
"""


import logging

def logConfig(level=1, logfile="spider.log"):
    formats = {
        1:"%(asctime)s %(name)s %(link)s %(http_status)s",
        2:"%(asctime)s %(name)s %(link)s %(http_status)s %(content_size)s",
        3:"%(asctime)s %(name)s %(link)s %(http_status)s %(content_size)s %(server)s",
        4:"%(asctime)s %(name)s %(link)s %(http_status)s %(content_size)s %(server)s %(last_modified)s",
        5:"%(asctime)s %(name)s %(link)s %(http_status)s %(content_size)s %(server)s %(last_modified)s %(start_time)s %(end_time)s",
    }
    if level > 5 or level < 1:
        raise Exception("level must between 1,5")
    logging.basicConfig(filename=logfile,format=formats[level],level=logging.INFO)

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())

