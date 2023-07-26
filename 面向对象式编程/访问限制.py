# -*- coding: utf-8 -*-
# @Time     : 2023/7/21 14:47
# @Author   : JiMing
# @File     : 访问限制.py
# @SoftWare : PyCharm

from student import Student

if __name__ == '__main__':
    # 类中的访问限制
    try:
        bart = Student('bart Simpson', 88)
        lisa = Student('lisa Simpson', 99)
        print(bart.__name)    # # 'Student' object has no attribute '__name'
        print(lisa.__name)
    except AttributeError:
        print("'Student' object has no attribute '__name'")

    # 对于公共的实例变量，类外可以随意修改其内容
    # print('--------------------')
    # bart.name = 'ming'
    # lisa.name = 'chen'
    # print(bart.name)
    # print(lisa.name)

    # 通过类中提供的get访问获取私有实例属性
    bart1 = Student('bart Simpson', 82)
    print(f"name: {bart1.get_name()}")
    print(f"score: {bart1.get_score()}")
    print(f"grade: {bart1.get_grade()}")

    try:
        bart1.set_name('chen')
        bart1.set_score(459)
    except ValueError as e:
        print(e)

    print(f"name: {bart1.get_name()}")
    print(f"score: {bart1.get_score()}")

    # 通过使用类名和实例属性的方式访问类中的私有属性（强烈不建议)
    # print(bart1._Student__name)
