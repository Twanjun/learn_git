# -*-coding: UTF-8 -*-
#更多更多的练习

def break_words(stuff):
    """this function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """sorts the words."""
    return sorted(words)

def print_first_word(words):
    """prints the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """print the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
	
#执行 help(ex25) 和 help(ex25.break_words)，得到模组帮助文档的方式。
#所谓帮助文档就是定义函数时放在 """ 之间的东西，它们也被称作 documentationcomments （文档注解）。
#重复键入 ex25. 是很烦的一件事情。有一个捷径就是用 fromex25import* 的方式导入模组。
#这相当于说：“我要把 ex25 中所有的东西 import 进来。”
#可以执行CTRL-D (Windows 下是 CTRL-Z)来关闭编译器。