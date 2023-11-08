# -*- coding: utf-8 -*-
# @Time     : 2023/11/9 10:36
# @Author   : JiMing
# @File     : sampleMysql.py
# @SoftWare : PyCharm
# 导入mysql驱动
import pymysql

"""
MySQL是Web世界中使用最广泛的数据库服务器。SQLite的特点是轻量级、可嵌入，但不能承受高并发访问，
适合桌面和移动应用。而MySQL是为服务器端设计的数据库，能承受高并发访问，同时占用的内存也远远大于SQLite。
"""
# 连接数据库
conn = pymysql.connect(
    user='root',
    password='jiming',
    database='test'
)

# 获取游标
cursor = conn.cursor()


def create_table():
    try:
        # 创建user表
        cursor.execute('create table book (id varchar(20) primary key , name varchar(20))')
    except pymysql.OperationalError as e:
        print(e)
    else:
        # 插入一行记录 注意MySQL的占位符是%s
        cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Jiming'])

        # 返回影响行数
        row = cursor.rowcount
        print(row)
        # 提交事务
        conn.commit()
    finally:
        # 关闭游标
        cursor.close()
        # 关闭数据库连接
        conn.close()


def search_table():
    # 查询数据
    try:
        cursor.execute('select * from user where 1')
    except BaseException as e:
        print(e)
    else:
        values = cursor.fetchall()
        print(values)
    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    # create_table()
    search_table()
