# -*- coding: utf-8 -*-
# @Time     : 2023/7/23 11:58
# @Author   : JiMing
# @File     : 百度翻译.py
# @SoftWare : PyCharm

import requests

# 请求内容
content = input("请输入你要翻译的内容: ")

# 构造数据发送给服务器
data = {
    'kw': content
}
# 请求链接
url = 'https://fanyi.baidu.com/sug'

# 封装模拟请求头
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 "
                  "Safari/537.36 "
}

# 通过post发送数据 必须要将发送的内容以字典的形式传递给 data
response = requests.post(url, data=data, headers=head)

# 将服务器响应的数据以JSON格式显示
print(response.json())

# 关闭请求
response.close()