# -*- coding: utf-8 -*-
# @Time     : 2023/7/21 14:13
# @Author   : JiMing
# @File     : student.py
# @SoftWare : PyCharm


# 使用函数实现（面向过程)
std1 = {'name': 'Michael', 'score': 100}
std2 = {'name': 'Bob', 'score': 88}


def print_score(std):
    """
    打印学生成绩
    :param std:
    :return:
    """
    print('%s: %s' % (std['name'], std['score']))


# 面向对象编程（OOP)
class Student(object):
    """
    模拟输出学生成绩的简单实例
    """
    # 类属性
    address = '天柱县远口镇'

    def __init__(self, name=None, score=None):
        """
        初始化函数(构造函数)
        :param name: 学生姓名
        :param score:  学生成绩
        """
        # self.name = name
        # self.score = score

        # 如果在实例变量中加上__下划线声明定义的 那么该实例变量在类外不可轻易访问
        self.__name = name
        self.__score = score

    # 提供get_name, 和 get_score函数方便用户获取类中的私有属性
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    # 提供set_name, 和 set_score函数 允许用户外部修改类中的私有属性
    def set_name(self, name=None):
        self.__name = name

    def set_score(self, score=None):
        # 检查传入的数据有效性
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def print_score(self):
        """
        打印学生姓名和成绩
        :return:
        """
        print('%s: %s' % (self.__name, self.__score))

    def get_grade(self):
        """
        根据学生的成绩判断等级
        :return:
        """
        if self.__score > 100:
            return 0
        elif self.__score >= 90:
            return 'A'
        elif self.__score >= 80:
            return 'B'
        elif self.__score >= 70:
            return 'C'
        elif self.__score >= 60:
            return 'E'
        else:
            return 0


if __name__ == '__main__':
    print_score(std1)
    print_score(std2)

    # 实例化Student类
    bart = Student('Bart Simpson', 89)
    lisa = Student('lisa Simpson', 88)

    bart.print_score()
    lisa.print_score()

# 总结：数据封装、继承和多态是面向对象的三大特点
