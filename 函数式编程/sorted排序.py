# -*- coding: utf-8 -*-
# @Time     : 2023/10/15 8:12
# @Author   : JiMing
# @File     : sorted排序.py
# @SoftWare : PyCharm

from operator import itemgetter

# sorted排序算法
# 数字比较
number_list = [i for i in range(1, 10)]
print(max(number_list))

# sorted()排序
print(sorted(number_list))
print(sorted(number_list, reverse=True))

# sorted()可以接受一个参数进行排序
digit_list = [10, 20, -11, 111, -2]
sort_value = sorted(digit_list, key=abs)
for i in sort_value:
    print(i, end=' ')
print()

# 字符串排序
string_list = ['bob', 'about', 'Zoo', 'Credit']
print(sorted(string_list))
# 全部转换成小写后排序
print(sorted(string_list, key=str.lower))

# sorted()是一个高阶函数，高阶函数的抽象能力是非常强大的，而且，核心代码可以保持的非常简洁

# example
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    """
    对学生进行姓名排序
    :param t:
    :return:
    """
    return t[0]


L2 = sorted(L, key=by_name)
print(L2)


def by_score(s):
    """
    根据成绩排序
    :param s:
    :return:
    """
    return s[1]


L3 = sorted(L, key=by_score, reverse=True)
print(L3)

# 使用itemgetter
L4 = sorted(L, key=itemgetter(0))
print(L4)
