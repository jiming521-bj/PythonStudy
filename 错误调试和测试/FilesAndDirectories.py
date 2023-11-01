# -*- coding: utf-8 -*-
# @Time     : 2023/10/28 17:58
# @Author   : JiMing
# @File     : FilesAndDirectories.py
# @SoftWare : PyCharm

# 操作文件和目录
import os  # 操作文件和目录的模块


def test01():
    """
    获取系统操作类型
    :return:
    """
    print(os.name)  # nt表示是windows系统  posix是Linux Unix或者Max OS


# 环境变量
def test02():
    """获取操作系统当前定义的环境变量"""
    for val in os.environ:
        print(val)
    print()


# 操作文件和目录
def test03():
    """使用os模块操作系统中的文件和目录"""
    # 查看当前目录的绝对路径
    print(f"当前的操作目录为: {os.path.abspath('.')}")

    # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
    new_dir = os.path.join(os.path.abspath('.'), 'textDir')
    print(new_dir)

    # 创建一个目录
    try:
        os.mkdir(new_dir)
    except FileExistsError as e:
        print(e)
    else:
        print(f"{new_dir}目录创建成功!")

    # 删除一个目录
    os.rmdir(new_dir)


"""
把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，
后一部分总是最后级别的目录或文件名
"""


def test04():
    """拆分目录"""
    # 获取当前操作目录
    current_dir = os.path.abspath('.')
    print(current_dir)

    # 使用split拆分目录
    split_dir_list = current_dir.split('\\')
    print(split_dir_list)

    # 添加一个目录路径
    split_dir_list.append('ming')
    print(split_dir_list)
    print('\\'.join(split_dir_list))


def test05():
    """直接获取文件扩展名"""
    my_path = 'C:\\Administrator\\Desktop\\jiming.txt'
    print(os.path.splitext(my_path))


def test06():
    """文件重命名和删除文件"""
    try:
        os.rename('content.cpp', 'content.txt')
    except FileNotFoundError as e:
        print(e)
    else:
        print('重命名成功')
    finally:
        print('End')


def test07():
    """当前文件夹下所有目录"""
    print([x for x in os.listdir('.') if os.path.isdir(x)])

    # 列出当前文件夹下的所有.py文件
    [print(y) for y in os.listdir('.') if os.path.isfile(y) and os.path.splitext(y)[1] == '.py']


if __name__ == '__main__':
    # test01()
    # test02()
    # test03()
    # test04()
    # test05()
    # test06()
    test07()
    pass
