# python给文章中手机号打马赛克效果

content = """
白日依19989881888山尽，黄河入45645546468798978海流。
欲穷12345千里目，更上15619292345一层楼。
"""

import re

pattern = r"(1[3-9])\d{9}"

# re是正则的表达式，sub是substitute表示替换
# re.sub是相对复杂点的替换
# re.sub(pattern, repl, string, count=0, flags=0)
#  \1代表第一个分组  \2代表第二个分组  从第一个分组开始 表达式中需要用小括号表示一个分组
print(re.sub(pattern, r"\1#########", content))
