# -*- coding: utf-8 -*-
# @Time     : 2023/10/13 11:11
# @Author   : JiMing
# @File     : filter过滤函数.py
# @SoftWare : PyCharm

# python 内建的filter函数用于过滤序列
"""
和map()类似，filter()也接收一个函数和一个序列。
和map()不同的时，filter()把传入的函数依次作用于每个元素，
然后根据返回值是True还是False决定保留还是丢弃该元素。
"""


def is_odd(number):
    """
    过滤偶数
    :param number:
    :return:
    """
    return number % 2 == 1


def not_empty(string):
    """
    过滤列表中元素为空格的字符
    :param string:
    :return:
    """
    return string and string.strip()


# 案例使用filter高阶函数求素数
"""
求解过程:
计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：

首先，列出从2开始的所有自然数，构造一个序列：

2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, …

取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：

3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, …

取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：

5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, …

取新序列的第一个数5，然后用5把序列的5的倍数筛掉：

7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, …

不断筛下去，就可以得到所有的素数。
"""


def _odd_iter():
    """构造一个奇数序列 并且这是一个无限序列 因为是一个Iterator 每次使用next()获取其中的值 """
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(number):
    """筛选函数"""
    # 大于0的余数说明不能够被整除，没有因子
    return lambda x: x % number > 0    # 返回一个匿名函数 _not_divisible(3)(10)调用方式


def primes():
    """生成器"""
    yield 2  # 因为最小的整数素数就是2
    it = _odd_iter()  # 初始序列  3 5 7 9 ....... generator对象
    while True:
        n = next(it)
        yield n

        it = filter(_not_divisible(n), it)  # 构造新序列


if __name__ == '__main__':
    # 定义一个包含偶数和奇数的列表
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # 通过filter函数过滤偶数 只保留奇数
    print(list(filter(is_odd, my_list)))

    # 定义一个包含随机字符的字符列表
    my_string_list = ['A', 'AB ', 'C', ' ', '', '# c', None]
    # 通过filter函数过滤其中的空字符
    print(list(filter(not_empty, my_string_list)))

    # 打印1000以内的所有素数 遍历primes这个生成器
    for j in primes():
        if j < 20:
            print(j)
        else:
            break

# 可见用filter()这个高阶函数，关键在于正确实现一个“筛选”函数。
"""
注意到filter()函数返回的是一个Iterator(迭代器)，也就是一个惰性序列，
所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。
"""
