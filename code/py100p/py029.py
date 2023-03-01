# python怎样从文本中提取手机号码

content = """
白日依19989881888山尽，黄河入45645546468798978海流。
欲穷12345千里目，更上15619292345一层楼。
"""

# 手机号的模式  1开头  11位  第二位3-9

import re

pattern = r"1[3-9]\d{9}"

res = re.findall(pattern, content)

print(len(res))
print(res)
