# -*- coding: utf-8 -*-
# @Time     : 2022/12/24 11:13
# @Author   : JiMing
# @File     : 4.生成器.py
# @SoftWare : PyCharm
# 生成器
print("generator")

"""
通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，
那后面绝大多数元素占用的空间都白白浪费了。
所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，
称为生成器：generator。
"""
# 要创建一个generator，有很多种方法。
# 第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
# 列表解析（列表生成器)
number_list = [value for value in range(10)]
print(number_list)
print(type(number_list))

# 创建一个生成器
my_generator = (value for value in range(10))
print(my_generator)
print(type(my_generator))

# 获取生成器的第一个值
print(next(my_generator))

# 获取生成器的第二个值
print(next(my_generator))

# 获取所有生成器的值
for i in my_generator:
    print(i, end=' ')

print("\n--------------------")


# 斐波那契数列
def fib(number):
    """
    获取斐波那契数列
    :param number: 前number项的值
    :return:
    """
    n, a, b = 0, 0, 1

    while n < number:
        print(b, end=' ')
        a, b = b, a + b
        n += 1
    else:
        return None


# 第二种方式构造生成器
def generator_two(number):
    """
    构造生成器
    :param number: 生成器的终止值
    :return:
    """
    n, a, b = 0, 0, 1

    while n < number:
        yield b
        a, b = b, a + b
        n += 1
    else:
        return 'done'


def fib_range(range_number):
    """
    求斐波那契数列 range_number范围内的值
    :param range_number:
    :return:
    """
    a, b = 0, 1
    while b < range_number:
        print(b, end=' ')
        a, b = b, a + b


# 杨辉三角
def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[n] + L[n - 1] for n in range(1, len(L))] + [1]


def test():
    n = 0
    # 遍历生成器 使用for循环不能获取生成器的错误返回值
    for value in triangles():
        print(value)
        n += 1
        # n表示行数， 当打印了10行后 退出循环
        if n == 10:
            break


def multiplication():
    """乘法口诀表"""
    for row in range(1, 10):
        for col in range(1, row + 1):
            print(f'{col} * {row} = {col * row}', end=' ')
        print()


if __name__ == '__main__':
    # 普通方式求斐波那契数列  生成个数
    fib(6)
    print("\n------------------------")
    # 普通方式求斐波那契数列 生成范围
    fib_range(10)

    # # 第二种生成生成器的方法
    f = generator_two(6)
    while True:
        try:
            result = next(f)
            print(result)
        except StopIteration as e:  # e.value的值就是生成器错误时返回的结果
            print('Generator result value is %s' % e.value)
            break
    test()
"""
这里，最难理解的就是generator和函数的执行流程不一样。
函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
"""
