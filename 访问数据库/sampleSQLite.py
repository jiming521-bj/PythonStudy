# -*- coding: utf-8 -*-
# @Time     : 2023/11/8 21:21
# @Author   : JiMing
# @File     : sampleSQLite.py
# @SoftWare : PyCharm

# -*- coding: utf-8 -*-
import os
import sqlite3

# 创建数据库文件
db_file = os.path.join(os.path.dirname(__file__), 'jiming.db')
if os.path.isfile(db_file):
    os.remove(db_file)
# 初始数据:
# 连接数据库
conn = sqlite3.connect(db_file)
# 获取游标
cursor = conn.cursor()
# 创建关系表
try:
    cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
except sqlite3.OperationalError as e:
    print(e)
else:
    # 添加记录
    cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
    cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
    cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
    # 获取添加记录个数
    value = cursor.rowcount
    # print(value)
    # 提交事务
    conn.commit()
finally:
    cursor.close()
    conn.close()


def get_score_in(low, high):
    # 返回指定分数区间的名字，按分数从低到高排序
    # 连接数据库
    conn_inquire = sqlite3.connect(db_file)
    # 获取游标
    cursor_inquire = conn_inquire.cursor()
    # 根据成绩查询表记录并返回
    cursor_inquire.execute('select name from user where score between ? and ? order by score ASC ', (low, high))

    # 返回查询结果
    values = [list(i) for i in cursor_inquire.fetchall()]
    v = list()
    for j in values:
        v = v + j
    return v


# 测试:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)
# print(get_score_in(60, 80))
print('Pass')
