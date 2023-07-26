# -*- coding: utf-8 -*-
# @Time     : 2023/7/23 12:22
# @Author   : JiMing
# @File     : 豆瓣电影类型.py
# @SoftWare : PyCharm

import requests

# 获取请求链接
# https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=1
url = 'https://movie.douban.com/j/chart/top_list'

# 重新封装参数
param = {
    "type": "24",
    "interval_id": "100:90",
    "action": '',
    "start": 0,
    "limit": 20,
}

# 模拟浏览器发送请求 设置浏览器内核版本
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 "
                  "Safari/537.36 "
}

# 使用GET方式发送请求
response = requests.get(url, params=param, headers=head)

# 获取请求的链接url
request_url = response.request.url
print(request_url)

# 获取服务器响应的数据
for i in response.json():
    with open('movies.txt', mode='a+') as files:
        files.writelines(f"标题：{i['title']}---链接：{i['url']}---类型："
                         f"{i['types']}---产地：{i['regions']}\n")
    # for value in i['cover_url']:
    #     print(value, end='')
    # print()
print("保存成功")
# 关闭请求
response.close()

