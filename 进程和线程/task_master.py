# -*- coding: utf-8 -*-
# @Time     : 2023/11/2 12:55
# @Author   : JiMing
# @File     : task_master.py
# @SoftWare : PyCharm

# 分布式进程
# 创建一个分布任务进程
# import random
# import time
# import queue
# from multiprocessing.managers import BaseManager
#
# # 发送任务的队列
# task_queue = queue.Queue()
# # 接受任务的队列
# result_queue = queue.Queue()
#
#
# # 从BaseManage继承的QueueManage
# class QueueManager(BaseManager):
#     pass
#
#
# # 把两个Queue都注册到网络上，callable参数关联了Queue对象
# QueueManager.register('get_task_queue', callable=lambda: task_queue)
# QueueManager.register('get_result_queue', callable=lambda: result_queue)
#
# # 绑定端口5000 设置验证码'abc'
# manager = QueueManager(address=('', 5000), authkey=b'abc')
# # 启动Queue
# manager.start()
# # 获得通过网络访问的Queue对象
# task = manager.get_task_queue()
# result = manager.get_result_queue()
#
# # 加入几个任务
# for i in range(10):
#     n = random.randint(0, 1000)
#     print('Put task %d.....' % n)
#     task.put(n)
# # 从result队列读取结果
# print('Try get result....')
# for i in range(10):
#     r = result.get(timeout=10)
#     print('Result: %s' % r)
#
# # 关闭
# manager.shutdown()
# print('master exit...')


# task_master.py
import random
import queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

# send queue 发送队列
task_queue = queue.Queue()
# receiver queue 接收队列
result_queue = queue.Queue()


class QueueManager(BaseManager):
    pass


# 注册2个queue到网络上 使用callable和匿名函数关联了Queue对象
'''仅适用Linux Windows下callable不能使用lambda表达式赋值
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
'''


def return_task_queue():
    global task_queue
    return task_queue


def return_result_queue():
    global result_queue
    return result_queue


def run_function():
    QueueManager.register('get_task_queue', callable=return_task_queue)
    QueueManager.register('get_result_queue', callable=return_result_queue)
    # 绑定端口5000，设置验证密码'abc'
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
    # Linux下address留空等于本机 Windows下不能留空 127.0.0.0即本机的地址
    # 启动Queue
    manager.start()
    # 通过网络获取Queue对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    questionDict = {
        'a': '你的名字叫什么?',
        'b': '你来自哪里?',
        'c': '你要到那里去？'
    }
    # 开启示例任务
    for i in range(3):
        # n = random.randint(0, 10000)
        n = [name for name in questionDict.keys()][i]
        print('Put task %s to run...' % i)
        print('Question: %s' % questionDict[n])
        task.put(n)

    # 读取任务结果
    print('Try to get results...')
    for i in range(3):
        r = result.get(timeout=10)
        print('Results: %s' % r)
    manager.shutdown()
    print('master has been shutdown')


if __name__ == '__main__':
    freeze_support()
    run_function()
