# -*- coding: utf-8 -*-
# @Time     : 2023/7/22 21:22
# @Author   : JiMing
# @File     : 使用元类.py
# @SoftWare : PyCharm

class Hello(object):
    def hello(self, name='World'):
        print('Hello', '%s' % name)


# 通过type()函数定义类
def fn(self, name='World'):
    print("Hello", "%s" % name)


# 元类metaclass  metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        attrs['mv'] = lambda self, value: self.remove(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass


if __name__ == '__main__':
    h = Hello()
    h.hello()
    print(type(Hello))  # type
    print(type(h))  # Hello

    HelloOne = type("HelloOne", (object,), dict(hello=fn))  # 创建Hello Class
    hOne = HelloOne()
    hOne.hello()
    print(type(HelloOne))
    print(type(hOne))

    L = MyList()
    L.add(1)
    print(L)
    L.mv(1)
    print(L)

    L1 = list()
    L1.append(20)
    print(L1)

    # 普通list没有add方法
    try:
        L2 = list()
        L2.add(10)
    except AttributeError:
        print('no attr add!')
"""
要创建一个class对象，type()函数依次传入3个参数：

class的名称；
继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。
"""
