# -*- coding: utf-8 -*-
# @Time     : 2023/10/27 11:24
# @Author   : JiMing
# @File     : FileReadingWriting.py
# @SoftWare : PyCharm
# 读写文件是最常见的IO操作。Python内置了读写文件的函数，用法和C是兼容的。
"""
读写文件前，我们先必须了解一下，在磁盘上读写文件的功能都是由操作系统提供的，
现代操作系统不允许普通的程序直接操作磁盘，
所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），
然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件），或者把数据写入这个文件对象（写文件）。
"""
# 打开文件 写入数据到文件中
file = open('test.txt', 'w')

# 写入一段话进文件
file.write('这是一场没有尽头的旅途\n你的名字')

# 关闭文件
file.close()

# 获取文件内容
try:
    f = open('test.txt', 'r')
except FileNotFoundError as e:
    print(e)
else:
    # read()方法可以读取文件中的所有内容
    # print(f.read())
    # 读取一行，可以传递参数limit 指定读取多个字符
    print(f.readline(2))
    # 关闭文件
    f.close()

"""
由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。
所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try … finally来实现：
"""

global test_f


def test01():
    """文件的读写的关闭操作"""
    global test_f
    try:
        test_f = open('test.txt', 'r')
    except FileNotFoundError as E:
        print(E)
    else:
        print(test_f.read())
    finally:
        if test_f:
            test_f.close()


def test02():
    """使用with对文件进行操作，自动关闭文件"""
    with open('test.txt', 'r', encoding='GBK') as FileObject:
        # print(FileObject.read())
        # 返回一行内容
        # print(FileObject.readline())
        # 返回所有行的内容 并以list方式存储
        content = FileObject.readlines()

    for col in content:
        print(col.strip())  # 去掉末尾的空格或者换行符


"""
调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，
所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。
另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。
因此，要根据需要决定怎么调用。
"""


# 读取二进制文件 jpg
def test03():
    """
    读取一张图片
    :return:
    """
    with open('一寸.jpg', 'rb') as BinaryFile:
        print(BinaryFile.read())


# 字符编码
def test04():
    """
    utf-8  gbk 字符编码格式
    :return:
    """
    encode_file = open('content.txt', 'w', encoding='utf-8')
    encode_file.write('这是一场没有尽头的青春')
    encode_file.close()

    with open('content.txt', 'r', encoding='utf-8') as E_File:
        print(E_File.read())
    print('The file was read successfully.')

    gbk_file = open('name.txt', 'w', encoding='gbk')
    gbk_file.write('想你的夜')
    gbk_file.close()

    # error的作用是 当读写文件遇到UnicodeDecodeError时直接忽略
    with open('name.txt', 'r', encoding='gbk', errors='ignore') as G_File:
        print(G_File.read())
    print('End...')


# 写文件
def test05():
    """
    一个简单写入文件的函数
    :return:
    """
    WriteFile = open('w_file.txt', 'w', encoding='utf-8')
    WriteFile.write('If we never meet, I hope you will be well forever!')
    WriteFile.close()
    print('The file was written successfully!')


if __name__ == '__main__':
    # test01()
    # test02()
    # test03()
    # test04()
    test05()
    pass
