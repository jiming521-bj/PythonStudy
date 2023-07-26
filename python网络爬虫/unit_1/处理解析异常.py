# -*- coding: utf-8 -*-
# @Time     : 2023/7/24 13:59
# @Author   : JiMing
# @File     : 处理解析异常.py
# @SoftWare : PyCharm
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError


# 获取标题函数
def getTitle(url):
    """
    获取url资源下的标题
    :param url: www.baidu.com...
    :return:
    """
    # 处理url链接
    try:
        response = urlopen(url, timeout=4000)
    except HTTPError as e:
        print(e)
    except URLError as e:
        print(e)
    else:
        # 解析服务器返回的对象（HTML）
        bs = BeautifulSoup(response, 'html.parser')
        # 异常处理解析后的对象是否含有h1标题
        try:
            title = bs.body.h1
        except:
            raise AttributeError('not found tag!')
        else:
            return title


if __name__ == '__main__':
    resourceUrl = 'https://www.pythonscraping.com/pages/page1.html'

    myTitle = getTitle(resourceUrl)
    if myTitle is None:
        print('Tags is not found!')
    else:
        print(myTitle.text)
