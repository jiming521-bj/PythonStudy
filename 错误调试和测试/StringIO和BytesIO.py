# -*- coding: utf-8 -*-
# @Time     : 2023/10/28 15:09
# @Author   : JiMing
# @File     : StringIO和BytesIO.py
# @SoftWare : PyCharm

# 内存中读写文件
from io import StringIO, BytesIO


def test01():
    """将字符串写入到内存中"""
    f = StringIO()  # 创建一个写入对象 申请写入内存地址
    string_len = f.write('这是一场没有尽头的旅途')  # 将字符串写入到内存对象中 写入成功后会返回字符串的长度
    print(string_len)
    string_len = f.write('hello')
    print(string_len)

    # 获取写入内存对象的字符串 getvalue()方法用于获得写入后的str。
    print(f.getvalue())


def test02():
    """初始化StringIO 之后在像文件那样读取"""
    memory_content = StringIO('This\nis\nmy\nname!')
    while True:
        # 读取每一行数据
        s = memory_content.readline()
        if s == '':
            break  # 如果读取的数据为空 说明已经完成读取，退出循环
        print(s.strip())


# StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO
def test03():
    """读取二进制数据到内存中"""
    bytes_content = BytesIO()
    name = bytes_content.write('中文'.encode('utf-8'))
    # 获取写入到内存中的长度
    print(name)
    # 获取经过UTF-8编码写入的二进制数据
    print(bytes_content.getvalue())


def test04():
    """ 读取内存中保存的二进制数据"""
    read_byte = BytesIO('中文'.encode('utf-8'))
    # 将二进制文件解码为utf-8格式输出
    # print(read_byte.getvalue().decode('utf-8'))
    print(read_byte.read().decode('utf-8'))


def test05():
    """ read()方法读取二进制数据"""
    memory_byte_data = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
    print(memory_byte_data.read().decode('utf-8'))


if __name__ == '__main__':
    # test01()
    # test02()
    # test03()
    test04()
    # test05()
    pass
