# python按文件后缀整理文件夹

# ●小知识:怎样获取文件的后缀名?
# import Os
# os . path.splitext( '/path/to/aaa.mp3' )
# 输出: ( '/path/to/aaa','.mp3' )
# ●小知识:怎样移动文件
# import shutil
# shutil.move ("aaa.txt", "dir/bbb.foo" )


import os
import shutil

dir = "arrange_dir"

for file in os.listdir(dir):
    ext = os.path.splitext(file)[1]
    ext = ext[1:]
    # 根据后缀名创建文件夹
    if not os.path.isdir(f"{dir}/{ext}"):
        os.mkdir(f"{dir}/{ext}")
    source_path = f"{dir}/{file}"
    target_path = f"{dir}/{ext}/{file}"
    shutil.copy(source_path, target_path)

    print(file, ext)
