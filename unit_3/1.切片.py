# -*- coding: utf-8 -*-
# @Time     : 2022/12/22 12:18
# @Author   : JiMing
# @File     : 1.切片.py
# @SoftWare : PyCharm

# 切片
# 取一个list或tuple的部分元素是非常常见的操作。比如，一个list如下：
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 取前三个元素 方法一
print(L[0], L[1], L[2])

# 方法二
for i in range(3):
    print(f"{L[i]}", end=' ')
print()

# 使用循环增加的了代码量 使用切片就可以解决这样的问题 并且可以提高运行效率
print(L[:3])

# 索引位置从1开始，取两个元素
print(L[1: 3])

# 类似的，既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片
print(L[:-1])

print(L[-2:-1])

# number_list = []
#
# i = 1
# while i <= 5:
#     number_list.append(i)
#     i += 1
#
# print(number_list)
# print(list(range(1, 6)))
# print([i for i in range(1, 6)])

digit_list = [value for value in range(1, 100)]

# 获取前10个数字
print(digit_list[:10])
first_digit_list = digit_list[:10]

# 获取后10个数字
print(digit_list[-10:])
new_digit_list = digit_list[-10:]
new_digit_list.reverse()
print(new_digit_list)

result_list = []

for i in range(10):
    result_list.append(first_digit_list[i] + new_digit_list[i])
print(result_list)


result = [digit_list[i] + digit_list[-i-1] for i in range(10)]
print(result)

# 前11到20个数
print(digit_list[10:20])

# 所有数，每5个取一个     start: end: step  开始值 终止值 步长
print(digit_list[::5])

# 复制一个列表 浅拷贝
digit_list_new = digit_list[:]
print(digit_list_new[-10:])

# 这个不是复制，是将test_digit_list指向digit_list ，访问的内存空间内容是一样的，修改A会影响B
test_digit_list = digit_list
print(test_digit_list[-10:])


# 浅拷贝修改原有的值看产生的变化
digit_list[-1] = 1000
print(digit_list[-10:])
print(digit_list_new[-10:])
print(test_digit_list[-10:])

# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple
tuple_list = (1, 2, 3, 4, 5, 6, 7)
print(tuple_list)
print(type(tuple_list))

# 访问第一个元素
print(tuple_list[0])

# 访问最后一个元素
print(tuple_list[-1])

# tuple同样可以使用切片
print(tuple_list[::2])

# 字符串XXX也可以看成是一种list，每个元素就是一个字符。
# 因此，字符串也可以用切片操作，只是操作结果仍是字符串

string = 'She likes pizza, but I would like a sandwich'

# 访问字符串中的第一元素
print(string[0])

# 访问字符串中的最后一个元素
print(string[-1])

# 以步长为2的大小获取新的字符串
print(string[::2])
