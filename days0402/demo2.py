"""
用函数来创建生成器
"""

def f():
    yield 1
    yield 2
    yield 3
    return 'hello'

result = f()
try:
    print(next(result))
    print(next(result))
    print(next(result))
    print(next(result))
except StopIteration as e:
    print(e, '++')
