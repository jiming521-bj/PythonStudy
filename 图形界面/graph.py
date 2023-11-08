# -*- coding: utf-8 -*-
# @Time     : 2023/11/7 10:57
# @Author   : JiMing
# @File     : graph.py
# @SoftWare : PyCharm
from tkinter import *
import tkinter.messagebox as messagebox

"""
关于Tkinter
我们来梳理一下概念：
我们编写的Python代码会调用内置的Tkinter，Tkinter封装了访问Tk的接口；
Tk是一个图形库，支持多个操作系统，使用Tcl语言开发；
Tk会调用操作系统提供的本地GUI接口，完成最终的GUI。
所以，我们的代码只需要调用Tkinter提供的接口就可以了。
"""


class Application(Frame):
    """创建一个GUI程序"""

    # 应用初始化
    def __init__(self, master=None):
        # 使用父类的Frame初始值
        Frame.__init__(self, master)
        self.pack()
        self.nameInput = Entry(self)  # 清空文本框内容
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.helloLabel = Label(self, text='Hello, World!')
        self.alterButton = Button(self, text='Hello', command=self.show_hello)
        # 创建一个窗体组件
        self.createWidgets()

    def createWidgets(self):
        # 将Label 和 button组件包装到父容器Frame中
        self.helloLabel.pack()
        self.quitButton.pack()
        # 添加文本输入框
        self.nameInput.pack()  # 加入到父容器中
        self.alterButton.pack()

    def show_hello(self):
        # 显示输入框信息 如果为空显示World
        name = self.nameInput.get() or 'World'
        messagebox.showinfo('Message', 'Hello, %s' % name)

    """
    在GUI中，每个Button、Label、输入框等，都是一个Widget。Frame则是可以容纳其他Widget的Widget，
    所有的Widget组合起来就是一棵树。
    pack()方法把Widget加入到父容器中，并实现布局。pack()是最简单的布局，grid()可以实现更复杂的布局。
    在createWidgets()方法中，我们创建一个Label和一个Button，当Button被点击时，触发self.quit()使程序退出。
    """


# 第一个GUI程序
def test01():
    app = Application()
    # 设置窗口标题
    app.master.title('Hello World')
    # 主消息循环
    value = app.mainloop()
    if not value:
        print('程序运行完成')


if __name__ == '__main__':
    test01()
