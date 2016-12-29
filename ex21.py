# -*-coding: UTF-8 -*-
#函数可以返回

def add(a, b):
    print "adding %d + %d" %(a, b)
    return a + b
#函数内容意思：第一行：将a和b加起来；第二行：再把结果返回
	
def subtract(a, b):
    print "subtracting %d - %d" %(a, b)
    return a - b

def multiply(a, b):
    print "multiplying %d * %d" %(a, b)
    return a * b

def divide(a, b):
    print "divding %d / %d" %(a, b)
    return a / b

print "let's do some math with just function!"

age = add(30,5) #当函数结束的时候，将a+b的结果赋予一个变量。
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

#a puzzle for the extra credit, type it in anymay.
print "here is a puzzle."

#what = add(age, subtract(height,multiply(weight,divide(iq,2))))
#顺序，由内往外
one = divide(iq, 2)
two = multiply(weight, one)
three = subtract(height, two)
what = add(age, three)

print "that becomes: ", what, "can you do it by hand?"



