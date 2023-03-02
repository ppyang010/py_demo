# python批量提取网页上的手机号码

import re

content = ""

with open("./txt/webpage_phone_number.txt", encoding="utf-8") as fin:
    content = fin.read()

pattern = r"1[3-9]\d{9}"
res = re.findall(pattern, content)

print(len(res))
print(res)
