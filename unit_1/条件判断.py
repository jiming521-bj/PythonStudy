# -*- coding: utf-8 -*-
# @Time     : 2022/12/4 11:41
# @Author   : JiMing
# @File     : 条件判断.py
# @SoftWare : PyCharm

# 计算机之所以能做很多自动化的任务，因为它可以自己做条件判断。
# username = input('Please your username: ')
# password = input('Please your address: ')
# if username == 'JiMing' and password == 'admin':
#     print('yes')
# else:
#     print("User or password error")

age = 20
if age > 20:
    print('your age is ', age)
    print('adult')
else:
    print('You are not more than twenty years old')

# elif 多分支
"""
if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
elif <条件判断3>:
    <执行3>
else:
    <执行4>
"""

height = 160
if height > 180:
    print("your are Tall")
elif height > 170:
    print("your are nice")
else:
    print("your are short")

# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
# input()从终端获取的内容是字符串，如果要获取数字，要进行转换
# s = input('birth: ')
# birth = int(s)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')

# demo
"""
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，
并根据BMI指数：
        低于18.5：过轻
        18.5-25：正常
        25-28：过重
        28-32：肥胖
        高于32：严重肥胖
"""
height = float(input("请输入你的身高(m): "))
weight = float(input("请输入你的体重(kg): "))
Bmi = round(weight / height ** 2, 2)  # 保留两位小数
print(Bmi)

# 根据指数判断身体状况
if Bmi > 32:
    print("严重肥胖")
elif Bmi > 28:
    print("肥胖")
elif Bmi > 25:
    print("过重")
elif Bmi > 18.5:
    print("正常")
else:
    print("过轻")
