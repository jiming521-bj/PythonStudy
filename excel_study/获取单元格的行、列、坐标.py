# -*- coding: utf-8 -*-
# @Time     : 2022/12/4 14:59
# @Author   : JiMing
# @File     : 获取单元格的行、列、坐标.py
# @SoftWare : PyCharm
import os
import openpyxl

"""
.row 获取某个格子的行数；
.columns 获取某个格子的列数；
.coordinate 获取某个格子的坐标；
"""


# 获取表格对象
def LoadExcel():
    """
    获取一个工作表对象
    :return:
    """
    # 打开工作簿，返回一个工作簿对象
    try:
        book = openpyxl.load_workbook('英语四级考试居住信息排查表.xlsx')
    except FileNotFoundError as e:
        print(e)
    else:
        return book


# 设置路径
path = r'F:\PythonStudy\excel_study'

# 指定当前脚本执行操作路径 用于打开读取工作簿
os.chdir(path)

# 获取工作表对象
workbook = LoadExcel()

# 获取当前工作表 （活动表）
sheet_active = workbook.active

print(sheet_active)
