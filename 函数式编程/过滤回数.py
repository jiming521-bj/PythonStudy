# -*- coding: utf-8 -*-
# @Time     : 2023/10/13 14:19
# @Author   : JiMing
# @File     : 过滤回数.py
# @SoftWare : PyCharm

# 使用filter过滤回数
# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909
def is_palindrome(n):
    """
    判断是不是回数
    :param n:
    :return:
    """
    return str(n) == str(n)[::-1]


# 测试:
output = filter(is_palindrome, range(1, 100))
for i, j in enumerate(output):
    # 控制回数之间的间距
    if j < 10:
        print(j, end='  ')
    else:
        print(j, end=' ')
    # 每5个回数为一行
    if (i + 1) % 5 == 0:
        print()

