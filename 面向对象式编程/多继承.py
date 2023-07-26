# -*- coding: utf-8 -*-
# @Time     : 2023/7/22 16:34
# @Author   : JiMing
# @File     : 多继承.py
# @SoftWare : PyCharm

class Animal(object):
    pass


class Runnable(object):
    def run(self):
        print("Running.....")


class Flyable(object):
    def fly(self):
        print("Flying.....")


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
