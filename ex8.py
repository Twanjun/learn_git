# -*- coding: UTF-8 -*-
# 打印，打印
formatter = "%r %r %r %r"

print formatter % (1,2,3,4) #这里的结果是1 2 3 4
print formatter % ("one","two","there","four") #运行结果是'one' 'two' 'there' 'four'
print formatter % (True,False,False,True) #运行结果True False False True
print formatter % (formatter,formatter,formatter,formatter) 
#运行结果是'%r %r %r %r' '%r %r %r %r' '%r %r %r %r' '%r %r %r %r'
# 而不是formatter formatter formatter formatter
print formatter % (
"I had this thing.",
"That you could type up right.",
"But it didn't sing.",
"So I said goodnight."
)
# 运行结果'I had this thing.''That you could type up right.'
# "But it didn't sing."'So I said goodnight.'这一行程序中既有单引号也有双引号
# 这是因为当字符串中有单引号时，程序就会选择用双引号