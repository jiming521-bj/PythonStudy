# -*- coding: utf-8 -*-
# @Time     : 2022/12/23 12:15
# @Author   : JiMing
# @File     : 2.迭代.py
# @SoftWare : PyCharm
from collections.abc import Iterable


def judge_iterable(obj):
    """
    检测不同对象是否可以迭代
    :param obj:  测试该对象是否支持迭代
    :return:
    """
    if isinstance(obj, Iterable):
        print('yes')
    else:
        print('no')


# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，
# 这种遍历我们称为迭代（Iteration）。
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# 输出字典
# print(d)

# 获取整个字典中的键和值
for key in d:
    print(f"key: {key}, value: {d[key]}")

# 获取字典中的键
for key in d:
    print(f"key = {key}")

for key in d.keys():
    print(f"key = {key}")

# 获取字典中的值
for value in d.values():
    print(f"value = {value}")

for value in d:
    print(f"value = {d[value]}")

# 使用items 获取字典中的键值对
for i, j in d.items():
    print(f"key = {i}\t value = {j}")

# 判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断
# 判断字符串对象是否可以迭代
judge_iterable('abc')

# 判断一个数字是否可以迭代
judge_iterable(1212)

# 判断一个list是否可以迭代
judge_iterable(list(range(1, 10)))

# 判断一个tuple是否可以被跌打
judge_iterable((1, 2, 3, 4, 5))

# 判断一个字典是否支持迭代
judge_iterable({'name': 'ming', 'age': 12})

# 判断bool类型的值是否可以迭代
judge_iterable(True)

# Python内置的enumerate函数可以把一个list变成索引-元素对，
# 这样就可以在for循环中同时迭代索引和元素本身
numbers_list = [value for value in range(1, 10)]
print(numbers_list)

for i, j in enumerate(numbers_list):
    print(f"index = {i}, value = {j}")

for i, j in ([1, 2], [2, 3], [3, 4], [4, 5]):
    print(f'x = {i}\ty = {j}')

first_ten_hundred = [value for value in range(1, 10)]
end_ten_hundred = [value for value in range(90, 100)]

print(first_ten_hundred, end_ten_hundred)
for first, end in zip(first_ten_hundred, reversed(end_ten_hundred)):
    print(f'first + end = {first + end}')
