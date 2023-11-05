# -*- coding: utf-8 -*-
# @Time     : 2023/11/5 12:31
# @Author   : JiMing
# @File     : my_collections.py
# @SoftWare : PyCharm
from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import Counter


# collections 是Python内建的一个集合模块，提供了许多有用的集合类
# tuple 表示不可变对象
def test01():
    """namedtuple"""
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1, 2)
    print(p.x)
    print(p.y)
    """
    namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，
    并可以用属性而不是索引来引用tuple的某个元素。
    """
    print(isinstance(p, Point))
    print(isinstance(p, tuple))


def test02():
    """deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈："""
    # 创建一个deque容器
    q = deque(['a', 'b', 'c'])
    # 向容器中尾部插入一个数据
    q.append('x')
    # 向容器第一个位置插入一个数据
    q.appendleft('y')
    # 打印当前deque容器
    print(q)

    # 将容器中的最后一个值删除
    q.pop()

    # 将容器的第一个值删除
    q.popleft()

    # 再次打印容器
    print(q)

    for i in q:
        print(i, end=' ')
    print()

    """
    deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，
    这样就可以非常高效地往头部添加或删除元素。
    """


def test03():
    """defaultdict方法的使用"""
    """
    使用dict时，如果引用的Key不存在，就会抛出KeyError
    如果希望key不存在时，返回一个默认值，就可以使用defaultdict
    """
    # 设置dict访问getter方法的默认返回值 'N/A'
    dd = defaultdict(lambda: 'N/A')
    # 存储两个键值对
    dd['one'] = 'ming'
    dd['two'] = 'jiming'

    # 访问dd字典的键值对
    print(dd.get('one'))
    print(dd.get('two'))

    # 尝试访问不存在的键
    print(dd['name'])


def test04():
    """OrderedDict"""
    """
    使用dict时，Key是无序的，在对dict做迭代时，我们无法确定Key的顺序
    如果要保持Key的顺序，可以用OrderDict
    """
    # 此时的Key是无序的
    d = dict([('a', 1), ('c', 2), ('d', 3)])
    print(d)
    d1 = dict(a=1, b=2, c=3)
    d1['d'] = 4
    d1['e'] = 5
    d1['f'] = 6
    print(d1)

    # 使用OrderedDict对其排序
    od = OrderedDict([('a', 1), ('c', 3), ('b', 2)])
    # 此时打印od 是有序的键值排序
    print(od)

    od['d'] = 4
    od['e'] = 5
    print(od)
    print(list(od.keys()))


class LastUpdatedOrderedDict(OrderedDict):
    """OrderedDict实现先进先出的dict"""

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)


def test05():
    """先进先出队列测试"""
    d = LastUpdatedOrderedDict(2)
    d['name'] = 'ming'
    print(d.get('name'))

    # 添加一对键值对
    d['age'] = 12
    print(d.get('age'))

    # 在添加一个 因为容量为2 所以最先添加的name键被自动移除了
    d['hobby'] = 'basketball'
    print(d.get('hobby'))

    # 添加一个重复的键值对
    d['hobby'] = 'baseball'
    print(d)


def test06():
    """Counter方法"""
    c = Counter()
    for ch in 'programmer':
        c[ch] = c[ch] + 1

    print(c)


if __name__ == '__main__':
    # test01()
    # test02()
    # test03()
    # test04()
    # test05()
    test06()
