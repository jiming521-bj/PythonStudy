# -*- coding: utf-8 -*-
# @Time     : 2023/10/26 19:35
# @Author   : JiMing
# @File     : shakedown_test.py
# @SoftWare : PyCharm

# 调试
"""
程序能一次写完并正常运行的概率很小，基本不超过1%。
总会有各种各样的bug需要修正。有的bug很简单，看看错误信息就知道，
有的bug很复杂，我们需要知道出错时，哪些变量的值是正确的，哪些变量的值是错误的，
因此，需要一整套调试程序的手段来修复bug。

"""
import logging

logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.WARNING)


# 使用print()将错误结果自己打印出来
def foo(s):
    try:
        n = int(s)
    except ValueError as e:
        logging.exception(e)
    else:
        # 使用print先打印传入的值
        print('>>> n = %d' % n)
        return 10 / n


def main():
    foo('q')


# 使用断言调试代码
def foo1(string):
    try:
        n = int(string)
    except ValueError as e:
        logging.exception(e)
    else:
        assert n != 0, 'n is zero!'  # 如果n为0 则断言失败 抛出AssertError异常
        return 10 / n


def main1():
    # 处理用户输入的数据是否会有异常
    try:
        value = foo1(input('Please enter any data: '))
    # 捕获断言异常
    except AssertionError as e:
        print(e)
    else:
        if value is None:
            pass
        else:
            print(value)


# 使用logging方式调试
def shakedown_logging():
    s = '0'
    n = int(s)
    # logging.info('n = %d' % n)
    logging.warning('n = %d' % n)
    print(10 / n)


"""
这就是logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，
当我们指定level=INFO时，logging.debug就不起作用了。
同理，指定level=WARNING后，debug和info就不起作用了。
这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。
"""


def test01():
    main()


def test02():
    main1()


def test03():
    shakedown_logging()


if __name__ == '__main__':
    # test01()
    # test02()
    test03()
