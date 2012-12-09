#! /usr/bin/env python
# coding: utf-8
# author: ruandao(ljy080829@gmail.com)


import time


class Status:
    """
    收集状态信息, 用于产生进度等信息
    如：每隔10秒在屏幕上打印进度信息
    """
    def add(self, field, info):
        """
        field 是用来记录字段的，即产生信息的来源
        """
        pass

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())

