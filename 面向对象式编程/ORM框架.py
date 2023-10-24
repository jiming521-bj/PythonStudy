# -*- coding: utf-8 -*-
# @Time     : 2023/7/23 8:53
# @Author   : JiMing
# @File     : ORM框架.py
# @SoftWare : PyCharm

# 定义字段基类
class Field(object):
    # 初始化实例数据
    def __init__(self, name, column_type):
        # 字段名称
        self.name = name
        # 字段所属类型
        self.column_type = column_type

    # 以字符串的格式返回字段名称和字段类型
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


# 定义字段派生类
class StringField(Field):
    # 初始化数据
    def __init__(self, name):
        # 继承父类的初始化方法 重写父类的__init__方法
        super(StringField, self).__init__(name, 'varchar(100)')  # 利用子类向父类传值初始化


class IntegerField(Field):
    # 重写父类__init__方法
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaclass(type):  # 定义元类
    def __new__(mcs, name, bases, attrs):
        if name == 'Model':
            return type.__new__(mcs, name, bases, attrs)
        print('Found model: %s' % name)

        mappings = dict()
        for key, value in attrs.items():
            if isinstance(value, Field):
                print('Found mapping: %s ==> %s' % (key, value))
                mappings[key] = value
        for key in mappings.keys():
            attrs.pop(key)
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类名一致
        return type.__new__(mcs, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def sava(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) value (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


class User(Model):
    # 定义类的属性到列的映射
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


if __name__ == '__main__':
    # 创建一个实例
    u = User(id=1212, name='chen', email='jiming581@gmail.com', password='ming')

    # 保存到数据库中
    u.sava()
