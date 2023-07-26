# -*- coding: utf-8 -*-
# @Time     : 2022/12/2 12:42
# @Author   : JiMing
# @File     : 4字符串和编码.py
# @SoftWare : PyCharm

"""
Unicode标准也在不断发展，但最常用的是用两个字节表示一个字符
（如果要用到非常偏僻的字符，就需要4个字节）。现代操作系统和大多数编程语言都直接支持Unicode。
现在，捋一捋ASCII编码和Unicode编码的区别：ASCII编码是1个字节，而Unicode编码通常是2个字节。
字母A用ASCII编码是十进制的65，二进制的01000001；
字符0用ASCII编码是十进制的48，二进制的00110000，注意字符'0'和整数0是不同的；
汉字中已经超出了ASCII编码的范围，用Unicode编码是十进制的20013，二进制的01001110 00101101。
你可以猜测，如果把ASCII编码的A用Unicode编码，只需要在前面补0就可以，
因此，A的Unicode编码是00000000 01000001
"""
# 字符串
char = 'A'
print(ord(char))  # 将字符对应的ASCII编码转换成数字

number = 97
print(chr(number))  # 将数字转换为对应的ASCII编码

# 十六进制编写字符串
print('\u4e2d\u6587')
print('中文')

"""
由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。
如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
"""

x = 'ABC'
y = b'ABC'
print(f"{x}, {y}")
print(type(x))
print(type(y))

# 以Unicode表示的Str通过encode()方法可以编码为制定的bytes
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))

# print('中文'.encode('ascii'))  # 不能将中文使用ascii编码进行保存,中文的表示范围大于ascii

# 将字节流bytes变为str类型就需要使用decode()方法
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# 获取字符串的长度len
message = "This is a beautiful dress"
print(len(message))
list_numbers = [i for i in range(1, 10)]
print(len(list_numbers))

# len()是计算str字符长度，如果换成bytes那计算的就是字节数
print(len(b'ABC'))
print(len('中文'.encode('utf-8')))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))

# 可见，1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节。


# 格式化输出字符串
print("This is %d number" % list_numbers[1])
print("This words is %s." % "beautiful")
print("Hi, %s, you have $%d." % ('JiMing', 100))

# 常见的占位符
# | %d | 整数 || %f | 浮点数 || %s | 字符串 || %x | 十六进制整数 |

print('%d-%05d' % (1, 3))
print('%.2f' % 3.1415926)

# demo
"""
小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，
并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
"""
old_year_score = 72.0
new_year_score = 85.0
temp_score = (new_year_score - old_year_score) / old_year_score
print('%.1f%%' % (temp_score * 100))

