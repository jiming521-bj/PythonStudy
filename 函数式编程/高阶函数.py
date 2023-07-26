# -*- coding: utf-8 -*-
# @Time     : 2023/6/9 10:57
# @Author   : JiMing
# @File     : 高阶函数.py
# @SoftWare : PyCharm

# 高阶函数
"""
1 变量名可以指向函数
2 函数名也是变量
3 传入函数
"""

# 变量可以指向函数
test_number = abs(-1)
print(test_number)
print(abs)  # 得到的结果就是一个函数

# 可见abs是一个函数 abs(-1)是一个函数调用

# 将abs函数直接赋值给一个变量
f = abs  # 函数本身可以赋值给变量
print(f(-10))  # 10  变量可以指向函授
# 调用abs() 和 f() 作用相同


# 函数名也是变量: 函数名其实就是指向函数的变量 abs就是指向实现求绝对值的函数
# 将abs指向其他对象
# abs = 10

# 由于abs函数实际上是定义在builtin模块中的，所以要让修改abs变量的指向在其它模块也生效，
# 要用builtin.abs = 10
try:
    print(abs(-10))
except TypeError as e:
    print(e)

# 传入函数
"""
既然变量可以指向函数，函数可以接受参数传递，那么一个函数可以接收另一个
函数作为参数，这种我们就称为“高阶函数”
"""


def add(number_1, number_2, absCopy):
    """
    计算两个数字绝对值的和
    :param number_1: 第一个参数值
    :param number_2: 第二个参数值
    :param absCopy:  函数
    :return: |number_1| + |number_2|
    """
    # return abs(10) + abs(-10)
    return absCopy(number_1) + absCopy(number_2)


if __name__ == '__main__':
    result = add(10, -10, abs)
    print(result)


