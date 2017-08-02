# -*- coding:utf-8 -*-

from sys import argv

script, filename = argv

txt = open(filename)
#argv 函数获取需要打开的文件名字，然后用open函数获取文件

print "Here's your file %r:" % filename
print txt.read()
#输出文件名、用read函数打开文件


