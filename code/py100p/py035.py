# python进行多种日期格式的标准化


content = """
白日依2023/03/03山尽，黄河入2023.03.03海流。
欲穷03-01-2023千里目，更上03/29/2023一层楼。
"""

import re

# \1代表第一个分组 \2代表第二个分组 从第一个分组开始
# 正则表达式中需要用小括号表示一个分组
content = re.sub(r"(\d{4})/(\d{2})/(\d{2})", r"\1-\2-\3", content)
print(content)

content = re.sub(r"(\d{4})\.(\d{2})\.(\d{2})", r"\1-\2-\3", content)
print(content)

content = re.sub(r"(\d{2})-(\d{2})-(\d{4})", r"\3-\1-\2", content)
print(content)

content = re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\3-\1-\2", content)
print(content)
