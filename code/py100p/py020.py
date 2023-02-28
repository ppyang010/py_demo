# python实现批量txt文件合并

# 小知识: Python读取文件的两个方法
# 方法1:按行读取
# for line in fin
# 方法2: -次读取所有内容到一个字符串
# content = fin.read()


import os

data_dir = "./datas/many_texts"

contents = []
for file in os.listdir(data_dir):
    file_path = f"{data_dir}/{file}"
    if os.path.isfile(file_path) and file.endswith(".txt"):
        print(file_path)
        with open(file_path, encoding="utf-8") as fin:
            contents.append(fin.read())

print(contents)
final_content = "\n".join(contents)

with open("./datas/many_texts_out.txt", mode="w", encoding="utf-8") as fout:
    fout.write(final_content)
