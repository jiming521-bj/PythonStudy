# -*- coding: utf-8 -*-
# @Time     : 2023/11/1 19:12
# @Author   : JiMing
# @File     : multiprocessing_my.py
# @SoftWare : PyCharm
from multiprocessing import Process, Pool, Queue, Pipe
import os
import time
import random
import subprocess


def run_proc(name):
    """子进程要执行的代码"""
    print('Run child process %s (%s)' % (name, os.getpid()))


def run_parent_proc():
    """创建一个进程"""
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    # 开始创建子进程
    p.start()
    # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    p.join()
    print('Child process end.')


def long_time_task(name):
    """运行子进程"""
    print('Run task %s (%s).' % (name, os.getpid()))
    # 记录第一个子进程的时间
    start = time.time()
    time.sleep(random.random() * 3)  # 随机休眠0到3秒
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


def random_process():
    """创建多个父进程"""
    print('Parent process %s.', os.getpid())
    p = Pool(5)  # 同时执行最多n个进程
    # 创建5个父进程
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))  # 同步执行
    print('Waiting for all subprocesses done')
    p.close()  # 关闭子进程后，就不能再创建子进程了
    p.join()  # 表示所有的子进程执行完成
    print('All subprocesses done.')


"""
对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，
调用close()之后就不能继续添加新的Process了
"""


def create_auto_subprocess():
    """快速创建一个子进程"""
    # print('$ nslookup www.baidu.com')
    # r = subprocess.call(['nslookup', 'www.baidu.com'])
    print(r'C:\Users\Administrator> echo jiming')
    r = subprocess.call(['echo', 'jiming'])
    print('Exit code: ', r)


def communicate_subprocess():
    """子进程输入额外数据"""
    print('$ nslookup')
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
    # output, err = p.communicate(b'echo jiming\nexit\n')
    print(output.decode('gb18030'))
    print('Exit code:', p.returncode)


def write(q, number):
    """写数据进程"""
    print('Process to write : %s' % os.getpid())
    content_list = [chr(i) for i in range(97, 123)]
    for value in random.sample(content_list, 4):
        print('Put %s to queue' % value)
        q.put(value)
        time.sleep(random.random())


def read(q, number):
    """读数据进程"""
    print('Process to read : %s' % os.getpid())
    # i = 1
    # while True:
    #     if i <= number:
    #         value = q.get(True)
    #         print('Get %s from queue.' % value)
    #     else:
    #         break
    #     i += 1

    while True:
        value = q.get(True)
        print('Get %s from queue' % value)


def manage_read_write():
    # 父进程创建Queue 并传给各个子进程
    q = Queue()
    # q = Pipe()
    number = 4
    pw = Process(target=write, args=(q, number))
    pr = Process(target=read, args=(q, number))
    # 启动子进程 写入：
    pr.start()
    # 启动子进程 读取:
    pw.start()
    # 等待pw结束
    pw.join()
    # pr进程是死循环 无法等待其结果，只能强行终止
    pr.terminate()


def test01():
    """父进程和子进程的创建"""
    run_parent_proc()


def test02():
    """启动大量的子进程"""
    random_process()


def test03():
    """subprocess启动一个子进程"""
    # create_auto_subprocess()
    communicate_subprocess()


def test04():
    """进程间的通信"""
    manage_read_write()


if __name__ == '__main__':
    # test01()
    # test02()
    # test03()
    test04()
    pass
