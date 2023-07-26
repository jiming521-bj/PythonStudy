# -*- coding: utf-8 -*-
# @Time     : 2023/7/24 20:55
# @Author   : JiMing
# @File     : 正则表达式.py
# @SoftWare : PyCharm
# 如果有一个问题你打算用正则表达式解决，那么就是两个问题了

from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
import re


def getHtml(url):
    """
    获取url资源内容
    :param url:
    :return:
    """
    try:
        response = urlopen(url, timeout=5000)
    except HTTPError as e:
        print(e)
    except URLError as e:
        print(e)
    else:
        try:
            bs = BeautifulSoup(response, 'html.parser')
        except:
            raise AttributeError('not attr tag')
        else:
            return bs


if __name__ == '__main__':
    resource_url = 'https://www.pythonscraping.com/pages/page3.html'
    html = getHtml(resource_url)

    # print(html)

    # 查找网站中所有的img标签
    # images = html.find_all('img')
    # for i in images:
    #     print(i)

    # 查找匹配的img资源
    my_images = html.find_all('img', {'src': re.compile(r'../img/gifts/img.*.jpg')})

    for img in my_images:
        print(img)

    # 获取标签属性
    first_img = html.find('img', {'src': re.compile(r'../img/gifts.img[1].jpg')})
    print(first_img.attrs)
    print(first_img.attrs['src'])

    # Lambda表达式在BeautifulSoup中的应用
    # 查找有连个属性的所有标签
    # content = html.find_all(lambda tag: len(tag.attrs) == 2)
    # for tex in content:
    #     print(tex)

    # 查找Russian Nesting Dolls
    # search_string = html.find_all(lambda tag: tag.get_text() == 'Vegetable Basket')
    # for search_value in search_string:
    #     print(search_value)

    search_context = html.find('tr', {'id': 'gift1'}).next_siblings
    for i in search_context:
        print(i)

