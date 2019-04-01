"""
实例方法：第一个参数是self
类方法：第一个参数是cls，并且使用@classmethod声明
静态方法：需要使用@staticmethod声明

实例可以调用，类方法、静态方法、实例方法
类可以调用，类方法、静态方法
"""


class Stu():
    """
    这是一个学生类
    """

    def __init__(self, _name, _age):
        self.name = _name
        self.age = _age

    def getinfo(self):
        print(self.name, self.age)

    @classmethod
    def met(cls):
        print(cls.__doc__)

    @staticmethod
    def meh():
        print('静态方法')


s1 = Stu('jack', 20)
s1.getinfo()
s1.met()
s1.meh()

Stu.met()
Stu.meh()

