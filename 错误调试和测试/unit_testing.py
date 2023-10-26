# -*- coding: utf-8 -*-
# @Time     : 2023/10/26 20:28
# @Author   : JiMing
# @File     : unit_testing.py
# @SoftWare : PyCharm
# 单元测试
# 导入单元测试模块
import unittest

"""
单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作。

比如对函数abs()，我们可以编写出以下几个测试用例：
输入正数，比如1、1.2、0.99，期待返回值与输入相同；
输入负数，比如-1、-1.2、-0.99，期待返回值与输入相反；
输入0，期待返回0；
输入非数值类型，比如None、[]、{}，期待抛出TypeError。

把上面的测试用例放到一个测试模块里，就是一个完整的单元测试。
"""


class Dict(dict):
    """
    自定义dict类型
    """

    def __init__(self, **kwargs):
        super(Dict, self).__init__(**kwargs)

    # 获取关键字
    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(f'"Dict" object has no attribute {item}')
        # return self[item]

    # 设置关键字
    def __setattr__(self, key, value):
        self[key] = value


# 单元测试
class TestDict(unittest.TestCase):
    """这是一个针对Dict的简单测试类"""

    def setUp(self) -> None:
        print('setUp.....')

    def tearDown(self) -> None:
        print('tearDown....')

    def test_init(self):
        """测试初始化值"""
        d = Dict(a=1, b=2)
        self.assertEqual(d.a, 1)  # 断言d.a的值是否是1
        self.assertEqual(d.b, 2)  # 断言d.b的值是否是2
        self.assertTrue(isinstance(d.a, int))
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        """测试关键字是否是存在"""
        d = Dict()
        d['key'] = 'value'  # 调用了dict的原生方法
        self.assertEqual(d.key, 'value')  # 测试含有getattr方法

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertEqual(d['key'], 'value')  # 使用dict原生方法获取key属性值 是否可以调用原生方法获取
        self.assertTrue('key' in d)  # 关键词key是否存在于字典中

    def test_key_error(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']
            print(value)

    def test_attr_error(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty
            print(value)


# 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行
"""
对每一类测试都需要编写一个test_xxx()方法。由于unittest.TestCase提供了很多内置的条件判断，
我们只需要调用这些方法就可以断言输出是否是我们所期望的。最常用的断言就是assertEqual():
self.assertEqual(abs(-1), 1) # 断言函数返回的结果与1相等

而通过d.empty访问不存在的key时，我们期待抛出AttributeError:
with self.assertRaises(AttributeError):
    value = d.empty
"""

# setUp和tearDown方法
"""
可以在单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。

setUp()和tearDown()方法有什么用呢？设想你的测试需要启动一个数据库，
这时，就可以在setUp()方法中连接数据库，在tearDown()方法中关闭数据库，
这样，不必在每个测试方法中重复相同的代码
"""


def test01():
    d = Dict(a=1, b=2)
    print(d['a'])
    try:
        value = d.a
    # except KeyError as e:
    #     print(e)
    except AttributeError as e:
        print(e)
    else:
        if value is None:
            print('不存在改键对应的值')
        else:
            print(value)


def test02():
    """运行测试代码"""
    unittest.main()


if __name__ == '__main__':
    # test01()
    test02()


# 总结
"""
单元测试可以有效地测试某个程序模块的行为，是未来重构代码的信心保证。
单元测试的测试用例要覆盖常用的输入组合、边界条件和异常。
单元测试代码要非常简单，如果测试代码太复杂，那么测试代码本身就可能有bug。
单元测试通过了并不意味着程序就没有bug了，但是不通过程序肯定有bug。
"""