#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time,calendar

localtime = time.localtime(time.time())
print '本地时间：',localtime
newTime = time.asctime(localtime)
print newTime

print time.strftime('%Y-%m-%d %H:%M：%S',time.localtime())
print time.strftime('%a %b %d %H:%M:%S %Y',time.localtime())

a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))


cal = calendar.month(2016,1)
print cal