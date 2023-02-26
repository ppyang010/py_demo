# python 读取成绩文件实现排序
# 根据成绩降序排序


def read_file():
    result = []
    # with open as 是try final + io.close的语法糖  类似java try with resources
    # https://blog.csdn.net/xrinosvip/article/details/82019844
    with open("./student_grade_input.txt", "r", encoding="utf-8") as f:
        for line in f:
            # line[:-1]其实就是去除了这行文本的最后一个字符（换行符）后剩下的部分
            line = line[:-1]
            result.append(line.split(","))
    return result


def sort_data(datas):
    # key reverse 这几个在Pycharm中显示红色只是因为主题中这个位置的配色是这个  后续修改为7F4E4E
    # 参考文档 https://juejin.cn/post/7017672330570629134
    return sorted(datas, key=lambda x: int(x[2]), reverse=True)


def write_file(datas):
    with open("./student_grade_output.txt", "w", encoding="utf-8") as fOut:
        for data in datas:
            fOut.write(",".join(data) + "\n")


# 读取文件

datas = read_file()
print(datas)

# 排序数据
datas = sort_data(datas)
print(datas)

# 写入新文件
write_file(datas)
