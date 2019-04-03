"""
垃圾回收-引用计数
    引用计数+1的情况
        1.对象被创建时，如a=‘fdd’
        2.对象被copy引用时，如b=a
        3.对象被作为参数，传递到函数中时
        4.对象被作为一个子元素，存储到容器中时，如list=[a,b]
    引用计数-1的情况
        1.对象别名被销毁，如del a
        2.对象引用被赋予新的对象，如b=‘we’
        3.一个函数离开它的作用域，例如函数执行完成
        4.对象所在容器被销毁，或者从容器中删除
    引用计数的优点：
        简单、直观
        实时性、只要没有了引用就释放资源
    引用计数的缺点：
        维护引用计数需要消耗一定的资源
        循环引用时，无法回收
"""
import sys

print(sys.getrefcount('hello'))
a = 'hello'
print(sys.getrefcount('hello'))
# del a
# print(sys.getrefcount('hello'))
b = a
print(sys.getrefcount('hello'))
print(sys.getrefcount(a))
# del a
# print(sys.getrefcount(a))   # NameError: name 'a' is not defined
print(sys.getrefcount('hello'))
# del b
# b = 'world'
print(sys.getrefcount('hello'))

print(a)
print(b)
list1 = [a, b]
print(sys.getrefcount('hello'))

del list1
print(sys.getrefcount('hello'))
