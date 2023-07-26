# -*- coding: utf-8 -*-
# @Time     : 2022/12/21 13:34
# @Author   : JiMing
# @File     : 5.递归函数.py
# @SoftWare : PyCharm
# 在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。

def face(n):
    """
    求n的阶乘
    :param n: 整数阶乘
    :return: 阶乘值
    """
    if n == 1:
        return 1
    return n * face(n - 1)


# 使用尾部递归的方法防止栈溢出
def face_iter(num, product):
    """
    求num的阶乘
    :param num: num数字阶乘
    :param product: num阶乘值
    :return: 阶乘值
    """
    if num == 1:
        return product
    return face_iter(num - 1, num * product)


def face_1(n):
    return face_iter(n, 1)


def test_1(n):
    """
    测试n的阶乘
    :return:
    """
    result = face(n)
    print(f"{n}的阶乘值为: {result}")


def test_2(n):
    """
    测试n的阶乘值 第二版
    :return:
    """
    result = face_1(n)
    print(f"{n}的阶乘值为: {result}")


# 1到n的阶乘之和
def test_3(n):
    sum_result = 0
    for i in range(1, n + 1):
        sum_result += face(i)
    else:
        print(f"{n}!到1!的阶乘和为: {sum_result}")


# 汉诺塔
def hanoi(n, a, b, c):
    """
    将a柱子上的盘子移动到c柱子上
    :param n:  盘子个数
    :param a:  a柱子
    :param b:  b柱子
    :param c:  c柱子
    :return:
    """

    # 当盘子只有一个的时候
    if n == 1:
        print(a, '-->', c)
    else:
        hanoi(n - 1, a, c, b)
        print(a, '-->', c)
        hanoi(n - 1, b, a, c)


if __name__ == '__main__':
    test_1(5)
    test_2(2)
    test_3(5)
    hanoi(3, 'A', 'B', 'C')

"""
解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，
所以，把循环看成是一种特殊的尾递归函数也是可以的。

遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，
所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。
"""
