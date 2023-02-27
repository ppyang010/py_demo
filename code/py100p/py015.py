# python统计目录下的文件大小

import os

print(os.path.getsize("student_grade_input.txt"))

size_sum = 0
for file in os.listdir("."):
    # 判断是不是文件  过滤掉文件夹
    if os.path.isfile(file):
        print(file)
        size_sum += os.path.getsize(file)

print(size_sum/1024)