# -*- coding: utf-8 -*-
# @Time     : 2022/12/13 20:15
# @Author   : JiMing
# @File     : 2.函数调用.py
# @SoftWare : PyCharm

# 调用内置的Python函数
# 求绝对值
number = -10
print(f"{number}的绝对值为{abs(number)}")


# 自定义绝对值函数
def my_abs(digit):
    """
    求一个数的绝对值
    :param digit: 数字
    :return: 绝对值
    """

    # 如果传入的数字大于0,那么绝对值就是本身
    # 否则就是相反数
    if digit > 0:
        return digit
    else:
        return -digit


def my_max(list_value):
    """
    判断列表中的最大值
    :param list_value: 列表
    :return: 列表中的最大值
    """

    max_value = list_value[0]
    for i in range(1, len(list_value)):
        if list_value[i] > max_value:
            max_value = list_value[i]
    else:
        print("执行完成")

    return max_value


# my_max()函数调用
list_number_max = my_max([1, 2, 43, 64, 2, 32, 65, 14, 144, 90])
print(f"list_number中的最大的值为: {list_number_max}")

# 函数调用
test_number = eval(input("请输入一个整数: "))
result = my_abs(test_number)

print(f"{test_number}的绝对值为{result}")

# max()函数和min()函数
list_numbers = list(range(10, 100))
print(f"max result is {max(list_numbers)}")
print(f"min result is {min(list_numbers)}")

# demo 使用内置函数hex()把一个整数转换成十六进制表示的字符串
n1 = 256
n2 = 1000
print(hex(n1))
print(hex(n2))
