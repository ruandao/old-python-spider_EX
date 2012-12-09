#! /usr/bin/env python
# coding: utf-8
# author: ruandao(ljy080829@gmail.com)

from task import task
from work import Work
from spawn import Spawn

w = Work()
spawn = Spawn(15,w)
spawn.add(task)


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())

