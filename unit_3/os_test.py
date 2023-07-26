# -*- coding: utf-8 -*-
# @Time     : 2022/12/23 19:54
# @Author   : JiMing
# @File     : os_test.py
# @SoftWare : PyCharm
import os

# 获取当前工作路径下的所有目录和文件
print(os.listdir('.'))

# 更改Python操作路径
os.chdir(r'C:\Users\Administrator\Desktop\test')
print(os.listdir('.'))

# 创建一个目录
try:
    os.mkdir('Ji_ming')
except FileExistsError as e:
    print(e)
finally:
    print(os.listdir('.'))

os.system('notepad.exe')
