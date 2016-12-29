#-*- coding: utf-8 -*-
#数字和数字运算
print "I will now count my chickens:"
print "hens",25+30/6
#在没有输入脚本第一行的情况下，运行本脚本的时候出现这样的错误：
#SyntaxError(语法错误)：Non-ASCII character '\x86' in file ex2.py on line 7,but no encoding declared;..
#这是关于ASCII编码的错误，在脚本的最上面加入一行-*- coding: utf-8 -*-。
#%是求余符号。而不是百分号，很大程度上只是因为设计人员选择了这个符号而已。正常写作时它是百分号没错，
#在编程中除法用了/，而求余数又恰恰选择了%这个符号，仅此而已。%运算的结果就是求余数。
print "Roosters",100-25*3%4
print "I will count the eggs:"
print 3+2+1-5+4%2-1/4+6
print "Is it true that 3+2<5-7?"
print 3+3<5-7
print "What is 3+2?",3+2
print "What is 5-7?",5-7
print "Oh,that's why it's False."
print "How about some more."
print "Is it greater?",5>-2
print "Is it greater or equal?",5>=-2
print "Is it less or equal?",5<=-2
#7/4运算结果为1，只有整数部分，而没有小数部分，需要将运算值写成浮点数，才能让结果更准确。
print 7/4
#7.0/4.0运算结果为1.75，2.0是一个浮点数。
print 7.0/4.0
print 12-8+3