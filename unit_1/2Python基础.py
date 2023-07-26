# -*- coding: utf-8 -*-
# @Time     : 2022/12/1 12:48
# @Author   : JiMing
# @File     : 2Python基础.py
# @SoftWare : PyCharm
"""
Python是一种计算机编程语言。计算机编程语言和我们日常使用的自然语言有所不同，
最大的区别就是，自然语言在不同的语境下有不同的理解，而计算机要根据编程语言执行任务，
就必须保证编程语言写出的程序决不能有歧义，所以，任何一种编程语言都有自己的一套语法，
编译器或者解释器就是负责把符合语法的程序代码转换成CPU能够执行的机器码，然后执行。
Python也不例外。
"""
# print absolute value of integer
number = input("Please Enter a number: ")
number = int(number)

if number >= 0:
    print(number)
else:
    print(-number)
