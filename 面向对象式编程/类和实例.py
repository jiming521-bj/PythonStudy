# -*- coding: utf-8 -*-
# @Time     : 2023/7/21 14:25
# @Author   : JiMing
# @File     : 类和实例.py
# @SoftWare : PyCharm

from student import Student

"""
面向对象最重要的概念就是类（Class）和实例（Instance），必须牢记类是抽象的模板，
比如Student类，而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，
但各自的数据可能不同。
"""
if __name__ == '__main__':
    bart = Student('bart Simpson', 100)
    bart.print_score()

    test_bart = Student()
    print(test_bart)   # test_bart就是Student类的一个对象
    print(Student)     # Student就是本质上就是一个类（模板提供者)

    # 给类中的动态的绑定实例属性
    bart.hobby = 'basketball'
    if bart.hobby is not 'basketball':
        print('yes')
    else:
        print('no')

    # 获取学生成绩的等级
    lisa = Student('lisa Simpson', 99)
    lisa_score_grade = lisa.get_grade()
    lisa.hobby = 'football'
    print(bart.hobby)
    print(lisa.hobby)
    print(lisa_score_grade)


# 小结
"""
类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；

方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；

通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。
"""