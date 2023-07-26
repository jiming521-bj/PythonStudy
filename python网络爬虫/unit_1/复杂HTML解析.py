# -*- coding: utf-8 -*-
# @Time     : 2023/7/24 16:39
# @Author   : JiMing
# @File     : 复杂HTML解析.py
# @SoftWare : PyCharm

# 想法大于实际
from bs4 import BeautifulSoup
from urllib.request import urlopen

# 目标网址
url = 'https://www.pythonscraping.com/pages/warandpeace.html'

# 打开链接
response = urlopen(url, timeout=4000)

# 解析数据 以HTML对象返回
bs = BeautifulSoup(response, 'html.parser')

# 打印HTML对象
# print(bs)

# 筛选出类属性为green的span标签
nameList = bs.find_all('span', {'class', 'green'})

# 打印所有结果
for name in nameList:
    print(name.get_text())   # 使用get_text()获取标签中的内容

# BeautifulSoup对象中的find_all()和find()函数
# find_all(tag, attributes, recursive, text, limit, keywords)
# find(tag, attributes, recursive, text, keywords)
"""
tag 标签列表
attributes CSS属性或者ID属性（字典形式）
recursive 迭代参数 默认为True 表示查找子标签和子标签的标签
text 匹配查找内容的（标签中的内容）
limit 表示从第几个开始
keyword 关键词查找 id 或者 class_


其他的BeautifulSoup对象
BeautifulSoup对象 bs
Tab对象（标签）
NavigableString对象（标签内容）
Comment对象（注释)
"""