# -*- coding: utf-8 -*-
# @Time     : 2023/11/5 12:31
# @Author   : JiMing
# @File     : my_collections.py
# @SoftWare : PyCharm
from collections import namedtuple


# collections 是Python内建的一个集合模块，提供了许多有用的集合类
# tuple 表示不可变对象
def test01():
    """namedtuple"""
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1, 2)
    print(p.x)
    print(p.y)


if __name__ == '__main__':
    test01()
