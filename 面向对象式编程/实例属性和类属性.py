# -*- coding: utf-8 -*-
# @Time     : 2023/7/22 10:26
# @Author   : JiMing
# @File     : 实例属性和类属性.py
# @SoftWare : PyCharm
from student import Student

if __name__ == '__main__':
    student = Student('ming', 80)
    student.print_score()

    # 实例绑定属性 直接在实例上对其绑定既可
    student.hobby = 'basketball'
    print(student.hobby)

    # 类本身绑定属性，可以直接在class中定义属性，并且该属性是类属性 归属于class所有
    print(student.address)  # 使用对象访问类属性
    print(Student.address)  # 使用类访问类属性

"""
>>> class Student(object):
...     name = 'Student'
...
>>> s = Student() # 创建实例s
>>> print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
Student
>>> print(Student.name) # 打印类的name属性
Student
>>> s.name = 'Michael' # 给实例绑定name属性
>>> print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
Michael
>>> print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问
Student
>>> del s.name # 如果删除实例的name属性
>>> print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
Student
"""