# python统计小说中的人名

# posseg 提供词性标注 例如 人名 动词 等标签
import jieba.posseg as posseg

# content = "李明喜欢韩梅梅,他两早恋了"
#
# words = posseg.cut(content)  # jieba默认模式
#
# for word, flag in words:
#     print('%s %s' % (word, flag))

content = ""
with open("txt/ludingji.txt", encoding="utf-8") as fin:
    content = fin.read()

words = posseg.cut(content)

name_list = []
for word, flag in words:
    if flag == "nr":
        name_list.append(word)

import pandas as pd

print(pd.Series(name_list).value_counts()[:20])
