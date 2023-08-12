# -*- coding: utf-8 -*-
# @Time     : 2023/8/12 17:32
# @Author   : JiMing
# @File     : fun_test.py
# @SoftWare : PyCharm
from functools import reduce


def number_power(number, n=1):  # 该n中的1值为默认参数
    """
    求一个数的n次方值
    :param number:  预求值
    :param n: 次方数
    :return:  最终结果
    """
    # 定义存储结果的临时变量
    result = 1
    while True:
        """循环执行该数自乘"""
        result *= number
        n -= 1

        if n == 0:
            break
    return result


def add_end(L=[]):  # 该L为list，是可变默认参数
    """
    定义参数为可变对象 list
    :param L:
    :return:
    """
    L.append('End')
    return L


def add_start(L=None):
    """
    将可变参数转换为不可变参数
    :param L:
    :return:
    """
    if L is None:
        L = []
    L.append('start')
    return L


def calc(numbers):
    """
    计算列表中元素的平方值的总和
    :param numbers: 元素列表
    :return: 总和
    """
    # 定义一个临时存放总和的临时变量
    result = 0

    for number in numbers:
        result = result + number * number

    return result


def list_reduce_calc(x, y):
    """
    使用reduce函数求迭代数字
    :param x:
    :param y:
    :return:
    """
    # 计数器
    return x * 10 + y


if __name__ == '__main__':
    # 测试3的5次方结果
    print(f"3的5次方的结果为: {number_power(3, 5)}")

    # print(add_end([1, 2, 3, 4]))
    for i in range(3):
        print(add_end())

    # 不可变参数的例子
    for j in range(3):
        print(add_start())  # 每次调用函数会重新定义L

    # 列表中元素的总和
    print(calc([1, 2, 3, 4, 5]))
    print(reduce(list_reduce_calc, [1, 2, 3, 4, 5]))

# 总结： 定义默认参数要牢记一点：默认参数必须是不可变对象 比如 str int None
