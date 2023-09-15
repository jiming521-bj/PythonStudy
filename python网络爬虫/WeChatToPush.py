# -*- coding: utf-8 -*-
# @Time     : 2023/8/27 18:05
# @Author   : JiMing
# @File     : WeChatToPush.py
# @SoftWare : PyCharm
# import requests
#
#
# def send_wechat(msg):
#     token = 'd5c789ab93694d48a2f0c22298e62779'  # 前边复制到那个token
#     title = 'title1'
#     content = msg
#     template = 'html'
#     url = f"https://www.pushplus.plus/send?token={token}&title={title}&content='{content}'&template={template}"
#     print(url)
#     r = requests.get(url=url)
#     print(r.text)
#
#
# if __name__ == '__main__':
#     message = '这是一场没有尽头的旅途'
#     send_wechat(message)
# coding=utf8
import itchat
import re


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    if re.search('你好', msg['Text']):
        return '你好，我是自动回复机器人。'
    elif re.search('再见', msg['Text']):
        return '再见，祝你好运。'
    else:
        return '自动回复：我现在有事不在，稍后回复。'


itchat.auto_login(hotReload=True)
itchat.run()
