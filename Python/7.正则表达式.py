#!/usr/bin/python

import re
print (re.match('www','www.runoob.com').span())
print (re.match('com','www.runoob.com'))

line = 'Cats are smarter than dogs'

matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!")

matchObj1 = re.match(r'dogs',line,re.M|re.I)

if matchObj1:
    print ("match --> matchObj.groub():",matchObj1.group())
else:
    print ('No match')

matchObj = re.search( r'dogs', line, re.M|re.I)
if matchObj:
   print ("search --> matchObj.group() : ", matchObj.group())
else:
   print ("No match!!")