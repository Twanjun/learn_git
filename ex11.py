# -*- coding: UTF-8 -*-
#提出问题
print "how old are you?",
#print 后面加个逗号，这样的话print就不会输出新行符而结束这一行跑到下一行去了。
age = raw_input()#接受人的输入
print "how tall are you?",
height = raw_input()
print "how much do you weight?",
weight = raw_input()

print "so, you are %r old,%r tall and %r heavy."%(age,height,weight)

#提示别人
#y = raw_input("name?")括号内为提示语，将用户输入的结果赋值给变量y。这就是提示用户并且得到答案的方式。
age = raw_input("how old are you? ")
height = raw_input("how tall are you? ")
weight = raw_input("how much do you weight? ")

print "so, you are %r old,%r tall and %r heavy."%(age,height,weight)
#这两种方法出现的效果是一样的。

