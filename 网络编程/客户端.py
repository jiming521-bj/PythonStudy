# -*- coding: utf-8 -*-
# @Time     : 2023/11/7 12:55
# @Author   : JiMing
# @File     : 客户端.py
# @SoftWare : PyCharm

import socket

# 创建TCP连接 IPV4
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 创建基于UDP协议的TCP连接
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 建立连接
# s.connect(('127.0.0.1', 5000))

# 接收欢迎消息
# print(s.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据
    # s.send(data)
    # print(s.recv(1024).decode('utf-8'))

    # 当初在UDP协议时，发送数据和接收数据
    # 发送数据
    s.sendto(data, ('127.0.0.1', 5000))
    # 接收数据
    print(s.recv(1024).decode('utf-8'))

    """
    客户端使用UDP时，首先仍然创建基于UDP的Socket，然后，不需要调用connect()，直接通过sendto()给服务器发数据
    """

# s.send(b'exit')
s.close()

"""UDP的使用与TCP类似，但是不需要建立连接。此外，服务器绑定UDP端口和TCP端口互不冲突，
也就是说，UDP的9999端口与TCP的9999端口可以各自绑定"""