"""
练习
"""

import requests
import re


response = requests.get('http://quote.stockstar.com/stock/ranklist_a_3_1_1.html')
# print(response.text)

result = re.search(r'<tbody.*?>(.*?)</tbody>', response.text, re.S)
# print(result)
result = re.findall(r'<tr>(.*?)<tr>', result.group(1))
for r in result:
    # print(type(r), r)
    r1 = re.findall(r'<td.*?>(.*?)</td>', r)
    print(r1[0])
    # r2 = re.findall(r'')


