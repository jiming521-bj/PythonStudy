# -*- coding: utf-8 -*-
# @Time     : 2023/8/12 17:32
# @Author   : JiMing
# @File     : fun_test.py
# @SoftWare : PyCharm
def number_power(number, n=1):  # 该n中的1值为默认参数
    """
    求一个数的n次方值
    :param number:  预求值
    :param n: 次方数
    :return:  最终结果
    """
    # 定义存储结果的临时变量
    result = 1
    while True:
        """循环执行该数自乘"""
        result *= number
        n -= 1

        if n == 0:
            break
    return result


def add_end(L=[]):
    """
    定义参数为可变对象 list
    :param L:
    :return:
    """
    L.append('End')
    return L


if __name__ == '__main__':
    # 测试3的5次方结果
    print(f"3的5次方的结果为: {number_power(3, 5)}")

    # print(add_end([1, 2, 3, 4]))
    for i in range(3):
        print(add_end())

