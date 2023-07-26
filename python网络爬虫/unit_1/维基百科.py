# -*- coding: utf-8 -*-
# @Time     : 2023/7/25 14:11
# @Author   : JiMing
# @File     : 维基百科.py
# @SoftWare : PyCharm
import bs4
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
import re
import random
import datetime


def get_html(url):
    """
    获取维基百科中的词条内容
    :param url:
    :return:
    """
    # 检测url链接是否正确访问
    try:
        response = urlopen(url, timeout=5000)
    except HTTPError as e:
        print(e)
        raise
    except URLError as e:
        print(e)
        raise
    else:
        # 解析数据
        try:
            bs = BeautifulSoup(response, 'html.parser')
        except bs4.FeatureNotFound:
            return None
        return bs


def getLinks(articleUrl):
    """
    获取某个电影人词条
    :param articleUrl:
    :return:
    """
    try:
        html_re = urlopen(f'https://wikipedia.org{articleUrl}')
    except HTTPError as e:
        print(e)
    except URLError as e:
        print(e)
    else:
        try:
            bs = BeautifulSoup(html_re, 'html.parser')
        except bs4.FeatureNotFound:
            return None
        else:
            try:
                result = bs.find('div', {'id': 'bodyContent'}).find_all(
                    'a', href=re.compile('^(/wiki/)((?!:).)*$')
                )
            except AttributeError:
                return None

        return result


def test01():
    wiki_url = 'https://en.wikipedia.org/wiki/Kevin_Bacon'
    html = get_html(wiki_url)

    # print(html)
    # 查找获取资源的所有a标签
    # for link in html.find_all('a'):
    #     if 'href' in link.attrs:
    #         print(link.attrs['href'])

    # 获取维基百科上凯文-贝肯词条李所有指向其他词条的链接
    for link in html.find('div', {'id': 'bodyContent'}).find_all(
            'a', {'href': re.compile('^(/wiki/)((?!:).)*$')}
    ):
        if 'href' in link.attrs:
            print(link.attrs['href'])


def test02():
    """
    不断获取有关搜索电影人的姓名的词条
    :return:
    """
    random.seed(datetime.datetime.now())  # 获取当前系统时间戳

    links = getLinks('/wiki/Kevin_Bacon')  # 获取搜索的电影人

    pages = set()  # 防止重复抓取 筛选

    # 设置退出标志
    flag = 0
    while True:
        newArticle = links[random.randint(0, len(links) - 1)].attrs['href']
        if newArticle not in pages:
            pages.add(newArticle)
            print(newArticle)
            links = getLinks(newArticle)

        flag += 1
        if flag == 6:
            break


if __name__ == '__main__':
    # test01()
    test02()
