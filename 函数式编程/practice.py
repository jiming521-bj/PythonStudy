# -*- coding: utf-8 -*-
# @Time     : 2023/6/11 21:16
# @Author   : JiMing
# @File     : practice.py
# @SoftWare : PyCharm

from functools import reduce


def str2float(s):
    """
    将含有小数的字符串转换成具体的小数值
    :param s:
    :return:
    """
    # 标志
    flag = 0

    def string_change_float(x):
        """
        将字符转换为数字
        :param x:
        :return:
        """
        return {'.': -1, '0': 0, '1': 1, '2': 2,
                '3': 3, '4': 4, '5': 5, '6': 6,
                '7': 7, '8': 8, '9': 9}[x]

    def do_float(f, n):
        """
        将列表中的每个数组合成整体（整数或者小数）
        :param f: Iterator第一个值
        :param n: Iterator第二个值
        :return:
        """
        # 设置一个非局部变量
        nonlocal flag
        if n == -1:
            flag = 1
            return f  # 返回整数部分
        if flag == 0:
            return f * 10 + n
        else:
            flag = flag * 10  # 设置小数位数
            return f + n / flag

    return reduce(do_float, map(string_change_float, s), 0.0)
    # return list(map(string_change_float, s))  # [1, 2, 3, -1, 4, 5, 6]


"""
do_float(f, n)执行情况
第一次 f = 1	n = 2	flag = 0
第二次 f = 12	n = 3	flag = 0
第三次 f = 123	n = -1 	flag = 1   n的值为-1 标志改变
第四次 f = 123	n = 4	flag = 1   标志改变 if判断时效，走else语句
第五次 f = 123.4	n = 5 	flag = 10
第六次 f = 123.45	n = 6	flag = 100
第七次 f = 123.456 	n = StopIteration 退出迭代 结束函数调用
"""

print('str2float(\'123.456\') =', str2float('123.456'))
