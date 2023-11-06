# -*- coding: utf-8 -*-
# @Time     : 2023/11/6 11:39
# @Author   : JiMing
# @File     : my_hashlib.py
# @SoftWare : PyCharm
import hashlib

"""
Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。

什么是摘要算法呢？摘要算法又称哈希算法、散列算法。它通过一个函数，
把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。
"""


def test01():
    """生成一个MD5码"""
    md5 = hashlib.md5()
    md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
    value = md5.hexdigest()
    print(value)

    # 如果数据量很大，可以分多次调用
    md5.update('What\'s your name?'.encode('utf-8'))
    print(md5.hexdigest())


def test02():
    """SHAI算法"""
    sha1 = hashlib.sha1()
    sha1.update('This is my apple'.encode('utf-8'))
    sha1.update('python hashlib?'.encode('utf-8'))
    print(sha1.hexdigest())


def calc_md5(password):
    """根据用户输入的密码对其加密为md5返回"""
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()


db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}


def login(user, password):
    md5_password = calc_md5(password)
    if user in db.keys():
        if md5_password == db[user]:
            print('登录成功')
        else:
            print('密码有误!')
            print('登录失败!!!')
    else:
        print('用户名不存在')
        print('登录失败!!!')


def test03():
    """模拟用户登录"""
    login('bob', 'abc999')
    login('alice', 'alice2008')


my_user_sql = dict()


def get_md5(s):
    """获取加盐后的md5码"""
    md5 = hashlib.md5()
    md5.update(s.encode('utf-8'))
    return md5.hexdigest()


def register(username, password):
    """模拟用户注册"""
    if username in my_user_sql.keys():
        print('该用户名已存在 请换一个！')
        print('注册失败')
    else:
        my_user_sql[username] = get_md5(username + password + 'the-Salt')
        print('注册成功')
    # print(my_user_sql)


def loginM(username, password):
    """模拟用户登录"""
    login_message = username + password + 'the-Salt'
    verify = get_md5(login_message)
    if username in my_user_sql.keys():
        # 用户名存在的情况
        if my_user_sql[username] == verify:
            # 密码正确的情况
            print('登录成功!')
        else:
            print('密码有误!登录失败')
    else:
        print('用户名不存在!')


def test04():
    """测试用户的登录和注册"""
    try:
        choices = int(input('请输入你的选择(注册账号请按1，登录账号请按2)：'))
    except ValueError as e:
        print(e)
    else:
        if choices == 1:
            username = input('请输入用户名: ')
            password = input('请输入密码: ')
            register(username, password)
        elif choices == 2:
            username = input('请输入用户名: ')
            password = input('请输入密码: ')
            loginM(username, password)
        else:
            print('输入的指令不正确！')


def test05():
    """循环模拟登录注册"""
    while True:
        test04()
        if input('是否选择退出! 退出请按0,继续请按任意键: ') == '0':
            print('欢迎下次使用!')
            break


if __name__ == '__main__':
    # test01()
    # test02()
    # test03()
    # test04()
    test05()
    pass
