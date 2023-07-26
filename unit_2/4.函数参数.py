# -*- coding: utf-8 -*-
# @Time     : 2022/12/19 11:14
# @Author   : JiMing
# @File     : 4.函数参数.py
# @SoftWare : PyCharm

# 1、默认参数
#   求一个数的2次方

def power(r):
    """
    求一个数的2次方
    :param r: 2次方
    :return: 一个数字的二次方的结果
    """
    i = 1
    while True:
        if i == 2:
            break
        else:
            r *= r
        i = i + 1
    return r


# 求一个数字的n次方
def power_n(number, n=1):
    """
    求一个数字的n次方
    :param number: 已知数
    :param n: 次方数
    :return: 返回已知数的n次方的结果
    """
    s = 1
    while n > 0:
        s *= number
        n -= 1
    else:
        return s


# 调用函数 一个数的平方
calc_result = power(8)
print(f"result = {calc_result}")

# 调用函数 一个数的n次方
calc_result_n = power_n(9, 3)
print(f"result = {calc_result_n}")

# 默认参数  这里的power_n函数指定了最后的默认参数，可以支持传入一个值的方式
try:
    calc_result_n = power_n(100)
    print(f"result = {calc_result_n}")
except TypeError as e:
    print(e)
"""
一是必选参数在前，默认参数在后，否则Python的解释器会报错
（思考一下为什么默认参数不能放在必选参数前面）；
默认参数放在必须参数前会出现二义性问题，编译器无法知道传递的值归属于那个参数下
二是如何设置默认参数。
    当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。
    变化小的参数就可以作为默认参数。
    使用默认参数有什么好处？最大的好处是能降低调用函数的难度。
"""


# 成绩录入系统

# 信息录入
def message_input():
    student_no = input("请输入学生的学号: ")
    student_name = input("请输入学生的姓名: ")
    student_score = input("请输入学生的成绩: ")

    student_city = input("请输入学生的所在城市: ")

    if student_city != '':
        return student_no, student_name, student_score, student_city
    else:
        return student_no, student_name, student_score


# 成绩录入
def score_input(sno, name, score, age=7, city='Guiyang'):
    """
    成绩输入函数
    :param sno: 学号
    :param name: 姓名
    :param score: 成绩
    :param age: 年龄
    :param city: 所在城市
    :return:
    """
    message = f"学号: {sno}, 姓名: {name}, 成绩: {score}, 年龄: {age}, 所在城市: {city}"
    with open("./score.txt", 'a') as f:
        f.writelines(message + '\n')
    print("信息录入成功!")


# 默认参数的注意事项演示
def and_end(list_number=None):  # 这里的默认参数是列表，是一个可表对象，使用时要格外注意
    """
    # 针对可变对象使用默认参数需要注意的情形  我们将可变对象的默认参数值设置为None，将其为不可变
    :param list_number: 空列表
    :return: 向列表L中的添加end元素
    """
    if list_number is None:
        list_number = []
    list_number.append('end')

    return list_number


# 可变参数的使用情形
"""
在Python函数中，还可以定义可变参数。顾名思义，
可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。
要定义出这个函数，我们必须确定输入的参数。由于参数个数不确定，
我们首先想到可以把a，b，c……作为一个list或tuple传进来，这样，函数可以定义如下
"""


# number改变为可变参数*number
def calc(*number):
    """
    求不定个数值的平方和
    :param number: list 或者 tuple 不定对象
    :return: 和
    """

    Sum = 0

    for i in number:
        Sum += i * i
    else:
        return Sum


# if __name__ == '__main__':
#     # 录入成绩函数调用
#     student_1 = message_input()
#     if len(student_1) == 3:
#         score_input(student_1[0], student_1[1], student_1[2])
#     else:
#         score_input(student_1[0], student_1[1], student_1[2], city=student_1[3])

# if __name__ == '__main__':
#     list_result = and_end([1, 2, 3, 4])
#     print(f"{list_result}")
#
#     i = 1
#     while i < 4:
#         print(f"{and_end()}")  # 可变对象会存储上一次的值，不会在调用时重置
#         i += 1

# if __name__ == '__main__':
#     # result = calc(list(range(1, 10)))
#     # print(f"result_n = {result}")
#     #
#     # if result == sum([1, 4, 9, 16, 25, 36, 49, 64, 81]):
#     #     print("Yes")
#     # else:
#     #     print("No")
#     #
#     # # 对于可变参数，传入的值需要为list或者tuple
#     # result_one = calc((1, 2, 3, 4, 5, 6, 7, 8, 9))
#     # print(f"result_n = {result}")
#
#     # 对于参数使用*number表示的时候，我们不用间接传入list或者tuple，可以直接对其就值
#     result_two = calc(1, 2, 3, 4, 5, 6, 7, 8, 9)
#     print(f"result_n = {result_two}")
#
#     # 可变参数传入0个的情况
#     result_two = calc()
#     print(f"result_n = {result_two}")
#
#     # 可变参数对于处理list的 情况
#     number_list = [i for i in range(1, 10)]
#     result_two = calc(number_list[0], number_list[1], number_list[2])
#     # 上面的表示过于繁琐，可以使用*指定传入的list
#     result_three = calc(*number_list)
#     print(f"result_n = {result_three}")

# 关键字参数
"""
可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
"""


def person(name, age, **kw):
    """
    关键字参数
    :param name: 姓名
    :param age: 年龄
    :param kw: 不定键值对的可变参数
    :return:

    """
    print(f"name: {name}, age: {age}, other: {kw}")


# 命名关键字参数
# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至
# 于到底传入了哪些，就需要在函数内部通过kw检查。
def person_copy(name, age, *, city='Beijing', hobby):  # 使用*限定关键字名称,*的位置只能在位置参数后
    """
    命名关键字参数
    :param hobby: 限定关键词参数
    :param city: 限定关键词参数
    :param name: 姓名
    :param age: 年龄
    :return:
    """
    # if 'city' in kw:
    #     # 有city关键词
    #     print("city pass")
    #     pass
    # if 'hobby' in kw:
    #     # 有hobby关键词
    #     print("hobby pass")
    #     pass
    print(f'name = {name}, age = {age}, city = {city}, hobby = {hobby}')


# 参数组合
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


if __name__ == '__main__':
    # 关键字参数调用
    person('ming', 21)
    # 传递不指定关键词参数
    display_dict = {'city': 'Guiyang', 'hobby': 'basketball'}
    person('Ji_ming', 22, city=display_dict['city'], hobby=display_dict['hobby'])

    # 上面的表述过于繁琐可以使用**kw来传递字典键值对
    person('Ming_ming', 22, **display_dict)
    # person中的关键字参数获得的只是display_dict的一份拷贝，修改其元素不会对display_dict产生影响

    # 限制关键字名称city 和 hobby
    person_copy('chen_ming', 20, city='Guiyang', hobby='Baseball')

    # 参数组合的演示
    f1(1, 2)
    f1(1, 2, 3, 4, 5)
    f1(1, 2, 3, *(4, 5, 6, 7, 8), **{'one': 1, 'two': 2, 'three': 3})
    f1(1, 2, 3, 'a', 'b')

    f1(1, 2, 3, 'a', 'b', x='100', y='1000')
    f2(1, 2, 3, d=99, ext=None)

    args_result = list(range(1, 4))
    kw_result = {'d': 100, 'one': 1, 'two': 2, 'three': 3, 'four': 4}
    f1(*args_result, **kw_result)
    f2(*args_result, **kw_result)
