# -*- coding: utf-8 -*-
# @Time     : 2023/7/24 13:34
# @Author   : JiMing
# @File     : 美味的汤.py
# @SoftWare : PyCharm

from bs4 import BeautifulSoup
from urllib.request import urlopen

# 打开链接 获取资源
response = urlopen('https://www.pythonscraping.com/pages/page1.html')

# bs4解析数据
# bs = BeautifulSoup(response.read(), 'html.parser')  # 参数一：基于HTML的文本 参数二：解析器

# 获取html架构中h1标签
# print(bs.h1)

# 使用lxml解析器对HTML对象进行解析
# bs1 = BeautifulSoup(response.read(), 'lxml')
# print(bs1)

# 使用html5lib解析器
bs2 = BeautifulSoup(response.read(), 'html5lib')
print(bs2)

print(bs2.h1.text)




