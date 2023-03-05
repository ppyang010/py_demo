# python实现英文分词计算词频

import re

content = ""

with open("./txt/Beginner’s Guide To Python.txt", encoding="utf-8") as fin:
    content = fin.read()

words = re.split(r"[\s.()-?]+", content)
print(words)

import pandas as pd

# pandas是 Python 的核⼼数据分析⽀持库，提供了快速、灵活、明确的数据结构，旨在简单、直观地处理关系型、标记型数据。pandas是Python进⾏数据分析的必备⾼级⼯具。
# https://www.cnblogs.com/t-dashuai/p/15404501.html

# print(pd.Series(words).value_counts())
# 取前20
print(pd.Series(words).value_counts()[:20])
