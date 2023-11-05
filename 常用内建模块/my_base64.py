# -*- coding: utf-8 -*-
# @Time     : 2023/11/5 20:30
# @Author   : JiMing
# @File     : my_base64.py
# @SoftWare : PyCharm
import base64

# Base64是一种用64个字符来表示任意二进制数据的方法
"""
用记事本打开exe、jpg、pdf这些文件时，我们都会看到一大堆乱码，
因为二进制文件包含很多无法显示和打印的字符，所以，如果要让记事本这样的文本处理软件能处理二进制数据，
就需要一个二进制到字符串的转换方法。Base64是一种最常见的二进制编码方法。
['A', 'B', 'C', ... 'a', 'b', 'c', ... '0', '1', ... '+', '/']
"""


def test01():
    """Python内置的base64可以直接对base64的编解码"""
    # 编码
    encode_b = base64.b64encode(b'binary\x00string')
    print(encode_b)

    # 解码
    decode_b = base64.b64decode(encode_b)
    print(decode_b)

    """
    如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节怎么办？
    Base64用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候，会自动去掉。
    """


def test02():
    """ 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，
    所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_"""

    b_encode = base64.b64encode(b'i\xb7\x1b\xfb\xef\xff')
    print(b_encode)

    # 将++ // 编码成-- __
    b_url_encode = base64.urlsafe_b64encode(b'i\xb7\x1b\xfb\xef\xff')
    print(b_url_encode)
    print(len(b_url_encode))

    # 解码
    b_url_decode = base64.urlsafe_b64decode(b_url_encode)
    print(b_url_decode)
    """
    去掉=后怎么解码呢？因为Base64是把3个字节变为4个字节，所以，Base64编码的长度永远是4的倍数，
    因此，需要加上=把Base64字符串的长度变为4的倍数，就可以正常解码了。
    """


def safe_base64_decode(s):
    """sample"""
    # 处理=的base64解码函数
    # 对Base64编码的字符解码
    # 对长度进行判断 bs64是将3个字节转换成4个字节存储的数据类型
    b64_len = len(s)
    # 如果编码的字符能整除4 直接解码既可得到原始编码字符
    if b64_len % 4 == 0:
        b_decode = base64.b64decode(s)
    else:
        equal_number = b64_len % 4
        b_decode = base64.b64decode(s + b'=' * (4 - equal_number))
    return b_decode


def test03():
    """测试"""
    assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
    assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
    print('Pass')


if __name__ == '__main__':
    # test01()
    # test02()
    test03()
