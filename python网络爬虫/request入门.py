# -*- coding: utf-8 -*-
# @Time     : 2023/7/23 11:40
# @Author   : JiMing
# @File     : request入门.py
# @SoftWare : PyCharm

import requests

# 利用用户的输入 模拟浏览器搜索
search_flag = input("请输入你要搜索的歌手: ")

# 资源地址
url = f'https://www.sogou.com/web?query={search_flag}'

# print(url)

# 模拟请求头 防止反爬机制
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 '
                  'Safari/537.36'
}
# 使用request模块获取数据
response = requests.get(url, headers=head)

# 获取服务器响应的数据
print(response.text)

# 关闭请求
response.close()