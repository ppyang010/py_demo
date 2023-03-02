# python验证用户密码是否规范
"""
写一个函数，验证密码是否满足条件
1. 长度位于[6，20]之间
2. 必须包含至少1个小写字母
3. 必须包含至少1个大写字母
4. 必须包含至少1个数字
5. 必须包含至少1个特殊字符
返回
True None
或者 False，原因
"""

import re


def check_password(password):
    if not 6 <= len(password) <= 20:
        return False, "长度位于[6，20]之间"
    if not re.findall(r"[a-z]", password):
        return False, "必须包含至少1个小写字母"
    if not re.findall(r"[A-Z]", password):
        return False, "必须包含至少1个大写字母"
    if not re.findall(r"[0-9]", password):
        return False, "必须包至少1个数字"
    if not re.findall(r"[^0-9a-zA-Z]", password):
        return False, "必须包含至少1个特殊字符"
    return True, None


print(check_password("123*abcAAA"))
print(check_password("123abcAAA"))
print(check_password("123*abc"))
