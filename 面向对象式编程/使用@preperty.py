# -*- coding: utf-8 -*-
# @Time     : 2023/7/22 13:44
# @Author   : JiMing
# @File     : 使用@preperty.py
# @SoftWare : PyCharm
class Student(object):

    # def __init__(self):
    #     self._score = 0
    #
    # def get_score(self):
    #     return self._score
    #
    # def set_score(self, value):
    #     if not isinstance(value, int):
    #         raise ValueError('score must be an integer!')
    #     if value < 0 or value > 100:
    #         raise ValueError('score must between 0 ~ 100!')
    #     self._score = value

    def __init__(self):
        # 初始化实例属性
        self._score = 0
        self._birth = 0

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be in integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    @property
    def birthday(self):
        return self._birth

    @birthday.setter
    def birthday(self, value):
        self._birth = value

    @property
    def age(self):
        return 2023 - self._birth


class Screen(object):
    """
    一次模拟屏幕的简单尝试
    """

    def __init__(self):
        self._width = 0
        self._height = 0
        self._name = 'jiming'
        self.__salary = 10000

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height


if __name__ == '__main__':
    s = Student()

    # s.set_score(100)
    # print(s.get_score())
    #
    # s.set_score(11000)
    # print(s.get_score())
    s.score = 12
    print(s.score)

    student = Student()
    student.birthday = 2000
    print(f"他是{student.birthday}年出生的")
    print(f"他今年{student.age}岁了")

    s = Screen()
    s.width = 1024
    s.height = 7682

    # 返回授权限的属性值
    try:
        print(s._name)
        # print(s.__saraly)
        # print(s._Screen__salary)
    except AttributeError:
        print("this property is not exists!")
    print(s.resolution)

    try:
        assert s.resolution == 786432, 'check 1024 * 768 = %d ?' % s.resolution
    except AssertionError as e:
        print(e)
