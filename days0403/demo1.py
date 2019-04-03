"""
一般意义的复制以及深浅拷贝
"""

# 一般意义的等号相当于引用，原始队列改变，被赋值的队列也会做出改变
# list1 = [1, 2, 3, 4, [5, 6]]
# list2 = list1
# print(list1 is list2)
# list1.insert(2, 10)
# print(list1, list2)
# print(list1[2] is list2[2])
# print(id(list1))
# print(id(list2))


# 浅拷贝
# 外层是拷贝值，原始队列外层改变，拷贝队列外层不会改变
# 内层是拷贝引用，原始队列的内层改变，拷贝队列内层会改变
# import copy
# list1 = [1, 2, 3, 4, [5, 6]]
# list2 =copy.copy(list1)
# print(list1 is list2)
# print(list1[1] is list2[1])
# print(list1[4] is list2[4])
# print(list2[4])
# list1.insert(2,10)
# print(list1, list2)
# list1[4].insert(1, 10)
# print(list1, list2)


# 深拷贝，内层拷贝和外层拷贝都是值拷贝，原始队列改变，拷贝队列不会改变
# import copy
# list1 = [1, 2, 3, 4, [5, 6]]
# list2 = copy.deepcopy(list1)
# print(list1 is list2)
# list1.insert(1,10)
# print(list1,list2)
# list1[4].insert(1,10)
# print(list1,list2)
