# -*- coding: utf-8 -*-
# @Time     : 2023/11/2 19:53
# @Author   : JiMing
# @File     : 服务端.py
# @SoftWare : PyCharm

from multiprocessing.managers import BaseManager
import time
from multiprocessing import Queue

# 获取请求队列
request_queue = Queue()
# 获取响应队列
response_queue = Queue()


# 返回请求队列
def get_request_queue():
    global request_queue
    return request_queue


# 返回响应队列
def get_response_queue():
    global response_queue
    return response_queue


if __name__ == '__main__':
    # 注册通信队列至网络
    BaseManager.register('request_queue', callable=get_request_queue)
    BaseManager.register('response_queue', callable=get_response_queue)

    # 设置服务器响应地址和端口以及验证码
    server = BaseManager(address=('127.0.0.1', 5000), authkey=b'ming')

    # 启动网络服务
    server.start()
    print('服务器启动成功\n等待用户提问!')

    # 实例化网络通信队列
    server_request = server.request_queue()
    server_response = server.response_queue()

    # 标志
    i = 1
    while True:
        result = server_request.get()
        print(f"第{i}次用户提问内容: {result}")
        if result == 'exit' or result == 'EXIT':
            print('用户选择退出提问系统')
            break
        server_response.put(input('回复: '))
        i = i + 1
