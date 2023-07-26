# -*- coding: utf-8 -*-
# @Time     : 2023/7/24 20:03
# @Author   : JiMing
# @File     : 导航树.py
# @SoftWare : PyCharm
import urllib.error

from bs4 import BeautifulSoup
from urllib.request import urlopen


def getTitle(ResourceUrl):
    """
    获取网站h1标题
    :param ResourceUrl:
    :return:
    """
    try:
        response = urlopen(ResourceUrl, timeout=4000)
    except urllib.error.HTTPError as e:
        print(e)
    except urllib.error.URLError as e:
        print(e)
    else:
        bs = BeautifulSoup(response, 'html.parser')

        try:
            title = bs.body.h1
        except:
            raise AttributeError('not has attr')
        else:
            return title


def getHTML(R_ulr):
    """
    获取网络框架
    :param R_ulr:
    :return:
    """
    try:
        response = urlopen(R_ulr, timeout=5000)
    except urllib.error.HTTPError as e:
        print(e)
    except urllib.error.URLError as e:
        print(e)
    else:
        try:
            bs = BeautifulSoup(response, 'html.parser')
        except:
            raise AttributeError('not has tags!')
        else:
            return bs


if __name__ == '__main__':
    url = 'https://www.pythonscraping.com/pages/page3.html'
    # MyTitle = getTitle(url)
    #
    # if MyTitle is None:
    #     print('not found tag!')
    # else:
    #     print(MyTitle.get_text())

    # 找出子标签 可以使用children
    # children_url = getHTML(url)
    #
    # for child in children_url.find('table', {'id': 'giftList'}).children:
    #     print(child)

    # 找出后代标签可以使用descendants
    # descendants_url = getHTML(url)
    # for desc in descendants_url.find('table', {'id': 'giftList'}).descendants:
    #     print(desc)

    # 处理兄弟标签next_siblings()函数
    siblings_url = getHTML(url)
    # table = siblings_url.find('table', {'id': 'giftList'})

    # 获取table表格中标题的所有兄弟标签
    # for sibling in table.tr.next_siblings:
    #     print(sibling)

    # 获取table表格中的第一个标题标签
    # print(table.tr)

    # 获取table表格中最后一个tr标签
    # last_tr = siblings_url.find('table', {'id': 'giftList'}).find('tr', {'class': 'gift', 'id': 'gift5'})
    # print(last_tr)

    # 获取table表格最后一个标签的上一个标签

    # for previous in last_tr.previous_siblings:
    #     print(previous)

    # 处理父标签parent parents
    parent_url = getHTML(url)

    print(parent_url.find('img',
                          {'src': '../img/gifts/img1.jpg'}).parent.previous_sibling.get_text().replace('$', '').strip())
