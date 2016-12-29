# -*-coding:UTF-8 -*-
#读写文件

#了解各种文件相关的命令（方法/函数）
#close - 关闭文件。跟编辑器的 文件>保存 一个意思
#read - 读取文件内容。可以把结果赋给一个变量。
#readline - 读取文本文件中的一行
#truncate - 清空文件，小心使用该命令
#write(stuff) - 将stuff写入文件
#open - 打开文件

from sys import argv

script, filename = argv

print "we're going to erase %r." %filename #erase删除
print "if you don't want that, hit CTRL-C(^C)."
print "if you do want that, hit RETURN."

raw_input("?") #这个在这里是提示的作用

print "opening the file..."
target = open(filename, 'w') #target对象
#给open多赋予一个'w'参数，是因为open对于文件的写入操作态度是安全第一，
#所以只有特别指定以后，它才会进行写入操作。

print "truncating the file. goodbye!"
target.truncate()

print "now i'm going to ask you for three lines. "

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "i'm going to write these to the file."

target.write(line1)
target.write("\n") #文本过行
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "and finally, we close it."
target.close()

target_again = open(filename)
print target_again.read()
