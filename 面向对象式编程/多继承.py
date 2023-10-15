# -*- coding: utf-8 -*-
# @Time     : 2023/7/22 16:34
# @Author   : JiMing
# @File     : 多继承.py
# @SoftWare : PyCharm

from types import MethodType


class Animal(object):
    pass


class Runnable(object):
    @classmethod
    def run(cls):
        print("Running.....")


class Flyable(object):
    @classmethod
    def fly(cls):
        print("Flying.....")


def print_run(Object):
    Object.run()


def set_name(self, name):
    self.name = name


# 大类:
class Mammal(Animal):
    pass


class Bird(Animal):
    pass


# 各种动物:
class Dog(Mammal, Runnable):  # 继承了Mammal和Runnable两个类 实现了哺乳类和奔跑功能
    pass


class Bat(Mammal):
    pass


class Parrot(Bird):
    pass


class Ostrich(Bird):
    pass


if __name__ == '__main__':
    dog = Dog()
    print_run(dog)

    dog.set_name = MethodType(set_name, dog)
    dog.set_name('jiming')
    if hasattr(dog, 'name'):
        print(dog.name)
    else:
        print('not')
