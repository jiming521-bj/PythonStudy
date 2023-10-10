# -*- coding: utf-8 -*-
# @Time     : 2023/10/11 13:29
# @Author   : JiMing
# @File     : 第一个爬虫程序.py
# @SoftWare : PyCharm

# 使用urllib爬虫
from urllib.request import urlopen
from bs4 import BeautifulSoup

r = urlopen('http://www.baidu.com')

bs = BeautifulSoup(r.read(), 'html.parser')
print(bs.find('a').get_text())


