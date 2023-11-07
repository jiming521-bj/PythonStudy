# -*- coding: utf-8 -*-
# @Time     : 2023/11/7 9:56
# @Author   : JiMing
# @File     : my_urllib.py
# @SoftWare : PyCharm
from urllib import request

# urllib提供了一系列用于操作URL的功能。
"""
urllib的request模块可以非常方便地抓取URL内容，也就是发送一个GET请求到指定的页面，然后返回HTTP的响应：
"""


def test01():
    # 抓取网页内容
    with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
        data = f.read()
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', data.decode('utf-8'))


if __name__ == '__main__':
    test01()
