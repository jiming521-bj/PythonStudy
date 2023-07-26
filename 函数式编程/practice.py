# -*- coding: utf-8 -*-
# @Time     : 2023/6/11 21:16
# @Author   : JiMing
# @File     : practice.py
# @SoftWare : PyCharm

from functools import reduce


def str2float(s):
    """
    将字符串转换成具体的小数值
    :param s:
    :return:
    """

    def string_change_float(x):
        """
        将字符转换为数字
        :param x:
        :return:
        """
        return {'.': -1, '0': 0, '1': 1, '2': 2,
                '3': 3, '4': 4, '5': 5, '6': 6,
                '7': 7, '8': 8, '9': 9}[x]

        # 标志

    flag = 0

    def do_float(f, n):
        """
        将列表中的每个数组合成整体（整数或者小数）
        :param f:
        :param n:
        :return:
        """
        nonlocal flag
        if n == -1:
            flag = 1
            return f
        if flag == 0:
            return f * 10 + n
        else:
            flag = flag * 10
            return f + n / flag

    return reduce(do_float, map(string_change_float, s), 0.0)


print('str2float(\'123.456\') =', str2float('123.456'))
