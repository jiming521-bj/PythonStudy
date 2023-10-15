# -*- coding: utf-8 -*-
# @Time     : 2023/10/15 15:39
# @Author   : JiMing
# @File     : 装饰器.py
# @SoftWare : PyCharm
from datetime import datetime
import functools

# 装饰器
"""
由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
"""


def now():
    print(datetime.now())


"""
现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，
但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
"""


def log(func):
    def wrapper(*args, **kw):
        print('call %s(): ' % func.__name__)
        return func(*args, **kw)

    return wrapper


def my_log(text):
    def decorator(func):
        @functools.wraps(func)  # 保持my_test函数地址不变 __name__指向不改变
        def wrapper(*args, **kwargs):
            print(f'{text}-{func.__name__}')
            return func(*args, **kwargs)

        return wrapper

    return decorator


# now = log('Hello World')(my_test) 执行效果
@my_log('Hello World')
def my_test(a, b):
    print(f"{a} * {b} = {a * b}")


"""
由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，
只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
"""


@log
def my_sum(a, b):
    print(f'{a} + {b} = {a + b}')


# 把@log放到now()函数的定义处，相当于执行了语句： my_sum = log(my_sum)


def myDecorator(text=None):
    def decorator(func):
        # 锁定被调装饰器的函数的地址__name__
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if text:
                print(f"{text}: {func.__name__}")
            else:
                print(f"{func.__name__}")
            return func(*args, **kwargs)

        return wrapper

    return decorator


@myDecorator()
def my_value(a, b):
    print(a, b)


if __name__ == '__main__':
    # 将函数名赋值给变量
    f = now
    # 打印函数名和变量名
    print(f)
    print(now)
    # 结果是now赋值给f 地址一样 此时f也指向now的那块内存空间
    # 调用now()函数 和它的引用f
    now()
    f()

    # 装饰器
    my_sum(10, 10)

    # 装饰器传参
    my_test(10, 10)

    print(my_test.__name__)  # wrapper 函数地址已经改变了

    my_value(10, 10)

"""
在面向对象（OOP）的设计模式中，decorator被称为装饰模式。OOP的装饰模式需要通过继承和组合来实现，
而Python除了能支持OOP的decorator外，直接从语法层次支持decorator。
Python的decorator可以用函数实现，也可以用类实现。
"""
