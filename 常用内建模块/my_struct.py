# -*- coding: utf-8 -*-
# @Time     : 2023/11/5 21:19
# @Author   : JiMing
# @File     : my_struct.py
# @SoftWare : PyCharm
import struct


# Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换。


def test01():
    """pack函数可以将任数据类型变成bytes"""
    value = struct.pack('>I', 10240099)
    print(value)
    """
    pack的第一个参数是处理指令，'&gt;I'的意思是：
    >;表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
    后面的参数个数要和处理指令一致。
    """
    # unpack把bytes变成相应的数据类型
    value = struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
    print(value)


def test02():
    """BMP位图处理"""
    s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00' \
        b'\x01\x00\x18\x00 '
    value = struct.unpack('<ccIIIIIIHH', s)
    print(value)


if __name__ == '__main__':
    # test01()
    test02()
