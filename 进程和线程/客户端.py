# -*- coding: utf-8 -*-
# @Time     : 2023/11/2 19:57
# @Author   : JiMing
# @File     : 客户端.py
# @SoftWare : PyCharm

from multiprocessing.managers import BaseManager


if __name__ == '__main__':
    # 客户端发送数据
    # 注册
    BaseManager.register('request_queue')
    BaseManager.register('response_queue')

    # 建立客户端
    client = BaseManager(address=('127.0.0.1', 5000), authkey=b'ming')
    # 连接服务端
    client.connect()
    print('连接服务器成功')

    task_request = client.request_queue()
    task_response = client.response_queue()
    while True:
        question = input('欢迎使用吉明AI智能工具，请提问: ')
        task_request.put(question)
        # 用户输入exit 选择性退出进程
        if question == 'exit' or question == 'EXIT':
            print('欢迎下次使用吉明AI工具')
            break
        print(f'AI回复: {task_response.get()}')
