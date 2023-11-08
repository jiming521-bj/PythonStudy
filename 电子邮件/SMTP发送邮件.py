# -*- coding: utf-8 -*-
# @Time     : 2023/11/7 21:15
# @Author   : JiMing
# @File     : SMTP发送邮件.py
# @SoftWare : PyCharm
# 导入处理纯文本文件的邮件模块
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib
import timeout_decorator

# SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送村文本邮件、HTML邮件以及带附件的邮件
"""
Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件
"""


def send_text():
    """发送纯文本文件的邮件"""
    msg = MIMEText('如果你的名字就是这样，那么我愿意追随', 'plain', 'utf-8')
    """
    注意到构造MIMEText对象时，第一个参数就是邮件正文，第二个参数是MIME的subtype，
    传入plain表示纯文本，最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性
    """
    return msg


def send_html():
    """发送HTML邮件"""
    """
    如果我们要发送HTML邮件，而不是普通的纯文本文件怎么办？方法很简单，
    在构造MIMEText对象时，把HTML字符串传进去，再把第二个参数由plain变为html就可以了
    """
    msg = MIMEText('''
        <html>
            <header>
                <title>python小知识分享</title>
            </header>
            <body>
                <h6>Python的由来</h6>
                <p>
                    <img src='https://steamuserimages-a.akamaihd.net/ugc/
                    1722038779511414256/BE6A52CC21E1325CAB97815A6DFF8A58A6737100/?imw=5000&imh=5000&
                    ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false'>
                    <a href='https://www.baidu.com/s?wd=python的由来'>点击查看python的由来</a>
                    <ul>
                        <li>你的名字</li>
                        <li>如果你好</li>
                    </ul>
                </p>
            </body>
        </html>
    ''', 'html', 'utf-8')
    return msg


def send_img():
    """邮件正文附带图片"""
    """
    如果要把一个图片嵌入到邮件正文中怎么做？直接在HTML邮件中链接图片地址行不行？
    答案是，大部分邮件服务商都会自动屏蔽带有外链的图片，因为不知道这些链接是否指向恶意网站。
    要把图片嵌入到邮件正文中，我们只需按照发送附件的方式，先把邮件作为附件添加进去，
    然后，在HTML中通过引用src="cid:0"就可以把附件作为图片嵌入了。
    如果有多个图片，给它们依次编号，然后引用不同的cid:x即可。
    """
    msg = MIMEText('<html><body><h1>Hello</h1>' +
                   '<p><img src="cid:0"></p>' +
                   '</body></html>', 'html', 'utf-8')
    return msg


def send_html_text():
    """同时支持HTML和Plain格式"""
    """
    如果我们发送HTML邮件，收件人通过浏览器或者Outlook之类的软件是可以正常浏览邮件内容的，
    但是，如果收件人使用的设备太古老，查看不了HTML邮件怎么办？
    办法是在发送HTML的同时再附加一个纯文本，如果收件人无法查看HTML格式的邮件，就可以自动降级查看纯文本邮件。
    """
    """
    msg = MIMEMultipart('alternative')
    msg.attach(MIMEText('hello', 'plain', 'utf-8'))
    msg.attach(MIMEText('<html><body><h1>Hello</h1></body></html>', 'html', 'utf-8'))
    # 正常发送msg对象...
    """
    pass


def format_address(s):
    """处理邮件发送者 接受者信息"""
    name, address = parseaddr(s)
    # print(name, address)
    return formataddr((Header(name, 'utf-8').encode(), address))


# @timeout_decorator.timeout(10)
def send_email():
    """使用SMTP发送邮件"""
    # 输入Email地址和口令
    # from_address = input('From: ')
    from_address = 'wumingming7890@163.com'
    # password = input('Password: ')
    password = 'XZZLKXFENMULABTJ'
    # 输入收件人地址：
    # to_address = input('TO: ')
    # to_address = 'jiming7890@qq.com'
    # to_address = 'jiming581@gmail.com'
    to_address = ['jiming7890@qq.com', 'jiming581@gmail.com']
    # 输入SMTP服务器地址：
    # smtp_server = input('SMTP server: ')
    smtp_server = 'smtp.163.com'
    # 设置端口  SMTP协议默认的端口是25 标准使用的明文传输
    server = smtplib.SMTP_SSL(smtp_server, 465)
    # 加密SMTP 发送端口： 25或465/994(使用ssl时)
    # server.starttls()
    print('端口设置完成!')
    # 打印出和SMTP服务器交互的所有信息
    # server.set_debuglevel(1)
    # 验证账号和口令
    server.login(from_address, password)
    print('账号验证成功!')
    # 遍历目标邮件
    for target_address in to_address:
        # 发送纯文本邮件
        emailContent = send_text()
        # 发送HTML格式的邮件
        # emailContent = send_html()

        # 发送附件 设置邮件对象
        # emailContent = MIMEMultipart()

        # 添加邮件主题 设置发件者和收件者信息
        emailContent['From'] = format_address('明明的Python助手<%s>' % from_address)
        emailContent['To'] = format_address('用户<%s>' % target_address)
        emailContent['Subject'] = Header('Python日推内容....', 'utf-8').encode()

        # 添加邮件正文
        # emailContent.attach(MIMEText('send with file.....', 'plain', 'utf-8'))

        # 添加附件就是加上一个MIMEBase，从本地读取一张图片
        # with open('test.jpg', 'rb') as imgFile:
        #     # 设置附件的MIME和文件名 这里是jpg
        #     mime = MIMEBase('image', 'jpg', filename='test.jpg')
        #     # 加上必要的头信息
        #     mime.add_header('Content-Disposition', 'attachment', filename='test.jpg')
        #     mime.add_header('Content-ID', '<0>')
        #     mime.add_header('X-Attachment-Id', '0')
        #     # 把附件的内容读进来
        #     mime.set_payload(imgFile.read())
        #     # 用base64编码
        #     encoders.encode_base64(mime)
        #     # 添加到MIMEMultipart
        #     emailContent.attach(mime)
            # 添加图片到正文
            # emailContent.attach(send_img())
        # 发送邮件
        server.sendmail(from_address, target_address, emailContent.as_string())
        print('邮件发送中....')
    # 退出邮件服务
    server.quit()
    print('邮件投递成功!')
    # XZZLKXFENMULABTJ 网易163邮箱的SMTP密码  对应的账号为wuminging7890@163.com
    """
    邮件没有主题；
    收件人的名字没有显示为友好的名字，比如Mr Green <green@example.com>；
    明明收到了邮件，却提示不在收件人中。
    这是因为邮件主题、如何显示发件人、收件人等信息并不是通过SMTP协议发给MTA，
    而是包含在发给MTA的文本中的，所以，我们必须把From、To和Subject添加到MIMEText中，才是一封完整的邮件：
    """


if __name__ == '__main__':
    # test01()
    send_email()
    pass

"""
总结：
使用Python的smtplib发送邮件十分简单，只要掌握了各种邮件类型的构造方法，正确设置好邮件头，就可以顺利发出。
构造一个邮件对象就是一个Messag对象，如果构造一个MIMEText对象，就表示一个文本邮件对象，
如果构造一个MIMEImage对象，就表示一个作为附件的图片，要把多个对象组合起来，就用MIMEMultipart对象，
而MIMEBase可以表示任何对象。它们的继承关系如下：

Message
+- MIMEBase
   +- MIMEMultipart
   +- MIMENonMultipart
      +- MIMEMessage
      +- MIMEText
      +- MIMEImage
这种嵌套关系就可以构造出任意复杂的邮件。你可以通过email.mime文档查看它们所在的包以及详细的用法。
"""