# -*- coding: utf-8 -*-
# @Time     : 2023/10/10 19:11
# @Author   : JiMing
# @File     : 迭代器.py
# @SoftWare : PyCharm

# 迭代器的使用
"""
集合数据类型：list tuple dict set str
generator(迭代器）包括生成器和yield的generator function
"""
from collections.abc import Iterator, Iterable

# 判断[] list类型是否是Iterator类型
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((1, 2, 3), Iterable))
print(isinstance(100, Iterable))

"""
生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，
直到最后抛出StopIteration错误表示无法继续返回下一个值了。
"""
print(x for x in range(1, 10))  # <generator object <genexpr> at 0x000001E6A29476C8>
print(isinstance((x for x in range(1, 10)), Iterator))  # 本质上就是一个迭代器 惰性的

# 生成器都是Iterator对象，但是向list，dict，set虽然可以被迭代(Iterable)，但是不是Iterator
"""
这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，
直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，
只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。

Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。
已知数和未知数的区别

凡是可作用于for循环的对象都是Iterable类型；
凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
"""
for x in [1, 2, 3, 4]:
    pass

# 上面的代码等同于
# 首先获得Iterator对象
it = iter([1, 2, 3, 4])

# 循环遍历
while True:
    try:
        # 使用next()获取迭代器中的值
        print(next(it), end=' ')
    except StopIteration:
        # 遇到StopIteration就退出循环
        break

