# -*- coding: utf-8 -*-
# @Time     : 2023/10/27 10:40
# @Author   : JiMing
# @File     : Document_testing.py
# @SoftWare : PyCharm

# 文档测试
import re
import doctest

m = re.search('(?<=abc)def', 'abcdef')
print(m.group(0))


# 将测试代码写入注释文档中，编译器会自动识别帮我们处理
def my_abs(n):
    # Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试
    """
    Function to get absolute value of number.
    Example:
    >>> abs(1)
    1
    >>> abs(-1)
    1
    >>> abs(0)
    0
    """
    return n if n >= 0 else (-n)


class Dict(dict):
    """
    Simple dict but also support access as x.y style.
    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    """

    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


# -*- coding: utf-8 -*-
def fact(n):
    """
    This is a document test for the fact function.
    >>> fact(2)
    2
    >>> fact(5)
    120
    >>> fact(1)
    1
    >>> fact(0)
    Traceback (most recent call last):
    ....
    ValueError: Minimum value cannot be less than or equal to 0.
    >>> fact('0')
    Traceback (most recent call last):
    ...
    TypeError: Parameter must be integer data.
    """

    if isinstance(n, str):
        raise TypeError('Parameter must be integer data.')
    if n < 1:
        raise ValueError('Minimum value cannot be less than or equal to 0.')
    if n == 1:
        return 1
    return n * fact(int(n) - 1)


if __name__ == '__main__':
    import doctest

    doctest.testmod()

if __name__ == '__main__':
    import doctest

    doctest.testmod()

if __name__ == '__main__':
    # 执行文档测试
    doctest.testmod()
