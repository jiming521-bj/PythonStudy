# -*- coding: utf-8 -*-
# @Time     : 2022/12/3 22:36
# @Author   : JiMing
# @File     : 使用list和tuple.py
# @SoftWare : PyCharm

# list
# Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
import random

classmates = ['ming', 'chen', 'wan', 'li', 'liu']
print(classmates)
print(len(classmates))

print(classmates[0])
print(classmates[-1])

for i in range(len(classmates)):
    print(classmates[i])

print("----------------")
cnt = 0
while True:
    # if classmates[cnt] != classmates[-1]:
    #     print(classmates[cnt])
    # else:
    #     print(classmates[-1])
    #     break

    print(classmates[cnt])
    if classmates[cnt] == classmates[-1]:
        break
    cnt = cnt + 1

classmates.append('ji')
print(classmates)
# print(classmates[len(classmates)])  # list index out of range

# 插入元素到指定的位置
classmates.insert(0, 'bu')
print(classmates)

classmates.insert(1, 'li')
print(classmates)

# 弹出list中的元素pop()
print(classmates.pop(1))
print(classmates)

# 删除已知元素
classmates.remove('ji')
print(classmates)

# 替换某个元素值
tempStr = ""
classmates.append('bu')
classmates.append('bu')
print(classmates)
for i in classmates:
    tempStr = tempStr + " " + i
# print(tempStr)
new_classmates = tempStr.strip().replace('bu', 'yue').split(' ')
print(new_classmates)

message = "This jacket is ten dollars"
print(message.split(' '))

# 修改指定元素值
new_classmates[1] = 'bu'
print(new_classmates)

# list元素可以是另一个list
s = ['python', 'C_plus_plus', new_classmates]
print(s)
s.append(10)
print(s)

# 空列表的创建
my_list = []
print(len(my_list))


# tuple 元组 该数据结构的特性是以,分隔 一旦初始化后就不可以修改
my_tuple = 'ming', 'ji', 'chen', 'li'
print(my_tuple)
print(type(my_tuple))
print(f"{len(my_tuple)}")

# 尝试修改元组中的元素
# my_tuple[0] = 'wan'  # 'tuple' object does not support item assignment
# print(my_tuple)

# 如果要修改只能重新定义这个元组并初始化新的元素内容
my_tuple = 'wan', 'ji', 'chen', 'li'
print(my_tuple)
print(type(my_tuple))
print(f"{len(my_tuple)}")

# 获取第一个元素和最后一个元素
print(my_tuple[0])
print(my_tuple[-1])

# 定义一个空的元组
your_tuple = ()
print(type(your_tuple))

# 要注意元组的标志符号是，而不是()
his_tuple = (1)
print(his_tuple)
print(type(his_tuple))

her_tuple = (1, 2, 3, 4)
print(her_tuple)
print(type(her_tuple))

# 可变的元组
t = ('a', 'b', 'c', ['x', 'y', 'z'])
print(t)
print(type(t))
print(f"{len(t)}")

t[3][0] = 'a'
print(t)

char_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
for i in range(3):
    t[3][i] = random.choice(char_list)
print(t)


# 请用索引取出下面list的指定元素
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple
print(L[0][0])

# 打印Python
print(L[1][1])

# 打印Lisa
print(L[2][2])

for i in range(3):
    print(f"{L[i][i]}", end=' ')
