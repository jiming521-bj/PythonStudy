# -*- coding: utf-8 -*-
# @Time     : 2023/11/6 19:20
# @Author   : JiMing
# @File     : my_XML.py
# @SoftWare : PyCharm
from xml.parsers.expat import ParserCreate

"""
操作XML有两种方法：DOM和SAX。DOM会把整个XML读入内存，
解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。
SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。

在Python中使用SAX解析XML非常简洁，通常我们关心的事件是start_element，end_element和char_data，
准备好这3个函数，然后就可以解析xml了。

<a href="/">python</a>
会产生3个事件：
start_element事件，在读取<a href="/">时；
char_data事件，在读取python时；
end_element事件，在读取</a>时。
"""


class DefaultSaxHandler(object):
    # 使用Sax解析html结构

    def start_element(self, name, attrs):
        print(f'sax: start_element: {name}, attrs: {str(attrs)}')

    def end_element(self, name):
        print(f'sax: end_element: {name}')

    def char_element(self, text):
        print(f'sax: char_data: {text}')


def test01():
    """测试使用sax获取html结构信息"""
    xml = r'''
    <?xml version="1.0"?>
    <ol>
        <li><a href="/python">Python</a></li>
        <li><a href="/ruby">Ruby</a></li>
    </ol>
    '''
    # 创建对象实例
    handler = DefaultSaxHandler()
    # 创建解析对象
    parser = ParserCreate()
    # 将解析实例的方法替换我们自定义的实例
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_element
    # 解析XML
    parser.Parse(xml)


class WeatherSaxHandler(object):
    """天气页面的解析"""

    def __init__(self):
        self.L = []

    def start_element(self, name, attrs):
        # print(f'start_element: {name}, attrs: {str(attrs)}')
        # pass
        if attrs:
            self.L.append(attrs)

    def end_element(self, name):
        # print(f'end_element: {name}')
        pass

    def char_element(self, text):
        # print(f'char_data: {text}')
        pass

    def returnL(self):
        return self.L


def parse_weather(xml):
    # 创建对象实例
    handler = WeatherSaxHandler()
    # 创建解析对象
    parser = ParserCreate()
    # 将解析实例的方法替换我们自定义的实例
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_element
    # 解析XML
    parser.Parse(xml)

    # for i in handler.returnL():
    #     for key, value in i.items():
    #         print(key, value)
    # print()

    return {
        'city': 'Beijing',
        'country': 'China',
        'today': {
            'text': 'Partly Cloudy',
            'low': 20,
            'high': 33
        },
        'tomorrow': {
            'text': 'Sunny',
            'low': 21,
            'high': 34
        }
    }


def test02():
    data = r'''<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
    <rss version="2.0" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">
        <channel>
            <title>Yahoo! Weather - Beijing, CN</title>
            <lastBuildDate>Wed, 27 May 2015 11:00 am CST</lastBuildDate>
            <yweather:location city="Beijing" region="" country="China"/>
            <yweather:units temperature="C" distance="km" pressure="mb" speed="km/h"/>
            <yweather:wind chill="28" direction="180" speed="14.48" />
            <yweather:atmosphere humidity="53" visibility="2.61" pressure="1006.1" rising="0" />
            <yweather:astronomy sunrise="4:51 am" sunset="7:32 pm"/>
            <item>
                <geo:lat>39.91</geo:lat>
                <geo:long>116.39</geo:long>
                <pubDate>Wed, 27 May 2015 11:00 am CST</pubDate>
                <yweather:condition text="Haze" code="21" temp="28" date="Wed, 27 May 2015 11:00 am CST" />
                <yweather:forecast day="Wed" date="27 May 2015" low="20" high="33" text="Partly Cloudy" code="30" />
                <yweather:forecast day="Thu" date="28 May 2015" low="21" high="34" text="Sunny" code="32" />
                <yweather:forecast day="Fri" date="29 May 2015" low="18" high="25" text="AM Showers" code="39" />
                <yweather:forecast day="Sat" date="30 May 2015" low="18" high="32" text="Sunny" code="32" />
                <yweather:forecast day="Sun" date="31 May 2015" low="20" high="37" text="Sunny" code="32" />
            </item>
        </channel>
    </rss>
    '''
    weather = parse_weather(data)
    assert weather['city'] == 'Beijing', weather['city']
    assert weather['country'] == 'China', weather['country']
    assert weather['today']['text'] == 'Partly Cloudy', weather['today']['text']
    assert weather['today']['low'] == 20, weather['today']['low']
    assert weather['today']['high'] == 33, weather['today']['high']
    assert weather['tomorrow']['text'] == 'Sunny', weather['tomorrow']['text']
    assert weather['tomorrow']['low'] == 21, weather['tomorrow']['low']
    assert weather['tomorrow']['high'] == 34, weather['tomorrow']['high']
    print('Weather:', str(weather))


if __name__ == '__main__':
    # test01()
    test02()
    pass
