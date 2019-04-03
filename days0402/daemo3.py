"""
斐波拉契算法
"""


def f(times):
    a, b = 0, 1
    yield a
    yield b
    count = 0
    print('a-------------------', a)
    print('b-------------------', b)
    while count < times:

        a, b = b, a+b
        print('a+++++++++++++++++++', a)
        print('b+++++++++++++++++++', b)
        yield b
        count += 1


result = f(10)
for i in result:
    print(i)
