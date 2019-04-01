import types
"""
类属性类方法、属于类，只占一份内存
实例方法、实例属性属于实例，每生成一个实例占用一份内存
声明实例属性、实例方法，浪费内存，适当的选择声明类属性和类方法节省内存
"""

# 动态添加属性和方法


class Person():
    """
    这是一个人类
    """
    __slots__ = ('name', 'age', 'gender', 'move', 'study', 'think')

    def __init__(self, _name):
        self.name = _name


p1 = Person('jack')
print(p1.name)
# 动态添加实例属性
p1.age = 20
print(p1.age)
# 不允许添加此属性
# p1.color = 'nj'
# print(p1.color)
# 动态添加类属性，__slots__只限制实例属性，不限制类属性
Person.country = 'China'
print(Person.country)

# 动态添加实例方法


def move(self):
    print('move')


p1.move = types.MethodType(move,p1)
p1.move()


# 动态添加类方法
@classmethod
def study(cls):
    print('study')


Person.study = study
Person.study()
p1.study()


# 定义静态方法
@staticmethod
def think():
    print('think')


Person.think = think
p1.think()

# 动态删除属性、方法
del p1.age
if hasattr(p1, 'age'):
    print('p1有age属性')
else:
    print('p1没有age属性')

if hasattr(p1, 'move'):
    print('p1有move方法')
else:
    print('p1没有move方法')
delattr(p1, 'move')
if hasattr(p1, 'move'):
    print('p1有move方法')
else:
    print('p1没有move方法')

if hasattr(Person, 'study'):
    print('Person有study方法')
else:
    print('Person没有study方法')
del Person.study
if hasattr(Person, 'study'):
    print('Person有study方法')
else:
    print('Person没有study方法')
