#! /usr/bin/env python
# coding: utf-8
# author: ruandao(ljy080829@gmail.com)
"""
处理日志格式的
"""


import logging
from logging import config
import LOG_setting

# 防止配置文件丢失时，信息直接刷在终端上
logging.root.addHandler(logging.NullHandler())

def logConfig(level=1, logfile="spider.log"):
    """
    """
    if level > 5 or level < 1:
        raise Exception("level must between 1,5")

    pass
    # modify LOG_CONFIG

    LOG_setting.LOG_CONFIG["handlers"]["record"]["filename"] = logfile
    LOG_setting.LOG_CONFIG["handlers"]["record"]["level"] = logging.getLevelName(level*10)

    config.dictConfig(LOG_setting.LOG_CONFIG)
