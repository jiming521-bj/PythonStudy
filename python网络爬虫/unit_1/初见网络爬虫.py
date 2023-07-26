# -*- coding: utf-8 -*-
# @Time     : 2023/7/24 13:28
# @Author   : JiMing
# @File     : 初见网络爬虫.py
# @SoftWare : PyCharm
# 导入爬虫请求url库
from urllib.request import urlopen

# 模拟浏览器向服务端发出链接请求
html = urlopen('http://pythonscraping.com/pages/page1.html')

# 读取服务器响应的内容
print(html.read())
