# -*-coding:UTF-8 -*-
#函数和变量

#函数里边的变量和脚本里边的变量之间是没有连接的。

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "you have %d cheese!" %cheese_count
    print "you have %d boxes of crackers!" %boxes_of_crackers
    print "man that's enough for a party!"
    print "get a blanket!"

#定义函数和函数的内容

print "we can just give the function numbers directly:"
cheese_and_crackers(20, 30)
#赋予函数中参数的值之后会运行函数

print "or, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "we can even do math inside too:"
cheese_and_crackers(10+20, 5+6)

print "and we can combine the two,variables and math:"
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)

#函数的参数和生成变量时用的=赋值符类似。
#事实上，如果一个物件可以用=将其命名，通常也可以将其作为参数传递给一个函数。