# -*- coding: utf-8 -*-
# @Time     : 2023/10/15 15:21
# @Author   : JiMing
# @File     : 匿名函数.py
# @SoftWare : PyCharm

from functools import reduce

# 不需要显示地定义函数，直接传入匿名函数更方便
print(list(map(lambda x: x * x, [i for i in range(1, 10)])))


def f(x):
    return x * x


L = list(map(f, [j for j in range(1, 10)]))
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
# lambda x: return x

"""
用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。
此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
"""


# 匿名函数作为返回值返回
def build(x, y):
    return lambda z: x * x + y * y + z


if __name__ == '__main__':
    print(L)

    # 匿名函数赋值给变量
    my_evaluation = lambda x, y: x * 10 + y

    # 打印my_evaluation
    print(my_evaluation)

    # 拼接数组为数字
    print(reduce(my_evaluation, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

    # 调用返回值为匿名函数的函数
    print(build(10, 10)(10))
