#-*coding: UTF-8 -*-
#更多文件操作，拷贝一个文件中的内容到另一个文件

from sys import argv
from os.path import exists
#命令exists将文件名字符串作为参数，如果文件存在的话，它将返回true，否则将返回false。

script, from_file, to_file = argv

print "codying from %s to %s " %(from_file, to_file)

#
input = open(from_file)
indata = input.read()

print "the input file is %d bytes long" %len(indata)

print "does the output file exist? %r" %exists(to_file)
#如果to_file文件存在的话，将返回true，否则返回false
print "ready, hit return to continue, ctrl-c to abort."
raw_input()

output = open(to_file, 'w')
output.write(indata)

print "alright, all done."

output.close() #作用相当于保存
input.close()
