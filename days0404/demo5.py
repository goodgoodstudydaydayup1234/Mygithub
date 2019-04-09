"""
表示边界
"""
import re

# ^ 匹配字符串开头
# result = re.findall('^hello', r'hello world \nhello zhengzhou', re.M)
# print(result)

# $ 匹配字符串结尾
# result = re.findall('zhengzhou$', 'hello worldzhengzhou\n hello zhengzhou', re.M)
# print(result)

# \b 匹配一个单词的边界
# result = re.findall(r'\bhello\b', 'hello world hello zhengzhou sayhellook')
# print(result)

# \B 匹配非单词边界
# result = re.findall(r'\Bhello\B', 'hello world chellok')
# print(result)

result = re.findall(r'\bhello\B', 'hello helloworld')
print(result)