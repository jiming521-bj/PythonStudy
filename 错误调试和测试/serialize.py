# -*- coding: utf-8 -*-
# @Time     : 2023/11/1 16:02
# @Author   : JiMing
# @File     : serialize.py
# @SoftWare : PyCharm
# 我们把变量从内存中变成可存储或传输的过程称之为序列化
# 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化

import pickle
import json


def test01():
    """所有变量都是在内存中的"""
    # pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
    d = dict(name='jiming', age=20, score=88)
    print(pickle.dumps(d))
    # print(pickle.loads(pickle.dumps(d)))


def test02():
    """将对象序列化后写入文件"""
    d = dict(name='ming', age=12, hobby='basketball')
    f = open('dump.txt', 'wb')
    pickle.dump(d, f)
    f.close()


def test03():
    """pickle反序列化"""
    global f
    try:
        f = open('dump.txt', 'rb')
    except FileNotFoundError as e:
        print(e)
    else:
        print(pickle.load(f))
    finally:
        f.close()
        print('读取内容成功')


"""
Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，
并且可能不同版本的Python彼此都不兼容，因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。
"""


def test04():
    """json模块序列化"""
    d = dict(name='ming', age=88, email='jiming581@gmail.com')
    serialize_d = json.dumps(d)
    print(serialize_d)
    print(type(serialize_d))
    try:
        json_file = open('json.txt', 'w')
    except FileNotFoundError as e:
        print(e)
    else:
        # json_file.write(serialize_d)
        json.dump(d, json_file)
    finally:
        print('End')


def test05():
    """json 反序列化"""
    try:
        file = open('json.txt', 'r')
    except FileNotFoundError as e:
        print(e)
    else:
        print(json.load(file))

    finally:
        print('读取内存成功')


class Student(object):
    """简单模拟学生类的尝试"""

    def __init__(self, name, age, gender, hobby, email):
        # 模板初始化
        self.name = name
        self.age = age
        self.gender = gender
        self.hobby = hobby
        self.email = email


class Person(object):
    """一次模拟人类的简单尝试"""

    def __init__(self, name):
        self.name = name

    def showPerson(self):
        print(self.name)


# 将对象实例转化成字典 序列化
def studentDict(std):
    return {
        'name': std.name,
        'age': std.age,
        'gender': std.gender,
        'hobby': std.hobby,
        'email': std.email,
    }


# 将字典拆分为对象实例参数 反序列化
def personDict(d):
    return Person(d['name'])


def test06():
    """JSON进阶"""
    # 将python中的字典直接转化成JSON数据格式 更多时候我们喜欢将class转化成JSON格式
    s = Student('jiming', 10, 'men', 'basketball', 'jiming581@gmail.com')
    # print(json.dumps(s))  # 错误的原因是Student对象不是一个可序列化为JSON的对象。
    # 可选参数default就是把任意一个对象变成可序列为JSON的对象
    print(json.dumps(s, default=studentDict))


def test07():
    """ 将所有对象的实例变成字典 JSON在根据字典类型作出序列化"""
    student = Student('ming', 20, 'men', 'tennis', 'wan29059@gmail.com')
    person = Person('chen')

    print(json.dumps(student, default=lambda obj: obj.__dict__))
    print(json.dumps(person, default=lambda obj: obj.__dict__))


def test08():
    """对象反序列化"""
    d = '{"name": "ming"}'
    print(d)
    print(json.loads(d, object_hook=personDict))


if __name__ == '__main__':
    # test01()
    # test02()
    # test03()
    # test04()
    # test05()
    # test06()
    # test07()
    test08()
    pass
