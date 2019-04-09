"""
单个字符
"""
import re
# result = re.findall('.', 'hello \n china')   # 默认不匹配换行符
# print(result)
# result = re.findall('.', 'hello \n china', flags=re.S)   # 单行模式匹配换行符
# print(result)

# 匹配[]中列举的字符
# result = re.findall('[0123].ello', '0hello 1hello 5 ello 88ello')
# print(result)

# \d 匹配数字，0-9
# result = re.findall('\dhello', 'hello 1hello 5hello 0hello')
# print(result)

# 匹配非数字，包括空格
# result = re.findall('\Dhello', 'hello xhello 1hello hello')
# print(result)

# 匹配空白，空格·tab键
# result = re.findall('\shello', 'hello hello hello')
# print(result)

# 匹配非空白
# result = re.findall('\Shello', '1hello hello    hello')
# print(result)

# 匹配单词字符
# result = re.findall('\wello', 'hello aello5ello_ello .ello ^ello')
# print(result)

# 匹配非单词字符
result = re.findall('\Wello', 'hello aello5ello_ello .ello ^ello')
print(result)
