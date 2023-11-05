# -*- coding: utf-8 -*-
# @Time     : 2023/11/3 21:53
# @Author   : JiMing
# @File     : 正则表达式.py
# @SoftWare : PyCharm
import re

"""
字符串是编程时涉及到的最多的一种数据结构，对字符串进行操作的需求几乎无处不在。
比如判断一个字符串是否是合法的Email地址，虽然可以编程提取@前后的子串，再分别判断是否是单词和域名，
但这样做不但麻烦，而且代码难以复用。

所以我们判断一个字符串是否是合法的Email的方法是：

1、创建一个匹配Email的正则表达式；
2、用该正则表达式去匹配用户的输入来判断是否合法。

\d 用于匹配任意一个数字
\w 用于匹配任意一个字母
要匹配变长的字符，在正则表达式中，用*表示任意个字符（包括0个），
用+表示至少一个字符，用?表示0个或1个字符，用{n}表示n个字符，用{n,m}表示n-m个字符


要做更精确地匹配，可以用[]表示范围，比如：

[0-9a-zA-Z_]可以匹配一个数字、字母或者下划线；
[0-9a-zA-Z_]+可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等等；
[a-zA-Z_][0-9a-zA-Z_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，
也就是Python合法的变量；

[a-zA-Z_][0-9a-zA-Z_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）。
A|B可以匹配A或B，所以[P|p]ython可以匹配'Python'或者'python'。
^表示行的开头，^\d表示必须以数字开头。
$表示行的结束，\d$表示必须以数字结束。
你可能注意到了，py也可以匹配'python'，但是加上^py$就变成了整行匹配，就只能匹配'py'了。
"""


def test01():
    """判断正则表达式是否匹配假定值"""
    value = re.match(r'^\d{3}\\-\d{3,8}$', '010-12345')
    print(value)

    value = re.match(r'^\d{3}\\-\d{3,8}$', '010 12345')
    print(value)

    """
    match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None
    """


def test02():
    """测试match()"""
    flag = 0
    test = input('请输入任意字符串: ')
    if re.match(r'\d{3}-\d{3,8}$', test):
        print('OK')
        flag = 1
    else:
        print('Failed')
    return flag


def test03():
    """切分字符串"""
    value = 'a b    c'.split(' ')
    print(value)

    value = re.split(r'\s+', 'a b c    d')
    print(value)

    value = re.split(r'[\s,]+', 'a, b,c    d,  e')
    print(value)

    value = re.split(r'[\s,;]+', 'a, b, d;; c   d')
    print(value)


def test04():
    """分组"""
    # 如果正则表达式中定义了组，就可以在Match对象上用group()方法提取出子串来
    """
    group(0)表示是原始字符串
    group(1)表示是第一个子串
    group(2)表示是第二个子串
    ......
    """
    t = '19:05:30'
    m = re.match(
        r'^(0[0-9]|1[0-9]|2[0-3]|[0-9]):(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9]):(0[0-9]|1[0-9]|2[0-9]|3['
        r'0-9]|4[0-9]|5[0-9]|[0-9])$',
        t)
    print(m.groups())


def test05():
    """贪婪匹配"""
    print(re.match(r'^(\d+)(0*)$', '1023000').groups())

    """非贪婪匹配"""
    print(re.match(r'(\d+?)(0*)$', '1023000').groups())


def test06():
    """
    如果一个正则表达式要重复使用几千次，出于效率的考虑，
    我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了，直接匹配
    :return:
    """
    # 编译
    re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
    # 使用
    value_1 = re_telephone.match('010-12345').groups()
    value_2 = re_telephone.match('010-666').groups()

    print(value_1, value_2)


def test07():
    """配置UTC时区"""
    UTCString = 'UTC-7:00'
    m = re.match(r'^(UTC)([+,-]\d):(0*)$', UTCString)
    print(m.group())
    print(m.group(1))
    print(m.group(2))


def test08():
    """sample"""
    # 尝试写一个验证Email地址的表达式，版本一应该可以验证出类似的Email
    """
    someone@gmail.com
    bill.gates@microsoft.com
    """
    email = 'billgates@microsoft.com'
    value = re.match(r'[(\w+).]*@(\w+)(.com)$', email)
    print(value)


def test09():
    """匹配带名字的邮箱"""
    email_username = '<Tom Paris> tom@voyager.org'
    value = re.match(r'(<[\w+ ]*>)\s?(\w+)@(\w+)(.org)$', email_username)
    print(value)

    # 输出原始邮箱
    print(value.group(0))
    # 提取邮箱的用户名
    print(value.group(2))

    print(value.groups())


if __name__ == '__main__':
    # test01()
    # while True:
    #     if test02():
    #         break
    # test03()
    # test04()
    # test05()
    # test06()
    # test07()
    # test08()
    test09()
