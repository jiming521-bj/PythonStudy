# -*- coding: utf-8 -*-
# @Time     : 2023/11/6 18:50
# @Author   : JiMing
# @File     : my_itertools.py
# @SoftWare : PyCharm
# Python的内建模块itertools提供了非常有哟红的由于操作迭代对象的函数

import itertools


# 无限迭代
def test01():
    natual = itertools.count(1)
    for n in natual:
        if n == 1000:
            break
        print(n)

    """
    因为count()会创建一个无限的迭代器，所以上述代码会打印出自然数序列，根本停不下来，只能按Ctrl+C退出。
    """


def test02():
    """cycle()接收一个序列然后不断无限重复下去"""
    cs = itertools.cycle('ABC')
    i = 1
    for c in cs:
        print(c, end=' ')
        if i % 50 == 0:
            print()
        # 当计数器达到1000时对出循环
        if i == 1000:
            break
        i = i + 1


def test03():
    # repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复的次数
    ns = itertools.repeat('A', 3)
    for n in ns:
        print(n, end=' ')
    print('end')

    """
    无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，
    它不会事先把无限个元素生成出来，事实上也不可能在内存中创建无限多个元素。
    """


def test04():
    # 通常使用takewhile()函数根据条件判断来截取出一个有限的序列
    natual = itertools.count(1)
    ns = itertools.takewhile(lambda x: x <= 10, natual)
    print(list(ns))


def test05():
    """chain()和groupby()"""
    # chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
    for c in itertools.chain('ABC', 'XYZ'):
        print(c, end=' ')
    print()

    # groupby()把迭代器中相邻的重复元素挑出来放在一起
    for key, group in itertools.groupby('AABBCCAAAABBBBDDDD'):
        print(key, list(group))


if __name__ == '__main__':
    # test01()
    # test02()
    # test03()
    # test04()
    test05()
    pass
