# -*- coding: utf-8 -*-
# @Time     : 2023/11/2 13:06
# @Author   : JiMing
# @File     : task_worker.py
# @SoftWare : PyCharm
import time
import sys
import queue

from multiprocessing.managers import BaseManager


# 创建类似的QueueManager
class QueueManager(BaseManager):
    pass


# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名称
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接服务器，也就是运行task_master.py的机器
server_address = '127.0.0.1'
print('Connect to server %s...' % server_address)

# 端口和验证码注意保持与task_master.py设置的完全一直
m = QueueManager(address=(server_address, 5000), authkey=b'abc')
# 从网络中连接
m.connect()
# 获取Queue对象
task = m.get_task_queue()
result = m.get_result_queue()

# 从task队列取任务，并把结果写入到result队列中
for i in range(3):
    try:
        n = task.get(timeout=1)
        # print('run task %d * %d....' % (n, n))
        # r = '%d * %d = %d' % (n, n, n * n)
        print('run task %s' % n)
        if n == 'a':
            r = '我的名字叫吉明！'
        elif n == 'b':
            r = '我来自北京！'
        elif n == 'c':
            r = '我想去北极看冰川！'
        else:
            r = 'None'
        time.sleep(1)
        result.put(r)
    except queue.Empty:
        print('task queue is empty')

# 处理结果
print('worker exit...')
