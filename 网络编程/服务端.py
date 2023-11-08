# -*- coding: utf-8 -*-
# @Time     : 2023/11/7 12:47
# @Author   : JiMing
# @File     : 服务端.py
# @SoftWare : PyCharm

import socket
import threading
import time

# 创建一个基于IPV4的TCP协议Socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 如果使用UDP协议创建Socket 那么不需要使用listen
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 监听端口
s.bind(('127.0.0.1', 5000))

# 调用listen()方法开始监听端口
# s.listen(5)
# print('Waiting for connection......')


def tcpLink(sock, address):
    # 创建多线程和进程来处理
    print('Accept new connection from %s:%s....' % address)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % address)


# 通过永久循环来接收客户端的连接
while True:
    # 接受一个新连接
    # sock, address = s.accept()  # 使用IP协议创建的连接
    # 创建新线程来处理TCP连接
    # t = threading.Thread(target=tcpLink, args=(sock, address))
    # t.start()
    data, address = s.recvfrom(1024)
    print('Received from %s: %s.' % (data, address))
    s.sendto(b'Hello, %s!' % data, address)

    """
    recvfrom()方法返回数据和客户端的地址与端口，这样，服务器收到数据后，
    直接调用sendto()就可以把数据用UDP发给客户端。
    """