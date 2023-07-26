# -*- coding: utf-8 -*-
# @Time     : 2023/7/22 16:39
# @Author   : JiMing
# @File     : 定制类.py
# @SoftWare : PyCharm

"""
看到类似slots这种形如xxx的变量或者函数名就要注意，这些在Python中是有特殊用途的。

slots我们已经知道怎么用了，len()方法我们也知道是为了能让class作用于len()函数。

除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。
"""
from typing import Dict
import random


class Student(object):
    """
    一次简单模拟学生的实例
    """

    def __init__(self, name):
        self.name = name
        self.hobby = ''

    @property
    def studentHobby(self):
        return self.hobby

    @studentHobby.setter
    def studentHobby(self, hobby):
        self.hobby = hobby

    def __str__(self):  # 定制类 将对象以指定字符串格式输出
        return 'Student object (name: %s)' % self.name

    def __len__(self):
        return len(self.name)

    def __call__(self, *args, **kwargs):
        print('My hobby is %s' % self.hobby)
        print(len(args))

        for i in args:
            print(i, end=' ')
        print()

        for key, value in kwargs.items():
            print(f"key: {key} ------- value: {value}")

    """
    call()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，
    所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。

    如果你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，
    因为类的实例都是运行期创建出来的，这么一来，我们就模糊了对象和函数的界限。
    """
    __repr__ = __str__  # 格式化repr格式


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本省就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration()  # 停止迭代
        return self.a  # 返回下一个值


class Fib1(object):
    def __getitem__(self, item):
        if isinstance(item, int):  # 判断item为索引
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b

            return a
        if isinstance(item, slice):  # 判断ite为切片
            start = item.start
            stop = item.stop
            step = item.step

            temp = start
            if start is None:
                start = 0
            if step is None:
                step = 1

            a, b = 1, 1
            L = []
            for x in range(stop):
                if step == 1:
                    if x >= abs(start):
                        L.append(a)
                else:
                    if x >= start and x % step == 1:
                        L.append(a)
                a, b = b, a + b

            if temp < 0:
                L.reverse()
                return L
            return L


class TestValue(Dict):

    def __setattr__(self, key, value):
        Dict[key] = value

    def __getitem__(self, item):
        return self.get(item, 'not found!')


class MyStudent(object):

    def __init__(self, name):
        self.name = name

    def __getattr__(self, item):
        if item == 'score':
            return lambda x: x + 90
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % item)


class Chain(object):

    def __init__(self, path=''):
        self.path = path

    def __getattr__(self, path):
        if path == 'users':
            return lambda paths: Chain('%s/%s' % (self.path, paths))
        return Chain('%s/%s' % (self.path, path))

    def __str__(self):
        return self.path

    __repr__ = __str__


if __name__ == '__main__':
    student = Student('chen')
    # print(student.name)
    print(student)
    print(len(student))
    print(student.__repr__())

    for n in Fib():
        print(n, end=' ')
    print()

    f = Fib1()
    print(f[2:8])
    print(f[1:8:2])

    test = TestValue({'a': 2})
    test['b'] = 10  # 设置字典内容
    test['c'] = 100
    print(test)
    print(test['c'])

    # 避免访问不存在的实例属性
    student1 = MyStudent("chen")
    print(student1.name)
    print(student1.score(10))

    # 动态链接
    chain = Chain('www.baidu.com')
    print(chain.files.name)

    # 姓名列表
    friend_names = ['chen', 'wan', 'liu', 'wu', 'ming', 'ji']
    # 获取随机姓名
    flag = 1
    while True:
        f_name = friend_names[random.randint(0, len(friend_names) - 1)]
        print(Chain('www.baidu.com').users(f_name).index.files.name)

        flag += 1

        if flag > 5:
            break

    # call()方法 实例不需要调用方法来访问实例属性可以通过内置call()方法获取
    myStudent = Student('ming')
    myStudent.studentHobby = 'basketball'
    myStudent([1, 2, 3, 4], {'a': 10, 'b': 11, 'c': 12}, a=10, b=20, c=20, d=40)

    # 判断一个变量是函数还是对象
    # 能被调用的对象就是一个Callable对象
    print(callable(Student('chen')))
    print(callable(max))
    print(callable([1, 2, 34, 3]))
    print(callable(None))
    print(callable('str'))
