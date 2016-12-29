#-*-coding:UTF-8 -*-
#循环和列表
the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
#这里相当于变量赋值，只不过是多个数值通过列表的方式赋值给变量

#this first kind of for-loop goes through a list
for number in the_count:  #将the_count里的值循环赋值给number
    print "this is count %d" %number

#same as above
for fruits in fruits:
    print "a fruit of type: %s" %fruits

#also we can go through mixed lists too
#notice we have to use %r since we dont't know what's in it 
for i in change:
    print "i got %r" %i

#we can also build lists, first start with an empty one 
elements = []

#then use the range function to do 0 to 5 counts
for i in range(0,6):  #range()表示范围，第一位数为起始数，第二位数为范围一共有几个数
    print "adding %d to the list." %i
	#append is a founction that lists understand
    elements.append(i)

#now we can print them out too
for i in elements:
    print "elements was: %d" %i
