# -*- coding: utf-8 -*-
# @Time     : 2023/7/21 20:41
# @Author   : JiMing
# @File     : 获取对象信息.py
# @SoftWare : PyCharm
from animal import Animal
import types  # 使用types模块判断一个对象是否是函数


class Dog(Animal):
    pass


class Husky(Dog):
    pass


# 使用type()
# 基本类型都可以使用type()函数获取对象信息
number = 10
print(type(number))

message = "This is a beautiful world"
print(type(message))

print(type(1212))
print(type('str'))
print(type(None))

# 如果一个变量指向函数或者类，也可以用type()判断：
print(type(abs))
print(type(Animal()))

# type()函数的返回值 对应的Class类型
if type(1212) == type(12):
    print('yes')
else:
    print('no')

if type('str') == type('1212'):
    print('yes')
else:
    print('no')

if type('12') == int:
    print('yes')
else:
    print('no')


# 判断一个对象是否是函数可以使用types模块中定义的常量
def fn():
    pass


print(type(fn) == types.FunctionType)  # 判断类型是否是函数
print(type(abs) == types.BuiltinFunctionType)  # 判断类型是否是内置函数
print(type(lambda x, y: x + y) == types.LambdaType)  # 判断类型是否是lambda函数
print(type(x for x in range(10)) == types.GeneratorType)  # 判断类型是否是迭代器

print('----------------------')
# 使用isinstance()函数判断类型
a = Animal()
d = Dog()
h = Husky()

# 继承关系 Object --> Animal --> Dog --> Husky
# 判断关系
print(isinstance(h, Husky))  # True
print(isinstance(h, Dog))  # True
print(isinstance(h, Animal))  # True

print(isinstance(d, Husky))  # False
print(isinstance(d, Animal))  # True

# 派生类的类型可以归属于本身或者父类  但是父类的类型不属于任何派生类
print('-----------------------')
# 使用type()函数判断的基本类型也可以使用isinstance()函数判断
print(isinstance(1212, int))
print(isinstance('str', str))
print(isinstance([1, 2, 3, 3], list))
print(isinstance(b'a', bytes))

# 判断一个变量是否是某些类型中的一种
print(isinstance([1, 2, 3, 4, 5], (list, dict)))
print(isinstance({name: age for name, age in zip(['chen', 'ming', 'li'], [12, 34, 22])}, (list, tuple)))

names = ['chen', 'yang', 'wan', 'li', 'ming']
ages = [19, 20, 21, 22, 21]

students = {name: age for name, age in zip(names, ages)}
print(students)

# 使用dir()函数获取一个对象的所有属性和方法
print(dir('ABC'))
print(len('ABC'))
print('ABC'.__len__())


class TestObject(object):

    def __len__(self):
        return 100


# 配合getattr() setattr() hasattr() 可以直接操作一个对象的状态
class MyObject(object):

    def __init__(self):
        self.x = 8

    def power(self):
        return self.x * self.x


if __name__ == '__main__':
    testSimpson = TestObject()
    print(len(testSimpson))

    obj = MyObject()
    # 测试obj的属性
    if hasattr(obj, 'x'):  # obj对象有属性x吗
        print("该对象有属性x")
        print(obj.x)
    else:
        print("该对象没有属性x")

    if hasattr(obj, 'y'):
        print("该对象有属性y")
        print(obj.y)
    else:
        print("该对象没有属性y")

    # 给对象动态的设置属性 setattr()
    setattr(obj, 'y', 10)

    # 获取对象属性值
    value = getattr(obj, 'y')
    print(value)

    # 如果获取的对象中没有对应的实例属性 将会抛出异常 AttributeError
    try:
        value = getattr(obj, '1212', '该对象不存在该属性')
        print(value)
    except AttributeError:
        print("AttributeError!")

    # 获取对象的方法
    if hasattr(obj, 'power'):
        print("obj对象中有该power方法")
    else:
        print("obj对象中没有该power方法")

    myFunction = getattr(obj, 'power')  # 将power()方法指向给变量myFunction
    print(myFunction)
    print(myFunction())  # myFunction变量可以通过()调用该实例方法 效果和对象访问方法一致 obj.power()
    print(obj.power())
