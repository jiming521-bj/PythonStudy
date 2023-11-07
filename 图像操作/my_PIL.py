# -*- coding: utf-8 -*-
# @Time     : 2023/11/7 10:00
# @Author   : JiMing
# @File     : my_PIL.py
# @SoftWare : PyCharm
from PIL import Image
from PIL import ImageFilter
from PIL import ImageDraw
from PIL import ImageFont
import random

"""
PIL：Python Imaging Library，已经是Python平台事实上的图像处理标准库了。
PIL功能非常强大，但API却非常简单易用。

由于PIL仅支持到Python 2.7，加上年久失修，于是一群志愿者在PIL的基础上创建了兼容的版本，名字叫Pillow，
支持最新Python 3.x，又加入了许多新特性，因此，我们可以直接安装使用Pillow。
"""


def test01():
    """图像缩放操作"""

    # 打开一个jpg图像，在当前路径下
    im = Image.open('test.jpg')
    # 获得图像尺寸
    width, height = im.size
    print(f"Original image size: {width} * {height}")
    # 开始图像进行缩放 缩放到50%
    im.thumbnail((width // 2, height // 2))
    print(f"Resize image to: {width // 2} * {height / 2}")
    # 把缩放后的图像用jpeg格式保存
    im.save('thumbnail.jpeg', 'jpeg')


def test02():
    # 对图像进行模糊
    # 打开一张图像
    im = Image.open('test.jpg')

    # 应用模糊滤镜
    im2 = im.filter(ImageFilter.BLUR)
    im2.save('blur.jpg', 'jpeg')
    pass


# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))


# 随机数字
def rndNumber():
    return str(random.randint(1, 9))


# 随机字符和数字
def rndCharNumber():
    L = [rndChar(), rndNumber()]
    return L[random.randint(0, 1)]


# 随机颜色1:
def rndColor():
    return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)


# 随机颜色2:
def rndColor2():
    return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)


def test03():
    """随机生成验证码"""
    # 240 x 60: 画布大小
    width = 60 * 6
    height = 60
    # 生成的图像模式
    image = Image.new('RGB', (width, height), (255, 255, 255))
    # 创建Font对象:
    font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 36)
    # 创建Draw对象:
    draw = ImageDraw.Draw(image)
    # 填充每个像素:
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndColor())
    # 存储文字的列表
    textList = []
    # 输出文字:
    for t in range(6):
        random_text = rndCharNumber()
        draw.text((60 * t + 10, 10), random_text, font=font, fill=rndColor2())
        textList.append(random_text)
    # 打印生成的验证码
    [print(i, end='') for i in textList]
    # 模糊:
    image = image.filter(ImageFilter.BLUR)
    image.save('code.jpg', 'jpeg')


if __name__ == '__main__':
    # test01()
    # test02()
    test03()
    pass
