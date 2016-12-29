# -*- coding: UTF-8 -*-
# 字符串(string)和文本
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary,do_not)
# 如果想在字符串中通过格式化字符放入多个变量，需要将变量放在（）圆括号中，而且
# 变量之间用，逗号隔开。

print x
print y 

print "I said: %r." % x 
print "I also said: '%s'." % y 
# 这里的%r没有用引号，而%s用引号是因为%r直接调用字符串，而%s只是调用变量引号内的字符串

hilarious = False #这里的False必须大写
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e