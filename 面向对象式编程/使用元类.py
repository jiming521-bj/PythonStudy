# -*- coding: utf-8 -*-
# @Time     : 2023/7/22 21:22
# @Author   : JiMing
# @File     : 使用元类.py
# @SoftWare : PyCharm

class Hello(object):
    @classmethod
    def hello(cls, name='World'):
        print('Hello', '%s' % name)


# 通过type()函数定义类
def fn(self, name='Jiming'):
    print("Hello", "%s" % name)


def s_func(self, name='jiming', age=12):
    print(f"my name is {name}, I am {age} years old.")


# 元类metaclass  metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(mcs, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        attrs['mv'] = lambda self, value: self.remove(value)
        return type.__new__(mcs, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass


if __name__ == '__main__':
    # Create an instance
    h = Hello()
    # Call instance method
    h.hello()
    # Print class type
    print(type(Hello))  # type
    # Print instance type
    print(type(h))  # Hello

    # type类型既可以获取对象类型，又可以创建出新的类型
    HelloOne = type("HelloOne", (object,), dict(hello=fn))  # 创建HelloOne Class

    hOne = HelloOne()
    hOne.hello()
    print(type(HelloOne))
    print(type(hOne))

    # 创建Person类 使用type()方法
    Person = type('Person', (object,), dict(show_person=s_func))
    # 根据Person类创建一个实例
    person = Person()
    # 调用Person类通用方法
    person.show_person()

    # 使用元类创建的list类 add 和 mv都是动态创建出来的
    L = MyList()
    L.add(1)
    print(L)
    L.mv(1)
    print(L)

    # 内置的list类型
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

1、class的名称；
2、继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
3、class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
总结：
通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，
仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。
"""
