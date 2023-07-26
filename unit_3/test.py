# -*- coding: utf-8 -*-
# @Time     : 2023/1/5 20:13
# @Author   : JiMing
# @File     : test.py
# @SoftWare : PyCharm

def ahead_one():
    """
    将列表中的所有元素往前移动一个位置
    :return:
    """
    a = [5, 2, 4, 7, 6, 0, 10, 11, 12, 76]

    # 将列表中的第一个元素放在最后一个位置就可以逻辑实现每一个元素向前移动一个位置
    b = a.pop(0)
    a.append(b)

    return a


if __name__ == '__main__':
    result = ahead_one()
    print(result)
