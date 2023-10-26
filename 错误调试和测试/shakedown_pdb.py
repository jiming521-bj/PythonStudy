# -*- coding: utf-8 -*-
# @Time     : 2023/10/26 20:06
# @Author   : JiMing
# @File     : shakedown_pdb.py
# @SoftWare : PyCharm
import pdb

s = '0'
n = int(s)
# 在需要调试的代码前加入pdb.set_trace()就会自动执行到这暂停
pdb.set_trace()
print(10 / n)

"""
pdb调试代码的命令
l : 用于显示所有代码
n : 用于执行下一步
p variable name  : 用于查看当前变量名的值
q : 用于退出调试
"""