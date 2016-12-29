# -*- coding: UTF-8 -*-
#参数、解包、变量
from sys import argv
#"import"语句，是将python的功能引入脚本的办法，python不会一下子将它所有的功能给你，
#而是让你需要什么就调用什么。这些"import"可以作为提示，让别人明白代码用到了哪些功能。
#argv是所谓的"参数变量(argument variable)",是一个非常标准的编程术语。
#在其他的编程语言也可以看到它，这个变量包含了传递给python的参数。

script, first, second, third = argv 
#上面将argv"解包(unpack)",与其将所有参数放在同一个变量下面，不如将每一个参数赋予一个变量名，
#script, first, second, third。这也许看上去有些些奇怪，不过"解包"可能是最好的描述方式了。
#它的含义很简单："把argv中的东西解包，将所有的参数依次赋予左边的变量"。

print "the script is called:", script
print "your first variable is:",first
print "your second variable is:",second
print "your third variable is:",third

from sys import argv
script,book,dream,music = argv#为什么前面要添加脚本script才可以运行呢？

book = raw_input("what's your favarige book?")
dream = raw_input("what's your dream?")
music = raw_input("你最近听什么音乐?")#命令端显示为乱码

print music 