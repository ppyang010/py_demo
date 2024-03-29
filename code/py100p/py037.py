#python 实现中文文章分词

content = """
山谷中，虫鸣声在我耳边回响，令我的心绪格外宁静。端坐树旁，望着天空，皎洁的明月，在彩云中时沉时浮，给我带来无限的遐想。月光照耀着大地，如水般流淌，让我想到了一瞬即逝的时光。岁月的沟壑蜿蜒在绿色的土地上，时间的箫声逡巡在美丽的夜空中。不知不觉中，我度过了十一个中秋，时光稍纵即逝。
举头望月，低首静思，我轻闭双眸，攥紧拳头，对自己说：要继续努力，不断前进。此时，我还只是一株稚嫩的幼苗，但是只要坚韧不拔，终会成长为参天大树；此刻，我只是涓涓细流，但是只要锲而不舍，终会拥抱大海；今夜，我虽是一只雏鹰，但是只要心存志远，终会翱翔蓝天！
"""

import jieba
import re

# 替换标点符号
content = re.sub(r"[\s.()-?]+", "", content)
word_list = jieba.cut(content)

print(list(word_list))
