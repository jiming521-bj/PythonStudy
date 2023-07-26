# -*- coding: utf-8 -*-
# @Time     : 2023/6/9 11:15
# @Author   : JiMing
# @File     : mapANDreduce.py
# @SoftWare : PyCharm
from functools import reduce

print("吉明")
# Python内建了map()和reduce()函数。

# map函数
"""
map()函数接收两个参数，一个是函数，一个是Iterable，
map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
"""


def square(number):
    """
    求number的平方值
    :param number: 任意的整数
    :return: 平方值
    """
    return number * number


def int_change_str(x):
    """
    将数字转换为字符串
    :param x:
    :return:
    """
    return str(x)


def printResult():
    """
    输入字符结果
    :return:
    """
    strList = []

    for i in [1, 2, 3, 4, 5, 6]:
        strList.append(int_change_str(i))
    print(strList)


# reduce函数
"""
reduce把一个函数作用在一个序列[x1, x2, x3, …]上，这个函数必须接收两个参数，
reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
"""


def addReduce(a, b):
    """
    求两个数字的和
    :param a: 第一个整数
    :param b: 第二个整数
    :return: 两个数字的和
    """
    return a + b


def testReduce():
    """
    测试reduce函数的结果
    :return:
    """
    print(reduce(addReduce, [1, 2, 3, 4, 5, 6, 7, 8, 9]))


# 将 1 2 3 4 5 6转换成123456
def fn(x, y):
    """
    将列表中的数字顺序组合为一个整数
    :param x: 第一个数字
    :param y: 第二个数字
    :return:  最终结果
    """
    return x * 10 + y


def string_change_int(x):
    """
    将字符串转化成数字
    :param x:
    :return:
    """
    return {'0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9}[x]


def intResult():
    """
    输出的结果
    :return:
    """
    print(reduce(fn, [1, 2, 3, 4, 5, 6]))


def str2int(string):
    """
    将字符串转化成整数
    :param string:
    :return:
    """
    def char2num(s):
        return {'0': 0,
                '1': 1,
                '2': 2,
                '3': 3,
                '4': 4,
                '5': 5,
                '6': 6,
                '7': 7,
                '8': 8,
                '9': 9}[s]

    return reduce(lambda x, y: x * 10 + y, map(char2num, string))


if __name__ == '__main__':
    result = map(square, [1, 2, 3, 4, 5, 6])  # 得到一个Iterator
    print(list(result))  # 将Iterator转换成列表
    printResult()
    print(list(map(str, [1, 2, 3, 4, 5])))  # 将列表中的每一个数字转化成字符

    testReduce()
    intResult()

    # 将字符串转换成数字
    print(reduce(fn, map(string_change_int, "1212")))

    print(str2int('9090'))

