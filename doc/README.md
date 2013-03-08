# 各文件描述
## 注意这些文件有的放在 lib/ 目录里面

analysis.py

    Analysis 用来从页面中提取链接，过滤结果数据

status.py

    程序每隔10秒在屏幕上打印进度信息

args.py

    用来处理参数，显示使用文档

linkM.py

    用来过滤已经抓取过的链接,提取出同一个网站的链接

resultSaver.py

    是用来负责将数据存储到sqlite数据库的

log.py

    处理日志格式的

wget.py

    用来下载页面，将页面编码转换为utf-8,以及记录下载页面的一些信息

mthread.py

    线程池

spider.py

    主运行文件，处理一些杂务，胶水功能

worker.py

    worker 根据链接，抓取一个页面，然后返回提取的新的链接
    和spider 类似，也属于胶水吧
