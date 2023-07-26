# -*- coding: utf-8 -*-
# @Time     : 2022/12/13 20:01
# @Author   : JiMing
# @File     : 1.函数.py
# @SoftWare : PyCharm

PI = 3.1415926


def area(r):
    """
    计算不同半径的圆的面积
    :param r: 半径值
    :return: PI * r * r
    """

    return PI * r * r


# 调用函数
r1 = 2
r2 = 4
r3 = 6

print(f"第一个圆的面积为: {round(area(r1), 2)}")
print(f"第二个圆的面积为: {round(area(r2), 2)}")
print(f"第三个圆的面积为: {round(area(r3), 2)}")


# 求1到指定数之内的所有偶数和
def even_sum(number):
    """
    计算1到指定数number的所有偶数和
    :param number: 指定数
    :return: sum和
    """

    Sum = 0

    for i in range(1, number):
        # 判断是否是偶数
        if i % 2 == 0:
            Sum += i
    return Sum


# 函数调用
your_number = eval(input("请输入你要输入的数字: "))
sum_value = even_sum(your_number)
print(f"1到{your_number}之间的偶数值为: {sum_value}")
