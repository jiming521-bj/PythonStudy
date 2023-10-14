# -*- coding: utf-8 -*-
# @Time     : 2023/10/15 8:42
# @Author   : JiMing
# @File     : 返回函数.py
# @SoftWare : PyCharm

# 函数作为返回值
def calc_number(*args):
    """可变参数求和"""
    ax = 0
    for n in args:
        ax = ax + n
    return ax


# 返回可变参数的求和函数
def lazy_sum(*args):
    def sum_number():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum_number


"""
在这个例子中，我们在函数lazy_sum中又定义了函数sum，
并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，
这种称为“闭包（Closure）”的程序结构拥有极大的威力。
"""

# 闭包
"""
注意到返回的函数在其定义内部引用了局部变量args，
所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，
所以，闭包用起来简单，实现起来可不容易。
"""


def count():
    # 定义一个列表 用于存储函数返回的数据
    fs = []
    for i in range(1, 5):
        def power():
            return i * i

        fs.append(power)
    return fs


def count01():
    """ 利用函数传参给目标函数传参再返回 可以实现立即执行"""

    def g(j):
        return lambda: j * j

    value_list = []
    for i in range(1, 5):
        value_list.append(g(i))
    return value_list


def test01():
    f = lazy_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    f1 = lazy_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    # f和f1是两个不同的函数返回对象
    print(f == f1)

    result = f()
    print(result)


def test02():
    """返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量"""
    value1 = count()
    for i in value1:
        print(i(), end=' ')  # 全部都是16 原因是在count()函数的for循环中i的值没有立即执行
    print()


def test03():
    values = count01()
    for i in values:
        print(i(), end=' ')
    print()


if __name__ == '__main__':
    # 引入闭包
    test01()
    # 测试闭包返回值
    test02()
    # 立即执行闭包
    test03()
