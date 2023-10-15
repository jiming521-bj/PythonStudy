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
        if isinstance(hobby, int):
            raise TypeError('Please pass in string...')
        self.hobby = hobby

    def __str__(self):  # 定制类 将对象以指定字符串格式输出
        return 'Student object (name: %s)' % self.name

    def __len__(self):
        return len(self.name)

    def __call__(self, *args, **kwargs):
        if self.hobby == '':
            return
        print('My hobby is %s' % self.hobby)
        print(f"The number of parameters you passed in is: {len(args)}")

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
            a, b = 0, 1
            for x in range(item):
                a, b = b, a + b

            return a
        if isinstance(item, slice):  # 判断ite为切片
            # 获取起始值
            start = item.start
            # 获取终止值
            stop = item.stop
            # 获取步长
            step = item.step

            # 判断起始值是否空，如果则默认起始值为0开始
            if start is None:
                start = 0
            # 判断是否传入步长，如果没有默认步长为1
            if step is None:
                step = 1
            # 临时保存起始值
            temp = start
            # 初始化斐波那契数列的起始值
            a, b = 1, 1
            # 存储切片结果的列表
            L = []
            # 遍历到终止值的所有斐波那契数列
            # 判断stop的值是否是负索引
            for x in range(stop):
                # 步长为1 不考虑步长的问题 直接从起始值（start）到终止值（stop）开始获取所有的斐波那数
                if step == 1:
                    # 保证从stop终止值遍历的数据值始终大于等于起始值（start）
                    if x >= abs(start):
                        L.append(a)
                # 考虑有传入步长情况 另外添加条件 x % step == 1
                else:
                    if start == 0:
                        # 对起始位置为0的处理方式
                        if x >= start and x % step == 0:
                            L.append(a)
                        pass
                    else:
                        if x >= start and x % step == 1:
                            L.append(a)
                a, b = b, a + b

            # 该段代码仅仅作为测试  后续考虑终止值为负数的情况
            if temp < 0:
                L.reverse()
                return L
            # 以列表的方式返回截取结果
            return L


class Fib2(object):
    """
    setitem方法
    """

    def __setitem__(self, key, value):
        myDict = {'name': 'jiming', key: value}
        return myDict


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
        if item == 'age':
            return lambda: 23
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


# 函数式编程
def test01():
    student = Student('chen')
    # print(student.name)
    print(student)
    print(len(student))
    print(student.__repr__())
    # 测试调用call函数
    student.studentHobby = 'basketball'
    try:
        student('test', **{'name': 'jiming'})
    except TypeError as e:
        print(e)


def test02():
    for n in Fib():
        print(n, end=' ')
    print()

    f = Fib1()
    print(f[10])
    print(f[2:8])
    print(f[1:8:2])
    print(f[:8:2])
    print(f[1:-1])


def test03():
    test = TestValue({'a': 2})
    test['b'] = 10  # 设置字典内容
    test['c'] = 100
    print(test)
    print(test['c'])


def test04():
    # 避免访问不存在的实例属性
    student1 = MyStudent("chen")
    print(student1.name)
    print(student1.age())
    print(student1.score(10))

    try:
        print(student1.hobby)
    except AttributeError as e:
        print(e)


def test05():
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


def test06():
    # call()方法 实例不需要调用方法来访问实例属性可以通过内置call()方法获取
    myStudent = Student('ming')
    try:
        # myStudent.studentHobby = 'basketball'
        myStudent.studentHobby = 'football'
    except TypeError as e:
        print(e)

    myStudent([1, 2, 3, 4], {'a': 10, 'b': 11, 'c': 12}, a=10, b=20, c=20, d=40)


def test07():
    # 判断一个变量是函数还是对象
    # 能被调用的对象就是一个Callable对象
    print(callable(Student('chen')))
    print(callable(max))
    print(callable([1, 2, 34, 3]))
    print(callable(None))
    print(callable('str'))


if __name__ == '__main__':
    # test01()
    # test02()
    # test03()
    # test04()
    # test05()
    # test06()
    test07()
