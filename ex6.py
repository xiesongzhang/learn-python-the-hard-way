# -*- coding:utf-8 -*-
#x 赋值一段话 其中数字可以修改参数
x="There are %d types of people." % 10
#设置变量并赋值
binary = "binary"
#设置变量并赋值
do_not="don't"
#y 赋值一段话 其中包含两个变量
y = "Those who know %s and those who %s." % (binary,do_not)
#输出变量
print x
print y
#输出字串符
print "I said: %r." % y
print "I also said: '%s'." % y
#设置变量并赋值
hilarious = False 
joke_evaluation="Isn't that joke so funny?! %r"
#输出字串符
print joke_evaluation % hilarious
#设置变量并赋值
w = "This is the left side of ..."
e = "a string with a right side."
#两个字串符一起输出
print w + e
