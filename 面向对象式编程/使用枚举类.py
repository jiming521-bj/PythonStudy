# -*- coding: utf-8 -*-
# @Time     : 2023/7/22 21:09
# @Author   : JiMing
# @File     : 使用枚举类.py
# @SoftWare : PyCharm

from enum import Enum, unique

Month = Enum(
    'Month',
    ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
     'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
)

# 枚举Month对象
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)  # value属性则是自动赋给成员的int常量，默认从1开始计数。


@unique  # @unique装饰器可以帮助我们检查保证没有重复值。
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


if __name__ == '__main__':
    day1 = Weekday.Mon
    print(day1)
    print(Weekday['Tue'])
    print(day1.value)
    print(Weekday['Tue'].value)

    if Weekday.Mon == Weekday['Tue']:
        print("yes")
    else:
        print("no")
    print(day1 == Weekday['Mon'])
    print(day1 == Weekday['Sat'])
    print(Weekday(2))

    for day, value in Weekday.__members__.items():
        print(day, "--->",  value)
