"""
用列表生成器，节省内存
"""
import sys

# 列表
list1 = [x for x in range(10)]
print(list1, type(list1))
print(sys.getsizeof(list1))

# 列表生成器
list2 = (x for x in range(10))
print(list2, type(list2))
print(sys.getsizeof(list2))

# 使用for循环遍历生成器
# for i in list2:
#     print(i)

# 使用next获取元素
# print(next(list2))
# print(next(list2))
# print(next(list2))
# print(next(list2))

while True:
    try:
        print(list2.__next__())
    except Exception as e:
        print('异常')
        break

