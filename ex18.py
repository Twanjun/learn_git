# -*-coding:UTF-8 -*-
#命令、变量、代码、函数(function)

#函数可以做三种事情：
#它们给代码片段命名，就跟“变量”给字符串个数字命名一样。
#它们可以接受参数，就跟你的脚本接受argv一样。参数变量(argument variable)
#通过使用#1和#2，它们可以让你创建“微型脚本”或者“小命令”。


#this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" %(arg1, arg2)
#1告诉 Python 创建一个函数，我们使用到的命令是 def ，也就是“定义(define)”的意思。	
#2def 的是函数的名称。本例中它的名称是 “print_two”，但名字可以随便取，但最好函数的名称能够体现出函数的功能来。
#3告诉函数我们需要 *args (asterisk args)，这和脚本的 argv 非常相似，参数必须放在圆括号 () 中才能正常工作。
#4接着我们用冒号 : 结束本行，然后开始下一行缩进。
#5冒号以下，使用 4 个空格缩进的行都是属于 print_two 这个函数的内容。 其中第一行的作用是将参数解包，这和脚本参数解包的原理差不多。
#6为了演示它的工作原理，我们把解包后的每个参数都打印出来，这和我们在之前脚本练习中所作的类似。
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" %(arg1, arg2)
#函数 print_two 的问题是：它并不是创建函数最简单的方法。
#在 Python 函数中我们可以跳过整个参数解包的过程，直接使用 () 里边的名称作为变量名。这就是 print_two_again 实现的功能。

def print_one(arg1):
    print "arg1: %r" %arg1
#print_one ，它向你演示了函数如何接受单个参数。

def print_none():
    print "i got nothin'."
#print_none ，它向你演示了函数可以不接收任何参数。
	
print_two("zed","shaw")
print_two_again("zed","shaw")
print_one("first!")
print_none()