# -*- coding: utf-8 -*-
# @Time     : 2022/12/14 12:54
# @Author   : JiMing
# @File     : 3.定义函数.py
# @SoftWare : PyCharm
import math

"""
在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:
然后，在缩进块中编写函数体，函数的返回值用return语句返回。
"""


def my_abs(x):
    """
    求绝对值的函数
    :param x: 被求数
    :return: 被求数的绝对值
    """
    # 对x的类型进行判断
    if isinstance(x, (float, int)):
        if x >= 0:
            return x
        else:
            return -x
    else:
        raise TypeError('bad operand type')


# 函数调用
abs_result = my_abs(-10)
print(f"-10的绝对值为: {abs_result}")
try:
    abs_result_1 = my_abs('a')  # 参数类型错误
except TypeError as e:
    print(e)


# 空函数的实现
def nop():
    pass  # 将来要添加的语句就可以将其把pass替换  这里作为占位符


age = 100
if age > 10:
    pass
else:
    pass


# 函数可以放回多个值
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)

    return nx, ny


# move()函数调用
new_x, new_y = move(1, 1, 10, (math.pi / 6))
print("移动的新坐标为: (%d, %d)" % (new_x, new_y))


# demo 求一元二次方程的解

def quadratic(a, b, c):
    """
    一元二次方程组的解
    :param a: 常数1
    :param b: 常数2
    :param c: 常数3
    :return: 解
    """

    # 判断传入的类型是否为数字
    if isinstance(a, int) and isinstance(b, int) and isinstance(c, int):
        # 判读是否有解
        judge_value = math.pow(b, 2) - 4 * a * c
        if judge_value > 0:
            x1 = (-b + math.sqrt(judge_value)) / (2 * a)
            x2 = (-b - math.sqrt(judge_value)) / (2 * a)
        elif judge_value == 0:
            x1 = (-b + math.sqrt(judge_value)) / (2 * a)
            x2 = x1
        else:
            print("这个方程没有解")
            return None
    else:
        raise TypeError('bad operand type')

    return x1, x2


# 调用一元二次方程 test
print(quadratic(2, 3, 1))  # => (-0.5, -1.0)
print(quadratic(1, 3, -4))  # => (1.0, -4.0)
