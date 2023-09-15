# -*- coding: utf-8 -*-
# @Time     : 2023/8/15 20:12
# @Author   : JiMing
# @File     : netScript.py
# @SoftWare : PyCharm
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import URLError


def get_html(url):
    """
    爬取数据
    :param url:
    :return:
    """
    try:
        html = urlopen(url, timeout=5000)
    except URLError as e:
        print(e)
    else:
        return html


def parser_html(url):
    """
    处理数据
    :return:
    """
    data_html = get_html(url)
    try:
        bs = BeautifulSoup(data_html.read(), 'html.parser')
    except BaseException:
        return
    else:
        return bs


if __name__ == '__main__':
    url = 'https://www.ghxi.com/ghapi?type=query&n=new'
    data = parser_html(url)
    print(data.decode('utf-8'))
