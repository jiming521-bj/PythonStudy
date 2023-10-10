# -*- coding: utf-8 -*-
# @Time     : 2023/10/11 12:06
# @Author   : JiMing
# @File     : 序列化和反序列化.py
# @SoftWare : PyCharm

# 设计一套标准，按照某种规则，把内存中的数据转换为字节序列，保存到文件，这就是序列化
# 反之，从文件的字节序列恢复到内存中，就是反序列化

# 使用JSON实现序列化
import json

# 打开文件
file = open('jiming.txt', 'w')
# 定义一个name列表
names = ['ming', 'wan', 'li', 'chen', 'zon', 'jiming']

# json序列化 将names对象序列化
names_text = json.dumps(names)

# 尝试将对象写入文件中
try:
    file.write(names_text)  # write() argument must be str, not list
except TypeError:
    print('类型错误')
else:
    print('数据写入成功')
finally:
    file.close()  # 关闭文件

# 使用dump()一步完成序列化并保存到文件
friends_list = [
    {'name': 'ming', 'age': 23, 'hobby': 'basketball', 'address': '贵州省天柱县'},
    {'name': 'jiming', 'age': 22, 'hobby': 'football', 'address': '贵州省永村县'}
]
# 打开文件 获取文件操作对象
fp = open('test.txt', 'w')

# 使用dump()方法进行序列化
try:
    json.dump(friends_list, fp)
except ModuleNotFoundError:
    print('不存在该模块')
except Exception as e:
    print(e)
else:
    print('数据写入文件成功')
finally:
    fp.close()


# 反序列化  load() 和 loads()
fp = open('test.txt', 'r')
# 读取文件
context = fp.read()
# 将JSON对象变成python对象 loads()方法读取的是文件中的数据
context = json.loads(context)
# 遍历python对象
for con in context:
    print(con)
# 关闭文件
fp.close()

