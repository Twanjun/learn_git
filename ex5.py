# -*- coding: UTF-8 -*-
#更多的变量和打印
#这次要键入更多的变量并且把它们都打印出来。将使用一个叫“格式化字符串”（format string)的东西。
#每一次使用双引号（"）把一些文本引用起来，就创建了一个字符串。字符串是程序向人展示信息的方式。
#可以打印（显示）它们，可以将它们写入文件，还可以将它们发送给网站服务器，很多事情都是通过字符串交流实现的。
#字符串是非常好用的东西，在这个习题中将学会创建包含变量内容的字符串，
#使用专门的格式和语法把变量的内容放到字符串里，相当于告诉python这是一个格式化字符串，把这些变量放到那几个位置。

my_name = 'tang wan jun'
my_age = 23 # not a lie
#60英寸 = 大约153厘米
my_height = 60.0 # inches（英寸）
inches = 2.54  #1英寸 = 2.54 厘米 1不是一个有效的变量名称，变量名称要以字母开头，所以a1可以，但1不行。
#40千克 = 88磅
my_weight = 88.0 # lbs
lbs = 0.4536 #1磅大约 = 0.45千克
my_eyes = 'black'
my_teech = 'white'
my_hair = 'black'
my_height_cm = my_height * inches
my_weight_km = my_weight * lbs
#file "ex.py",line 20
#  my_height(cm) = my_height * inches  # my_height(cm)应该为my_height_cm
#SyntaxError:can't assign to function call（不能分配函数调用）
#错误TypeError: 'str' object is not callable. 很有可能是漏写了字符串和变量之间的%。

print "Let's talk about %s." % my_name
print "She's %d cm tall." % my_height_cm
print "She's %d km heavy." % my_weight_km  #为什么my_weight_km结果是39？
print "Autually that's too thin."
print "She's got %s eyes and %s hair." % (my_eyes, my_hair)
print "Her teech are usually %s depending on the coffee." % my_teech

# this line is tricky, try to get it exactly right
# 字符串中的“,”,空格符号，运行结果将显示出来。
print "if I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)
# 结果：if I add 23, 74, and 80 I get 177.

name = 'tang wan jun'
age = 23 # not a lie
height = 74 # inches
weight = 80 # lbs
eyes = 'black'
teech = 'white'
hair = 'black'

print "Let's talk about %s." % name
print "She's %d inches tall." % height
print "She's %d pounds heavy." % weight
print "Autually that's too thin."
print "She's got %s eyes and %s hair." % (eyes, hair)
print "Her teech are usually %s depending on the coffee." % teech

# this line is tricky, try to get it exactly right
print "if I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

# 将my_去掉，以上两种变量运行结果一样。
# 部分Python格式化字符介绍
#格式化字符是一种“格式控制工具”，它们告诉python把右边的变量带到字符串中，并且把变量的值放在%s所在的位置。
# %% 百分号标记 #就是输出一个% 
# %c 字符及其ASCII码 
# %s 字符串 
# %d 有符号整数(十进制) 
# %u 无符号整数(十进制) 
# %o 无符号整数(八进制) 
# %x 无符号整数(十六进制) 
# %X 无符号整数(十六进制大写字符) 
# %e 浮点数字(科学计数法) 
# %E 浮点数字(科学计数法，用E代替e) 
# %f 浮点数字(用小数点符号) 
# %g 浮点数字(根据值的大小采用%e或%f) 
# %G 浮点数字(类似于%g) 
# %p 指针(用十六进制打印值的内存地址) 
# %n 存储输出字符的数量放进参数列表的下一个变量中
# %r 直接调用字符串