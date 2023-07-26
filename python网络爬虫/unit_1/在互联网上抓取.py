# -*- coding: utf-8 -*-
# @Time     : 2023/7/25 18:55
# @Author   : JiMing
# @File     : 在互联网上抓取.py
# @SoftWare : PyCharm
import bs4
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from urllib.parse import urlparse
import re
import datetime
import random


class HtmlRequest(object):
    """
    一次简单的网络爬取实例
    """

    def __init__(self, url):
        """
        初始化目标URL资源
        :param url:
        """
        self.url = url
        self.response = None
        self.bs = None

        # 获取随机种子 让每次访问的时间不一样
        random.seed(datetime.datetime.now())

        # 保存数据的集合
        self.allExternalLinks = set()
        self.allInternalLinks = set()

        # 退出循环的标志
        self.flag = 0

    def get_html(self):
        """
        打开URL资源
        :return:
        """
        try:
            response = urlopen(self.url, timeout=50000)
        except HTTPError as e:
            print(e)
            raise
        except URLError as e:
            print(e)
            raise
        else:
            self.response = response

    def parser_html(self):
        """
        处理HTML对象 使用bs4对其解析
        :return:
        """
        try:
            bs = BeautifulSoup(self.response, 'html.parser')
        except bs4.FeatureNotFound:
            print('parser object has error')
            raise
        else:
            self.bs = bs

    def getInternalLinks(self, includeUrl):
        """
        获取页面中的所以内链列表
        :param includeUrl:
        :return:
        """
        includeUrl = f'{urlparse(includeUrl)}.scheme' \
                     f'://{urlparse(includeUrl)}.netloc'
        internalLinks = []

        # 找出所有以'/'开头的链接
        for link in self.bs.find_all('a',
                                     href=re.compile(
                                         '^(/|.*' + includeUrl + ')')):
            if link not in internalLinks:
                if link.attrs['href'] is not None:
                    if link.attrs['href'] not in internalLinks:
                        try:
                            if link.attrs['href'].startswith('/'):
                                internalLinks.append(includeUrl +
                                                     link.attrs['href'])
                        except AttributeError as e:
                            print(e)
                        else:
                            internalLinks.append(link.attrs['href'])
        return internalLinks

    def getExternalLinks(self, excludeUrl):
        """
        获取所有的外链列表
        :param excludeUrl:
        :return:
        """
        externalLinks = []
        # 找出所有以https或者www开头且不包括当前URL的链接
        for link in \
                self.bs.find_all(
                    'a', href=re.compile(
                        '^(http|www)((?!' + excludeUrl + ').)*$')):
            if link not in externalLinks:
                if link.attrs['href'] is not None:
                    if link.attrs['href'] not in externalLinks:
                        externalLinks.append(link.attrs['href'])
        return externalLinks

    def getRandomExternalLinks(self, startingPage):
        """
        随机获取外链
        :return:
        """
        externalLinks = self.getExternalLinks(
            urlparse(startingPage).netloc)
        if len(externalLinks) == 0:
            print('No external links, looking around '
                  'the site for one')
            domain = f'{urlparse(startingPage).scheme},' \
                     f'{urlparse(startingPage).netloc}'
            internalLinks = self.getInternalLinks(domain)
            return self.getRandomExternalLinks(
                internalLinks[random.randint(
                    0, len(internalLinks) - 1)])
        else:
            return externalLinks[random.randint(
                0, len(externalLinks) - 1
            )]

    def followExternalOnly(self, startingSite):
        """
        获取指定外链
        :param startingSite:
        :return:
        """
        try:
            externalLink = self.getRandomExternalLinks(startingSite)
            print(f'Random external link is {externalLink}')
            self.followExternalOnly(externalLink)
        except RecursionError as e:
            print(e)

    def getAllExternalLinks(self, siteUrl):
        # domain = f'{urlparse(siteUrl).scheme},{urlparse(siteUrl).netloc}'
        internalLinks = self.getInternalLinks(siteUrl)
        externalLinks = self.getExternalLinks(siteUrl)

        for link in externalLinks:
            if link not in self.allExternalLinks:
                self.allExternalLinks.add(link)
                print(link)
        for link in internalLinks:
            if link not in self.allInternalLinks:
                self.allInternalLinks.add(link)
                print(link)

    def test(self):
        self.followExternalOnly(self.url)

    def test01(self):
        self.allInternalLinks.add(self.url)
        self.getAllExternalLinks(self.url)


if __name__ == '__main__':
    # 创建一个实例
    data = HtmlRequest('https://oreilly.com')

    # 获取HTML对象
    data.get_html()

    # 解析HTML对象
    data.parser_html()

    # 获取外链
    # data.test()

    # 记录外链
    data.test01()
