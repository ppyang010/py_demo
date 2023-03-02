# python自动提取电子邮箱地址

content = """
白日依19989881888山尽644@qq.com,黄河入45645546468798978海流。
欲穷nonono#163.com千里目，996nanshou@163.com更上15619292345一层楼。
"""

import re

# re.VERBOSE 支持多行编译
patter = re.compile(r"""
    [a-zA-Z0-9_-]+
    @
    [a-zA-Z0-9_-]+
    \.
    [a-zA-Z]{2,4}
""", re.VERBOSE)


# pattern = r"[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?"



res = re.findall(patter, content)

print(len(res))
print(res)

