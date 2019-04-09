"""
表示数量
"""
import re

# * 匹配前一个字符出现0次或多次
# result = re.findall('hi*', 'hi china hello china')
# print(result)

# + 匹配前一个字符出现1次或多次
# result = re.findall('hi+', 'hi china hello chiina')
# print(result)

# ? 匹配前一个字符出现0次或1次
# result = re.findall('hi?', 'hi china hello chiina')
# print(result)

# {m} 匹配前一个字符出现m次
# result = re.findall('hi{2}', 'hi china hello chiiina')
# print(result)

# {m,} 匹配前一个字符最少出现m次
# result = re.findall('hi{1,}', 'hi china hello chiina')
# print(result)

# {m,n} 匹配前一个字符出现从m到n次
# result = re.findall('hi{2,3}', 'hi china hello chiiina')
# print(result)

# 正则匹配默认贪婪模式即匹配尽可能多个字符
# result = re.findall('he*', 'h hee heeeee zzheee0')
# print(result)

# 当？出现在+、？、*、{m}之后开启非贪婪模式
# result = re.findall('he*?', 'h he heeeee')
# print(result)
