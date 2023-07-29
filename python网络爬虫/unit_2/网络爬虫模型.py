# -*- coding: utf-8 -*-
# @Time     : 2023/7/26 19:05
# @Author   : JiMing
# @File     : 网络爬虫模型.py
# @SoftWare : PyCharm

import requests
from bs4 import BeautifulSoup


class Content(object):
    """
    爬取网站相关信息
    """

    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body


def getPage(url):
    """
    获取页面框架
    :param url:
    :return:
    """
    req = requests.get(url)
    return BeautifulSoup(req, 'html.parser')


def scrapeNYTimes(url):
    bs = getPage(url)
    title = bs.find('h1').get_text()
    lines = bs.find_all('p', {'class': 'story-content'})
    body = '\n'.join([line.text for line in lines])
    return Content(url, title, body)


def scrapeBrookings(url):
    bs = getPage(url)
    title = bs.find('h1').get_text()
    body = bs.find('div', {'class': 'post-body'}).text
    return Content(url, title, body)


if __name__ == '__main__':
    url = 'https://www.brookings.edu/blog/future-develoment' \
          '/2018/01/26/delivering-inclusive-urban-access-3-' \
          'uncomfortable-truths/'

    content = scrapeBrookings(url)
    print(f'Title: {content.url}')
    print(f'URL: {content.url}')
    print(content.body)

    url = 'https://www.nytimes.com/2018/01/25/opinion/sunday/' \
          'silicon-valley-immortality.html'

    content1 = scrapeNYTimes(url)
    print(f'Title: {content1.title}')
    print(f'URL: {content1.url}')
    print(content1.body)
