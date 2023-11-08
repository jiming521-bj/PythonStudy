# -*- coding: utf-8 -*-
# @Time     : 2023/11/7 12:27
# @Author   : JiMing
# @File     : TCP编程.py
# @SoftWare : PyCharm
import socket

# TCP 编程
"""
Socket是网络编程的一个抽象概念。通常我们用一个Socket表示“打开了一个网络链接”，
而打开一个Socket需要知道目标计算机的IP地址和端口号，再指定协议类型即可
"""
# 客服端
"""
大多数连接是可靠的TCP连接，创建TCP连接时，主动发起连接的叫客户端，被动响应
连接的叫服务端
"""


# 创建一个基于TCP连接的Socket
def test01():
    # 创建一个socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接 连接的参数是一个元组数据类型
    s.connect(('www.sina.com.cn', 80))
    """
    创建Socket时，AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6。
    SOCK_STREAM指定使用面向流的TCP协议，这样，一个Socket对象就创建成功，但是还没有建立连接。   
     
    客户端要主动发起TCP连接，必须知道服务器的IP地址和端口号。
    新浪网站的IP地址可以用域名www.sina.com.cn自动转换到IP地址，但是怎么知道新浪服务器的端口号呢？
    
    答案是作为服务器，提供什么样的服务，端口号就必须固定下来。由于我们想要访问网页，
    因此新浪提供网页服务的服务器必须把端口号固定在80端口，因为80端口是Web服务的标准端口。
    其他服务都有对应的标准端口号，例如SMTP服务是25端口，FTP服务是21端口，等等。
    端口号小于1024的是Internet标准服务的端口，端口号大于1024的，可以任意使用。
    """

    # 建立连接后，发送数据
    s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

    # 接收数据
    buffer = []
    while True:
        # 每次最多接收1k字节
        d = s.recv(1024)
        if d:
            buffer.append(d)
        else:
            break
    data = b''.join(buffer)

    """
    接收数据时，调用recv(max)方法，一次最多接收指定的字节数，因此，在一个while循环中反复接收，
    直到recv()返回空数据，表示接收完毕，退出循环
    """
    # 关闭连接
    s.close()

    # 返回新浪首页
    return data


def dispose_data(d):
    header, html = d.split(b'\r\n\r\n', 1)
    print(header.decode('utf-8'))

    # 把接收的数据写入文件中
    with open('sina.html', 'wb') as f:
        f.write(html)


if __name__ == '__main__':
    dispose_data(test01())
