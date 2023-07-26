# -*- coding: utf-8 -*-
# @Time     : 2023/7/25 16:40
# @Author   : JiMing
# @File     : 收集整个网站上的数据.py
# @SoftWare : PyCharm

# 获取爬虫网站 拟定抓取模式
import bs4
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
import re


def get_html(name):
    """
    获取网站整体框架
    :param name:
    :return:
    """
    # 处理网站链接是否连接成功
    url = f'https://en.wikipedia.org{name}'
    if name is None:
        return None
    else:
        try:
            response = urlopen(url, timeout=10000)
        except HTTPError as e:
            print(e)
            raise
        except URLError as e:
            print(e)
            raise
        else:
            return response


def parser_html(name):
    """
    解析HTML对象内容
    :return:
    """
    html = get_html(name)

    if html is None:
        pass
    else:
        # 使用bs解析HTML对象
        try:
            bs = BeautifulSoup(html, 'html.parser')
        except bs4.FeatureNotFound:
            return None
        else:
            return bs


def data_save(name):
    """
    对数据进行筛选
    :return:
    """
    data = parser_html(name)

    # 获取网站的标题以及相关内容
    pages = set()  # 用于存放数据
    try:
        print(data.h1.get_text())  # 获取网站标题
        print(data.find(id='mw-content-text').find_all('p')[0])
        # print(data.find(id='ca-edit').find('span').find('a').attrs['href'])
    except AttributeError as e:
        print(e)
        raise
    else:
        for link in data.find_all('a', href=re.compile('^(/wiki/)')):
            if link.attrs['href'] not in pages:
                # 将新页面的内容添加到set中
                NewPage = link.attrs['href']
                print('-' * 20)
                pages.add(NewPage)
                print(NewPage)
                get_html(NewPage)
                if len(pages) >= 6:
                    break


if __name__ == '__main__':
    movie_name = '/wiki/Kevin_Bacon'
    data_save(movie_name)
