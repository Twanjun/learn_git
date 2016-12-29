# -*- coding: UTF-8 -*-
#读取文件

from sys import argv

script, filename = argv

txt = open(filename) 
#open接受一个filename参数，并返回一个值，将这个值赋予一个变量。
#这就是打开文件的方式。

print "here's your file %r:"%filename
print txt.read() #txt接受命令的方式是使用句点dot/period，紧跟着read命令，
#txt.read的意思是：让txt执行read命令，无需任何参数。

print "type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)
#open打开变量file_again文件，将值赋予给txt_again这个变量

print txt_again.read()
#叫txt_again执行read命令，打印出txt_again的值。
#这里的read()如果省略的话，打印出来的就是open(ex15_sample.txt)

txt.close()
