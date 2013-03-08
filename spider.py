#!/usr/bin/env python
#encoding:utf-8
"""
主运行文件，处理一些杂务
"""
import site;site.addsitedir('.')
import sys
from worker import workerFactory
from status import displayStatus
from args import getOpt
from linkM import LinkM
from resultSaver import SaveMethod
from analysis import Analysis
from log import logConfig
from mthread import ThreadM,Queue
from testself import TT
from clientFake import setPoolNum


# 获取参数
options         = getOpt()

url             = options.url
deep            = options.deep
dbfile          = options.dbfile
threadNumber    = options.threadNumber
conNumber    = threadNumber
keyword         = options.key
logfile         = options.logfile
loglevel        = options.loglevel
testself        = options.testself

# 设置日志文件
logConfig(loglevel,logfile)
# 设置连接数,与线程数相同
setPoolNum(conNumber)
# 自测
TT(testself)
# 设置任务
tasks = [ url,]
# 设置数据库存储文件
saver = SaveMethod(dbfile)
# 设置关键字，以及将设置好的数据存储方式saver传递给分析人员
analysis = Analysis(saver, keyword)
# 设置搜索深度
linkm = LinkM(deep)

w = workerFactory(analysis,linkm)
tm = ThreadM(w,max_thread=threadNumber)
jobsDone = Queue()
# 定期显示任务完成情况
displayStatus(tm, linkm, jobsDone)

# 添加任务
tm.add(tasks)
# 等待任务完成
tm.join()
# 任务完成后通知displayStatus 自杀
jobsDone.put(True)

