# -*- coding: utf-8 -*-
# @Time     : 2023/10/11 11:45
# @Author   : JiMing
# @File     : fileOpenClose.py
# @SoftWare : PyCharm

# python中的文件操作
# 打开和关闭 创建一个文件
# open('文件路径', '文件模式') r 可写  w 可读
# 打开
f = open('jiming.txt', 'w', encoding='gbk')
# 写入内容
f.write('歌唱的名字')
# 关闭文件
f.close()

# 读取文件
f = open('jiming.txt', 'r')
# 默认情况下 read()方法一个字节一个字节的读取，效率比较低
# readline()方法可以读取多个字节，但是只能读取一行
# readlines()方法可以读取多个字节，并且读取多行，但是数据是以数组的形式返回
print(f.read())
f.close()
