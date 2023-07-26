# -*- coding: utf-8 -*-
# @Time     : 2023/7/22 10:58
# @Author   : JiMing
# @File     : 使用__slots__.py
# @SoftWare : PyCharm
from types import MethodType


class Student(object):
    """
    一次模拟学生的简单实例
    """

    def __init__(self):
        self.hobby = ''

    # 显示Student类只能动态的绑定name 和 age实例属性
    __slots__ = ('name', 'age', 'address', 'score',
                 'set_address', 'set_score', 'set_age', 'hobby')  # 用tuple定义允许绑定的属性名称

    def set_hobby(self, hobby):
        """
        设置学生的爱好
        :return:
        """
        self.hobby = hobby  # slots会限制类中所有的实例属性和实例方法的创建


class GraduateStudent(Student):
    pass


def set_age(self, age):
    """
    设置年龄
    :param self: 指向自身
    :param age: 年龄
    :return:
    """
    self.age = age


def set_address(self, address):
    """
    设置学生的家庭住址
    :param self:
    :param address:  家庭住址
    :return:
    """
    self.address = address


def set_score(self, score):
    """
    设置学生的成绩
    :param self:
    :param score: 学生成绩
    :return:
    """
    self.score = score


if __name__ == '__main__':
    s = Student()
    s.name = 'chen'  # 动态给实例绑定一个属性
    print(s.name)

    # 动态的为实例绑定一个方法
    s.set_age = MethodType(set_age, s)
    s.set_address = MethodType(set_address, s)

    s.set_age(23)  # 调用实例方法
    s.set_address("贵州省天柱县远口镇坡脚村六组")

    if hasattr(s, 'age'):
        print(getattr(s, 'age'))
    else:
        pass
    if hasattr(s, 'address'):
        print(getattr(s, 'address'))
    else:
        pass

    # 给实例绑定的方法针对另一个实例不起作用
    s1 = Student()
    if hasattr(s1, 'address'):
        print('s1有实例属性address')
    else:
        print('s1没有实例属性address')  # 属性address只是绑定到s上 其他的实例无法访问

    # 通过绑定类方法 可以实现方法的共享
    Student.set_score = MethodType(set_score, Student)

    s2 = Student()
    if hasattr(s2, 'set_score'):
        s2.set_score(89)
        print(getattr(s2, 'score'))
    else:
        pass
    s3 = Student()
    print(getattr(s3, 'score')) if hasattr(s3, 'set_score') else print('no')

    s3.set_hobby('basketball')
    print(s3.hobby)

    # 为实例绑定动态数据（测试不在slots限定范围中的）
    try:
        s3.number = 100
        print(s3.number)
    except AttributeError:
        print("AttributeError!")

    # 绑定的类属性不被slots限制
    try:
        Student.digit = 1
        print(Student.digit)
    except AttributeError:
        print("AttributeError!")

    # slots定义的属性仅对当前实例起作用，对继承的子类是不起作用的
    g = GraduateStudent()
    g.ming = 'This is a beautiful world'
    print(g.ming)
