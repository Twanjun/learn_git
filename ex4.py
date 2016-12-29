#-*- coding: UTF-8 -*-
#变量和命名
#变量（variable)用来指代某个东西的名字。通过使用变量名可以让程序读起来更像自然语言，而且更容易记住程序的内容。
#变量名cars等于100
cars = 100
#变量名space_in_a_car（车位）等于4.0，这里使用浮点数，后面的而程序运行到这个值时，结果会更加准确。
space_in_a_car = 4.0
#变量名drivers司机等于30
drivers = 30
#变量名passengers乘客等于90
passengers = 90
#变量名cars_not_driven（没有开的车）等于cars - drivers，也就是100 - 30 = 70
cars_not_driven = cars - drivers
#变量名cars_driven（有开的车数）等于drivers，也就是30
cars_driven = drivers
#变量名carpool_capacity（车容量）等于120.0
carpool_capacity = cars_driven*space_in_a_car
#变量名average_passengers_per_car平均每辆车人数等于3
average_passengers_per_car = passengers/cars_driven
#average_passengers_per_car中的_是下划线（underscore)字符,这个变量里通常被用作假想的空格，用来隔开单词。
#=（单等号）的作用是将右边的值赋给左边的变量名；==（双等号）的作用是检查左右两边是否相等。


print "there are", cars, "cars available."
print "there are only",drivers,"drivers available."
print "there will be",cars_not_driven,"empty cars today."
print "we can transport",carpool_capacity,"people today."
print "we have",passengers,"to carpool today."
print "we need to put about",average_passengers_per_car,"in each cars."
