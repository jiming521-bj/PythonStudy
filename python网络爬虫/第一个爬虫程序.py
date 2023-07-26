# -*- coding: utf-8 -*-
# @Time     : 2023/7/23 11:30
# @Author   : JiMing
# @File     : 第一个爬虫程序.py
# @SoftWare : PyCharm

from urllib.request import urlopen

# 爬取数据目标地址 url
url = 'https://www.baidu.com'

# 使用urlopen库模拟浏览器打开网站 获取服务器资源
response = urlopen(url)

# 读取服务器响应的数据
# print(response.read().decode('utf-8'))

with open('index.html', mode='w') as files:
    files.writelines(response.read().decode('utf-8'))
print('下载成功')

# 关闭请求
response.close()