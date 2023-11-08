# -*- coding: utf-8 -*-
# @Time     : 2023/11/9 11:48
# @Author   : JiMing
# @File     : sqlalcheMy.py
# @SoftWare : PyCharm
import sqlalchemy.orm
from sqlalchemy import Column, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

# 创建对象的基类
Base = sqlalchemy.orm.declarative_base()


# 定义User对象
class User(Base):
    # 表名称
    __tablename__ = 'user'
    # 表结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

    # 一对多
    books = relationship('Book')


class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))

    # 多的一方的book表是通过外键关联到user表的
    user_id = Column(String(20), ForeignKey('user.id'))


# 初始化数据库连接 create_engine()用来初始化数据库连接。SQLAlchemy用一个字符串表示连接信息：
# '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+mysqlconnector://root:jiming@localhost:3306/test')

# 创建DBSession类型
DBSession = sessionmaker(bind=engine)
# 创建session对象
session = DBSession()


def add_row():
    # 创建User对象
    new_user = User(id='5', name='Ming')
    new_books = Book(id='1', name='平凡的世界', user_id='5')
    # 添加到session中
    session.add(new_user)
    # 提交即保存到数据库
    session.commit()
    # 关闭session
    session.close()

    # 打印提示信息
    print('添加成功')


def inquire_row():
    # 查询数据
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    user = session.query(User).filter(User.id).all()
    # 打印类型和对象的name属性
    print('type: ', type(user))
    for n in user:
        print('name: ', n.name, n.books)
    # 关闭Session
    session.close()
    # 可见，ORM就是把数据库表的行与相应的对象建立关联，互相转换。


if __name__ == '__main__':
    # add_row()
    inquire_row()
