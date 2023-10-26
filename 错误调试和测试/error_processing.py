# -*- coding: utf-8 -*-
# @Time     : 2023/10/26 10:52
# @Author   : JiMing
# @File     : error_processing.py
# @SoftWare : PyCharm

# 导入记入日志模块
import logging

# 错误处理
"""
在程序运行的过程中，如果发生了错误，可以事先约定返回一个错误代码，
这样，就可以知道是否有错，以及出错的原因。在操作系统提供的调用中，
返回错误码非常常见。比如打开文件的函数open()，成功时返回文件描述符（就是一个整数），出错时返回-1。
"""


def some_function(input_message):
    """这是一个简单的测试函数"""
    try:
        value = int(input_message)
    except ValueError:
        return -1
    else:
        return value


def foo():
    r = some_function('1212')
    if r == -1:
        return -1
    # 将该函数的结果方法给调用者
    return r


def bar():
    r = foo()
    if r == -1:
        print('error')
    else:
        print(r)
        print(type(r))


# 处理用户输入的数据
def process_data(val):
    """
    验证用户输入的数据
    :param val: 用户输入的数据
    :return:
    """
    try:
        result = int(val)
    except ValueError:
        return 0
    else:
        return result


def try_except():
    """
    使用try except机制处理错误
    :return:
    """
    try:
        print('try.....')
        # r = 10 / process_data(input("Please enter any data."))
        r = 10 / int(input('Please enter any data. '))
    except ValueError as e:
        print('except: ', e)
    except ZeroDivisionError as e:
        print('except: ', e)
    else:
        print('result: ', r)
    finally:  # 不管有没有错这条语句一定会被执行
        print('End....')


# 上面的函数测试 一旦某个函数错误，会一级一级的往上处理，直达可以处理这个错误为止
# 这样的效率不仅低，并且不容器查看具体错误的原始位置
# 函数模块化处理
def test01():
    bar()


# 使用try except finally机制处理错误
def test02():
    try_except()


"""
Python的错误其实也是class，所有的错误类型都继承自BaseException，
所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”
"""


def test03():
    """
    except 不仅会将该类型的错误捕获，并且还可以将其派生类的错误捕获
    :return:
    """
    try:
        r = 10 / int(input("Please Enter any data. "))
    except ValueError as e:
        print('except: ', e)
    # 只要ValueError被捕获到，这行代码永远不会别执行
    except UnicodeError as e:  # UnicodeError的父类就是ValueError
        print('sub except: ', e)
    except ZeroDivisionError as e:
        print('except: ', e)
    else:
        print(r)
    finally:
        print('end')


# 记录错误
def test04():
    """
    记录错误
    :return:
    """
    value = input("Please enter any data.")
    try:
        value = int(value) - 10
    except ValueError as e:
        logging.exception(e)
    else:
        print(value)
    print('错误会被记录，但是程序会继续执行!')


# 抛出错误
class MyTypeErrorRaise(TypeError):
    """自定义类型错误"""
    pass


def test05():
    """
    一个简单抛出错误的演示
    :return:
    """
    try:
        10 - '10'
    except TypeError:
        raise MyTypeErrorRaise('Integer and string operations are not supported.')
    finally:
        print('End....')

# 捕获错误，处理错误
def test06():
    """
    捕获异常
    :return:
    """
    try:
        test05()
    except MyTypeErrorRaise as e:
        print(e)
        raise  # 还可以将错误往上抛 交个顶层处理者来解决


if __name__ == '__main__':
    # test01()
    # test02()
    # test03()
    # test04()
    # 顶层处理错误
    try:
        test06()
    except MyTypeErrorRaise:
        print('ValueError!')

"""

BaseException
 ├── BaseExceptionGroup
 ├── GeneratorExit
 ├── KeyboardInterrupt
 ├── SystemExit
 └── Exception
      ├── ArithmeticError
      │    ├── FloatingPointError
      │    ├── OverflowError
      │    └── ZeroDivisionError
      ├── AssertionError
      ├── AttributeError
      ├── BufferError
      ├── EOFError
      ├── ExceptionGroup [BaseExceptionGroup]
      ├── ImportError
      │    └── ModuleNotFoundError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── MemoryError
      ├── NameError
      │    └── UnboundLocalError
      ├── OSError
      │    ├── BlockingIOError
      │    ├── ChildProcessError
      │    ├── ConnectionError
      │    │    ├── BrokenPipeError
      │    │    ├── ConnectionAbortedError
      │    │    ├── ConnectionRefusedError
      │    │    └── ConnectionResetError
      │    ├── FileExistsError
      │    ├── FileNotFoundError
      │    ├── InterruptedError
      │    ├── IsADirectoryError
      │    ├── NotADirectoryError
      │    ├── PermissionError
      │    ├── ProcessLookupError
      │    └── TimeoutError
      ├── ReferenceError
      ├── RuntimeError
      │    ├── NotImplementedError
      │    └── RecursionError
      ├── StopAsyncIteration
      ├── StopIteration
      ├── SyntaxError
      │    └── IndentationError
      │         └── TabError
      ├── SystemError
      ├── TypeError
      ├── ValueError
      │    └── UnicodeError
      │         ├── UnicodeDecodeError
      │         ├── UnicodeEncodeError
      │         └── UnicodeTranslateError
      └── Warning
           ├── BytesWarning
           ├── DeprecationWarning
           ├── EncodingWarning
           ├── FutureWarning
           ├── ImportWarning
           ├── PendingDeprecationWarning
           ├── ResourceWarning
           ├── RuntimeWarning
           ├── SyntaxWarning
           ├── UnicodeWarning
           └── UserWarning
"""
