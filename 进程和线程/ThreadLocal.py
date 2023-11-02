# -*- coding: utf-8 -*-
# @Time     : 2023/11/2 11:04
# @Author   : JiMing
# @File     : ThreadLocal.py
# @SoftWare : PyCharm
import threading

# 创建一个全局的ThreadLocal对象
local_school = threading.local()


def process_student():
    # 获取当前线程关联的student
    std = local_school.student
    teach = local_school.teacher
    print(f"Hello, {teach}---{std} (in {threading.current_thread().name})")


def process_thread(name, tea):
    # 绑定ThreadLocal的student
    local_school.student = name
    local_school.teacher = tea
    process_student()


def test01():
    """开始线程之间的数据传递"""
    t1 = threading.Thread(target=process_thread, args=('Alice', 'ming',), name='Thread-A')
    t2 = threading.Thread(target=process_thread, args=('Bob', 'ji'), name='Thread-B')
    t1.start()
    t2.start()
    t1.join()
    t2.join()


"""
全局变量local_school就是一个ThreadLocal对象，每个Thread对它都可以读写student属性，但互不影响。
你可以把local_school看成全局变量，但每个属性如local_school.student都是线程的局部变量，
可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal内部会处理
"""

if __name__ == '__main__':
    test01()
