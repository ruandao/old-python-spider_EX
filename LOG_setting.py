#! /usr/bin/env python
# coding: utf-8
# author: ruandao(ljy080829@gmail.com)
"""
"""
import logging

LOG_CONFIG = {
    "version":1,
    "formatters":{
        "1":{ "format":"%(asctime)s %(name)s %(link)s %(http_status)s"},
        "2":{ "format":"%(asctime)s %(name)s %(link)s %(http_status)s %(content_size)s"},
        "3":{ "format":"%(asctime)s %(name)s %(link)s %(http_status)s %(content_size)s %(server)s"},
        "4":{ "format":"%(asctime)s %(name)s %(link)s %(http_status)s %(content_size)s %(server)s %(last_modified)s"},
        "5":{ "format":"%(asctime)s %(name)s %(link)s %(http_status)s %(content_size)s %(server)s %(last_modified)s %(start_time)s %(end_time)s"},
        "debug_format":{
            "format":"%(levelname)s %(threadName)-15s%(filename)-15s%(module)+10s.%(funcName)-10s%(asctime)-25s%(message)s",
        },
        "intervalStatus_format":{
            "format":"%(message)s",
        },
    },

    "handlers":{
        "record":{
            "class":"logging.FileHandler",
            "filename":"spider.log",
            "formatter":"1",
            "level":"INFO",
        },
        "debug_handler":{
            "class":"logging.FileHandler",
            "filename":"debugfile.log",
            "formatter":"debug_format",
            "level":"INFO",
        },
        "intervalStatus_handler":{
            "class":"logging.StreamHandler",
            "formatter":"intervalStatus_format",
            "level":"INFO",
        },
    },
    "loggers":{
        "intervalStatus":{
            "level":"INFO",
            "handlers":["intervalStatus_handler",],
        },
        "dev":{
            "level":"DEBUG",
            "handlers":["debug_handler",],
        },
        "spider":{
            "level":"INFO",
            "handlers":["record",],
        },
    },
}
