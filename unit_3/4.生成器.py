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
    print(i, end='')

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
        print(b)
        a, b = b, a + b
        n += 1
    else:
        return 'done'


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


# 杨辉三角
def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[n] + L[n - 1] for n in range(1, len(L))] + [1]


def test():
    n = 0
    for value in triangles():
        print(value)
        n += 1

        if n == 10:
            break


if __name__ == '__main__':
    result = fib(6)
    print(result)

    # 第二种生成生成器的方法
    f = generator_two(6)
    while True:
        try:
            result = next(f)
            print(result)
        except StopIteration as e:
            print('Generator result value is %s' % e.value)
            break
    test()
