# -*- coding: utf-8 -*-
# @Time     : 2023/11/8 13:06
# @Author   : JiMing
# @File     : POP3收取邮件.py
# @SoftWare : PyCharm
import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

# QQ邮箱POP3授权码：zxetttfihhrachdh
"""
SMTP用于发送邮件，如果要收取邮件呢？
收取邮件就是编写一个MUA作为客户端，从MDA把邮件获取到用户的电脑或者手机上。
收取邮件最常用的协议是POP协议，目前版本号是3，俗称POP3。
Python内置一个poplib模块，实现了POP3协议，可以直接用来收邮件。

注意到POP3协议收取的不是一个已经可以阅读的邮件本身，而是邮件的原始文本，
这和SMTP协议很像，SMTP发送的也是经过编码后的一大段文本。
要把POP3收取的文本变成可以阅读的邮件，还需要用email模块提供的各种类来解析原始文本，变成可阅读的邮件对象
所以，收取邮件分两步：
第一步：用poplib把邮件的原始文本下载到本地；
第二部：用email解析原始文本，还原为邮件对象。
"""


def collect_email():
    """使用POP3收取邮件"""
    # 输入邮件地址，口令和POP3服务器地址
    email = 'jiming7890@qq.com'
    password = 'zxetttfihhrachdh'
    pop3_server = 'pop.qq.com'

    # 连接到POP3服务器
    server = poplib.POP3(pop3_server)
    # 可以打开或关闭调试信息
    server.set_debuglevel(1)  # 打开
    # 可选：打印POP3服务器的欢迎文字
    print(server.getwelcome().decode('utf-8'))

    # 身份认证
    server.user(email)
    server.pass_(password)

    # stat()返回邮件数量和占用空间
    print('Message: %s. Size: %s' % server.stat())

    # list()返回所有邮件的编号
    resp, mails, octets = server.list()

    # 可以查看返回的列表类似于[b'1 8899', n'2 8900',....]
    print(mails)

    # 获取最细一封邮件，注意索引号从1开始
    index = len(mails)
    resp, lines, octets = server.retr(index)

    # lines存储了邮件的原始本文信息的每一行数据
    # 可以获的整个邮件的原始文本
    msg_content = b'\r\n'.join(lines).decode('utf-8')
    # 稍后解析出邮件
    msg = Parser().parsestr(msg_content)
    # 可以根据邮件索引号直接从服务器删除邮件
    # server.dele(index)
    # 关闭连接
    server.quit()
    """
    用POP3获取邮件其实很简单，要获取所有邮件，只需要循环使用retr()把每一封邮件内容拿到即可。
    真正麻烦的是把邮件的原始内容解析为可以阅读的邮件对象。
    """

    return msg


def decode_str(s):
    """处理编码后的str 对其使用decode解码"""
    """
    decode_header()返回一个list，因为像Cc、Bcc这样的字段可能包含多个邮件地址，
    所以解析出来的会有多个元素。上面的代码我们偷了个懒，只取了第一个元素。
    """
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


def guess_charset(msg):
    # 文本邮件的内容也是str，还需要检测编码，否则，非UTF-8编码的邮件都无法正常显示
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset


def parser_email(message, indent=0):
    """解析邮件信息"""
    if indent == 0:
        # 解析发件者，取件者以及主标题信息
        for header in ['From', 'To', 'Subject']:
            # 通过get获取关键词对应的信息
            value = message.get(header, '')
            if value:
                # 如果是主题
                if header == 'Subject':
                    value = decode_str(value)
                else:
                    hdr, address = parseaddr(value)
                    name = decode_str(value)
                    value = u'%s <%s>' % (name, address)
            print('%s%s: %s' % ('   ' * indent, header, value))
    if message.is_multipart():
        parts = message.get_payload()
        for n, part in enumerate(parts):
            print('%s part %s' % ('  ' * indent, n))
            print('%s-------------------' % ('   ' * indent))
            print(part, indent + 1)
    else:
        content_type = message.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            content = message.get_payload(decode=True)
            charset = guess_charset(message)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % ('   ' * indent, content + '...........'))
        else:
            print('%sAttachment: %s' % ('   ' * indent, content_type))


if __name__ == '__main__':
    parser_email(collect_email())
