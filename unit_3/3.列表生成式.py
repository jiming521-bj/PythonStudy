# -*- coding: utf-8 -*-
# @Time     : 2022/12/23 13:08
# @Author   : JiMing
# @File     : 3.列表生成式.py
# @SoftWare : PyCharm
import os

# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式
# list方法生成列表
number_list = list(range(1, 10))

# 使用list推导式生成列表
number_list_1 = [value for value in range(1, 10)]
print(number_list, number_list_1)

# 使用for循环生成列表
L = []
for i in range(1, 10):
    L.append(i)
print(L)


def sqrt_value(number, choose):
    """
    获取1到number个有序数字的平方值
    :param choose: 选择不同的方式获取平方值
    :param number: 有序数字的终止范围值
    :return: 值的列表
    """
    if choose == 1:
        sqrt_value_list = []
        for value in range(1, number + 1):
            sqrt_value_list.append(value * value)

        return sqrt_value_list
    if choose == 2:
        sqrt_value_list = [value * value for value in range(1, number + 1)]
        return sqrt_value_list
    else:
        return -1


# 还可以使用两层循环，可以生成全排列：
Full_arrangement = [m + n for m in 'ABC' for n in 'abc']
print(Full_arrangement)

# 列出文件和目录
dir_list = [d for d in os.listdir(r'C:\Users\Administrator\Desktop\临时处理')]
print(dir_list)

char_list = ['A', 'B', 'C', 'D', 'E']
digit_list = [1, 2, 3, 4, 5]

char_digit_pairing = [char + ' : ' + str(digit) for char, digit in zip(char_list, digit_list)]
print(char_digit_pairing)

# 将names列表中的所有名字的首字母大写
names = ['ming', 'wan', 'li', 'ge', 'chen', 'wu']
capitalize_names = [name.capitalize() for name in names]
print(capitalize_names)

# 请修改列表生成式，通过添加if语句保证列表生成式能正确地执行
L1 = ['Hello', 'World', 18, 'Apple', None]

# 方法一
L2 = [value.lower() for value in L1 if isinstance(value, str)]

# 期待输出: ['hello', 'world', 'apple']
print(L2)

# 方法二
L3 = []
for value in L1:
    if isinstance(value, str):
        L3.append(value.lower())
    else:
        pass
print(L3)

if __name__ == '__main__':
    # 平方值函数调用
    result = sqrt_value(10, 2)
    print(result)
