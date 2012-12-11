#! /usr/bin/env python
# coding: utf-8
# author: ruandao(ljy080829@gmail.com)

import os

def TT(testself):
    """
    >>> TT(True)
    TestResults(failed=0, attempted=2)
    <BLANKLINE>
    TestResults(failed=0, attempted=2)
    <BLANKLINE>
    TestResults(failed=0, attempted=3)
    <BLANKLINE>
    TestResults(failed=0, attempted=4)
    <BLANKLINE>

    """
    if not testself:
        return

    tests = ["analysis.py","wget.py","linkM.py","mthread.py"]
    for testf in tests:
        result = os.popen("python %s" % testf).read()
        print result


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())

