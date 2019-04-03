"""
闭包特点：
    函数嵌套
    外部函数返回内部函数的引用
    内部函数可以访问并且保存外部函数的变量
"""


def fun1(a):
    def fun2(b):
        nonlocal a
        a = a+b
        return a
    return fun2


f1 = fun1(10)
print(f1(20))
# f1 = fun1(10)
print(f1(20))
# f1 = fun1(10)
print(f1(20))
# f1 = fun1(10)
print(f1(20))









