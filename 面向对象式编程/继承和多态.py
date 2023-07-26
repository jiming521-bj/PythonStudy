# -*- coding: utf-8 -*-
# @Time     : 2023/7/21 20:23
# @Author   : JiMing
# @File     : 继承和多态.py
# @SoftWare : PyCharm

from animal import Animal

# 继承和多态
"""
在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，
新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）。

类：实现封装数据和方法的特定模板
对象：通过类具体实现出的实例
"""


class Dog(Animal):
    """继承Animal类 实现狗狗的简单实例"""

    def run(self):
        """重写父类方法 获取本类独特方法"""
        print('Dog is running....')


class Cat(Animal):
    """继承Animal类 实现猫猫的简单实例"""

    def run(self):
        """ 重写父类方法"""
    print('Cat is running....')


if __name__ == '__main__':
    # 实例出一个具体的小狗对象
    my_dog = Dog()
    my_dog.run()  # 通过继承 小狗实例拥有父类的方法

    my_cat = Cat()
    my_cat.run()  # 同理 小猫也是通过Animal继承的，可以直接使用父类的方法

    """
    当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，
    在代码运行的时候，总是会调用子类的run()。这样，我们就获得了继承的另一个好处：多态。
    """


# 总结
"""
继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，
也可以把父类不适合的方法覆盖重写。

动态语言的鸭子类型特定决定了继承不像静态语言那样是必须的
"""