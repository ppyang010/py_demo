# python 统计每个兴趣的学生数
# 数据结构 小A 篮球,羽毛球,乒乓球,台球,足球

# k = like  v = count
like_map = {}

with open("./student_like.txt", encoding="utf-8") as fin:
    for line in fin:
        line = line[:-1]
        name, likesStr = line.split(" ")
        likeList = likesStr.split(",")
        for like in likeList:
            if like not in like_map:
                like_map[like] = 0
            like_map[like] += 1

print(like_map)
