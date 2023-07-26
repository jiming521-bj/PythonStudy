# -*- coding: utf-8 -*-
# @Time     : 2022/12/1 12:51
# @Author   : JiMing
# @File     : 3数据类型和变量.py
# @SoftWare : PyCharm

# 数据类型是什么？
# 计算机顾名思义就是可以做数学计算的机器，因此，计算机程序理所当然地可以处理各种数值。
# 但是，计算机能处理的远不止数值，还可以处理文本、图形、音频、视频、网页等各种各样的数据，
# 不同的数据，需要定义不同的数据类型。

# 整数int
print(10)
print(oct(10))  # 输出八进制的10
print(hex(10))  # 输出十六进制的10

# 浮点数float
print(10.3e2)
print(10.3e-2)

# 字符串 使用'' 和 "" 括起来的字符
print("I'm Ok")
print('I\'m Ok')
# 转义字符 \n \t
print("I love my parents\nAre you Ok!")
print("This restaurant is nice\t\tYes this good!")
# 文本标识符 '''
print('''
你的名字
我叫吉明
他叫明明
''')

# 布尔值 True False
print(10 in [10, 20, 30])
print(9 in [1, 2, 3, 4])
print(12 > 10)
print(10 < 9)

print(12 > 10 and 10 < 9)
print(12 > 10 or 10 < 9)
print(not 12 > 10)
print(not 10 < 9)

# 空值 None
number = None
print(number)
"""
空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，
而None是一个特殊的空值。
"""

"""
在Python中，等号=是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，
而且可以是不同类型的变量，
"""
test_variable = "This is string type variable"
print(test_variable)
test_variable = 100
print(test_variable)

# python 中的变量是动态的
message = "This is a number of variable"
print(message)
message = 10   # 将message变量指向整型数据
print(message)

# 常量：不能改变的量 但是在Python中一般没有这个值，常量也可以修改，因为本质上还是变量
PI = 3.1415926
print(PI)
print(2 * PI * 3)

# 求余数 %
result = 100 % 10
print(result)
result = 100 % 8
print(result)

# 求整除数
result = 100 // 8
print(result)   # 这个结果将会把小数部分舍去

"""
Python支持多种数据类型，在计算机内部，可以把任何数据都看成一个“对象”，
而变量就是在程序中用来指向这些数据对象的，对变量赋值就是把数据和变量给关联起来。
注意：python 对整数和浮点数没有数据范围一说，可以表示无限大inf
"""

