"""
正则表达式，RE模块
"""
import re
s1 = 'hellodfdsf'
# math方法，从头开始匹配，返回none或者匹配到的第一个match对象
# result = re.match('h', s1)
# search方法，扫描整个字符串，返回none或者匹配到的第一个match对象
# result = re.search('l', s1)
# fullmatch方法，匹配整个字符串，返回none或者匹配到的match对象
# result = re.fullmatch('hello', s1)
# findall方法，返回列表
# result = re.findall('l', s1)
# split方法返回分割列表
# result = re.split('o', s1)
# sub方法返回字符串
# result = re.sub('ll', '999', s1)
# finditer返回迭代器，迭代器里对象存储类型是match
result = re.finditer('l', s1)
if result:
    if isinstance(result, list):
        for i in result:
            print(i)
    elif isinstance(result, str):
        print(result, type(result))
    else:
        print(result, type(result))
        print(next(result))
# print(result)

# re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# print(re_telephone.match('010-12345678').group())
# print(re_telephone.match('010-8089').group())





