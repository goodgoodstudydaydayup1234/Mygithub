"""
类与对象
类：模板，定义属性和方法的封装
实例：具体的类对象，类的表现

1.实例的属性会根据实例的不同而不同，而类属性由类决定
2.实例属性通常在创建实例时赋值，而类属性是在创建类时赋值
3.实例属性属于实例，而类属性属于类
实例确定后，实例属性就确定了
实例可以调用类属性，类不可以调用实力属性
"""


class Stu():
    age = 20

    def __init__(self, _name, _gender):
        self.name = _name
        self.gender = _gender


s1 = Stu('jack', '男')
s2 = Stu('rose', '女')

print(s1.name, s1.gender, s1.age)
print(s2.name, s2.gender, s2.age)
print(Stu.age)
