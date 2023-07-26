# -*- coding: utf-8 -*-
# @Time     : 2023/7/24 13:50
# @Author   : JiMing
# @File     : 处理网络异常.py
# @SoftWare : PyCharm

from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

# 目标链接
url = 'https://www.pythonscraping.com/pages/page1.html'

try:
    # 访问链接（打开资源）
    response = urlopen(url, timeout=3000)
except HTTPError as e:    # 服务器响应错误
    print(e)
except URLError as e:    # 资源链接错误
    print(e)
else:
    # 解析服务器发送的HTML对象
    bs = BeautifulSoup(response, 'html.parser')

    # 打印解析的内容
    print(bs)

