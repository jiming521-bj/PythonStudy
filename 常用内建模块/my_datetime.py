# -*- coding: utf-8 -*-
# @Time     : 2023/11/4 18:23
# @Author   : JiMing
# @File     : my_datetime.py
# @SoftWare : PyCharm

from datetime import datetime
from datetime import timedelta
from datetime import timezone

import re


# datetime 使用Python处理日期和时间的标准库

def test01():
    """获取当前时间"""
    now = datetime.now()
    print(now)

    # 查看now所属于的类型
    print(type(now))

    """使用datetime.now()来获取当前系统时间"""


def test02():
    """获取指定日期和时间"""
    dt = datetime(2023, 11, 4, 18, 28, 55)
    print(dt)


def test03():
    """datetime 和 timestamp之间的相互转换"""
    # datetime转换为timestamp
    # timestamp和时区没有关系
    dt = datetime(2023, 11, 4, 18, 31, 5)
    print(dt.timestamp())

    # timestamp 转换为 datetime
    time = 1699093865.0
    print(datetime.fromtimestamp(time))

    # UTC时间
    print(datetime.utcfromtimestamp(time))


def test04():
    """datetime 和 str之间的转换"""
    cDay = datetime.strptime('2023-10-21 18:10:55', "%Y-%m-%d %H:%M:%S")
    print(cDay)
    # 转换后的时间是没有时区信息的

    # datetime转换为str
    now = datetime.now()
    print(now.strftime('%a, %b %d %H:%M'))


def test05():
    """datetime加减"""
    # 对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime
    # 可以直接使用 + -对时间进行操作
    now = datetime.now()
    print(now)

    print(now + timedelta(hours=10))
    print(now - timedelta(days=1))
    print(now + timedelta(days=1, hours=10))


def test06():
    """本地时间转化为UTC时间"""
    # 本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间
    tz_utc_8 = timezone(timedelta(hours=8))  # 创建北京东八区时间
    now = datetime.now()
    print(now)
    # 重新指定时间
    other_now = datetime(2012, 12, 12, 18, 5, 10, 129324)
    print(other_now)

    # 将指定的时间设置为北京时间
    dt = now.replace(tzinfo=tz_utc_8)
    print(dt)
    # 如果系统时区恰好是UTC+8:00，那么上述代码就是正确的，否则，不能强制设置为UTC+8:00时区。
    print(datetime(2023, 12, 12, 10, 10, 10, 102034, tzinfo=timezone(timedelta(0, 28800))))


def test07():
    """时区转换"""
    # 先拿到UTC时间 并强制设置时区为修改的时区
    utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
    print(utc_dt)

    # astimezone()将其时间转换为北京时间
    bj_time = utc_dt.astimezone(timezone(timedelta(hours=8)))
    print(bj_time)

    # astimezone() 将其时间转化为东京时间
    dj_time = utc_dt.astimezone(timezone(timedelta(hours=9)))
    print(dj_time)

    # astimezone() 将北京时间转换为东京时间
    dj_time_2 = bj_time.astimezone(timezone(timedelta(hours=9)))
    print(dj_time_2)


global nowStrUtc


def to_timestamp(time, utc):
    """将带有时区的str转换为timestamp格式"""
    global nowStrUtc
    nowStrTime = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
    # print(type(nowStrTime))

    # 获取时区
    m = re.match(r'^(UTC)([+,-]\d):(0*)$', utc)
    try:
        m = m.group(2)
    except AttributeError:
        print('输入的时区格式不正确,请检查(例子:UTC+7:00 UTC-9:00)!!!!!')
    else:
        nowStrUtc = timezone(timedelta(hours=int(m)))

    # 设置用户传入的时区
    value = nowStrTime.replace(tzinfo=nowStrUtc)
    print(value)

    # 将带有时间类型的datetime转换成timestamp(时间戳)
    return datetime.timestamp(value)


def test08():
    """sample"""
    """
    假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，
    请编写一个函数将其转换为timestamp：
    """
    # 测试一
    t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
    assert t1 == 1433121030.0, t1
    print('测试一通过')

    # 测试二
    t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-9:00')
    assert t2 == 1433121030.0, t2
    print('测试二通过')
    print('Pass')


if __name__ == '__main__':
    # test01()
    # test02()
    # test03()
    # test04()
    # test05()
    # test06()
    # test07()
    test08()
"""
总结：
datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。
如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。
"""
