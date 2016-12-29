# -*- coding: UTF-8 -*-
#打印，打印，打印
# here is some new strange stuff, remember type it exactly.
days = "mon tue wed thu fri sat sun"
months = "jan\nfeb\nmar\napr\nmay\njun\njul\naug" #\n转到下一行

print "here are the days:",days #前面是字符串，逗号后面加变量
print "here are the months: ",months
print """
there's something going on here
with the  three double-quotes
we'll be able to type as much as we we like
enve 4 line if we want ,or 5, or 6.
"""
#"""表示的意思是多行字符串

#两种让字符串扩展到多行的办法。
#第一种办法是在月份之间用\n（back-slash n)隔开。这两个字符的作用是在该位置上放入一份“新行”字符。
#第二种方法是使用“三引号”，也就是"""，可以在一组三引号之间放入任意多行的文字

tabby_cat = "\t i'm tabbed in."
persian_cat = "i'm split\non a line."
backslash_cat = "i'm \\a \\ cat." #转义序列#双反斜杠\\，这两个字符组合打印出一个反斜杠来。
fat_cat = '''
i'll do a list:
\t* cat food
\t* fishies
\t* catnip\n\t* grass
'''
#'''与"""的效果一样

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#转义序列#用反斜杠将单引号'和双引号"转义，不让python以为前后两个引号是字符串的边界，
#让python将引号也包含到字符串里边去。
print "i am 6'2\" tall" #将字符串中的双引号转义，结果 i am 6'2" tall
print 'i am 6\'2" tall'#将字符串中的单引号转义，结果 i am 6'2" tall

#将转义序列与格式化字符串放在一起。
print "i dot't know what to say ti you ,please find my gril's %r before 12'30\"30." % tabby_cat
print "i dot't know what to say ti you ,please find my gril's %s before 12'30\"30." % tabby_cat