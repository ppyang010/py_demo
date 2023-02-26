# 读取成绩文件 计算最高分 最低分 平均分

def compute_score():
    with open("./student_grade_input.txt", "r", encoding="utf-8") as fIn:
        scores = []
        for line in fIn:
            line = line[:-1]
            fields = line.split(",")
            scores.append(int(fields[-1]))
    max_score = max(scores)
    min_score = min(scores)
    avg_score = round(sum(scores) / len(scores), 2)
    return max_score, min_score, avg_score


max_score, min_score, avg_score = compute_score()

print(f"{max_score}, {min_score}, {avg_score}")
