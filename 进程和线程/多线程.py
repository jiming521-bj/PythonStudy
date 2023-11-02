# -*- coding: utf-8 -*-
# @Time     : 2023/11/2 10:16
# @Author   : JiMing
# @File     : 多线程.py
# @SoftWare : PyCharm
import threading
import multiprocessing
import time

# 多任务可以有多进程完成，也可以由一个进程内的多线程完成
# 一个进程至少有一个线程

"""
Python的标准库提供了两个模块：_thread和threading，
_thread是低级模块，threading是高级模块，对_thread进行了封装。
绝大多数情况下，我们只需要使用threading这个高级模块。
"""


# 新线程执行的代码
def loop():
    # 提示线程开始运行
    print('Thread %s is running.....' % threading.current_thread().name)
    # 初始线程个数值
    n = 0
    # 创建5个线程
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        # 每创建一个线程 休眠1秒
        time.sleep(1)
    # 所有线程创建后，结束进程
    print('thread %s ended.' % threading.current_thread().name)


# 初始化银行余额
balance = 0
# 创建一个线程锁
lock = threading.Lock()


def change_it(n):
    # 先存后取
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(1000000):
        # 先获取锁
        lock.acquire()
        try:
            # 放心修改
            change_it(n)
        finally:
            # 改完了释放锁 让下一个线程执行
            lock.release()


"""
锁的好处就是确保了某段关键代码只能由一个线程从头到尾完整地执行，
坏处当然也很多，首先是阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了。
其次，由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，
可能会造成死锁，导致多个线程全部挂起，既不能执行，也无法结束，只能靠操作系统强制终止。
"""


def test01():
    """多线程的简单测试"""
    # 任何一个进程创建后，都会有一个主线程 我们称之为主线程
    print('thread %s is running...' % threading.current_thread().name)
    t = threading.Thread(target=loop, name='LoopThread')
    # 开始执行线程
    t.start()
    # 等待线程全部执行完成
    t.join()
    # 结束主线程提示
    print('thread %s ended.' % threading.current_thread().name)


"""
由于任何进程默认就会启动一个线程，我们把该线程称为主线程，
主线程又可以启动新的线程，Python的threading模块有个current_thread()函数，
它永远返回当前线程的实例。主线程实例的名字叫MainThread，子线程的名字在创建时指定，
我们用LoopThread命名子线程。名字仅仅在打印时用来显示，完全没有其他意义，
如果不起名字Python就自动给线程命名为Thread-1，Thread-2……
"""


def test02():
    """线程间的数据访问"""
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)


"""
我们定义了一个共享变量balance，初始值为0，并且启动两个线程，先存后取，理论上结果应该为0，
但是，由于线程的调度是由操作系统决定的，当t1、t2交替执行时，只要循环次数足够多，balance的结果就不一定是0了
原因是因为高级语言的一条语句在CPU执行时是若干条语句，即使一个简单的计算：
balance = balance + n
上面的语句在CPU中执行的可能是这样的
先使用一个临时变量x存储 balance + n
再将x的值赋值给balance
所以就得出：
balance = balance + n
好比如
x = balance + n
balance = x


由于x是局部变量，两个线程各自都有自己的x，当代码正常执行时：
初始值 balance = 0
t1: x1 = balance + 5 # x1 = 0 + 5 = 5
t1: balance = x1     # balance = 5
t1: x1 = balance - 5 # x1 = 5 - 5 = 0
t1: balance = x1     # balance = 0
t2: x2 = balance + 8 # x2 = 0 + 8 = 8
t2: balance = x2     # balance = 8
t2: x2 = balance - 8 # x2 = 8 - 8 = 0
t2: balance = x2     # balance = 0
结果 balance = 0

但是t1和t2是交替运行的，如果操作系统以下面的顺序执行t1、t2：
初始值 balance = 0
t1: x1 = balance + 5  # x1 = 0 + 5 = 5
t2: x2 = balance + 8  # x2 = 0 + 8 = 8
t2: balance = x2      # balance = 8
t1: balance = x1      # balance = 5
t1: x1 = balance - 5  # x1 = 5 - 5 = 0
t1: balance = x1      # balance = 0
t2: x2 = balance - 8  # x2 = 0 - 8 = -8
t2: balance = x2   # balance = -8
结果 balance = -8


如果我们要确保balance计算正确，就要给change_it()上一把锁，当某个线程开始执行change_it()时，
我们说，该线程因为获得了锁，因此其他线程不能同时执行change_it()，只能等待，直到锁被释放后，获得该锁以后才能改。
由于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁，所以，不会造成修改的冲突。
创建一个锁就是通过threading.Lock()来实现：
"""


def test03():
    """测试多线程占用CPU核数"""

    def loop1():
        x = 0
        while True:
            x = x ^ 1

    for i in range(multiprocessing.cpu_count()):
        t = threading.Thread(target=loop1)
        t.start()


if __name__ == '__main__':
    # test01()
    test02()
    # test03()
