"""
可迭代Iterable和迭代器Iterator
可迭代：可以用for循环
迭代器：有next()方法
生成器既可迭代，又是迭代器
"""
from collections.abc import Iterable,Iterator

list1 = [1, 2, 3, 4, 5]
# print(next(list1))
print(isinstance(list1, Iterable))
print(isinstance(list1, Iterator))
print(isinstance(iter(list1), Iterator))
