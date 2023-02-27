# 读取成绩文件student_course_grade_input.txt  计算每门课的 最高分 最低分 平均分
# py013.py


# 字典接受
# key course val= 分数数组
course_grades = {}

with open("./student_course_grade_input.txt", encoding="utf-8") as fIn:
    for line in fIn:
        # 跳过空行
        if (len(line) <= 1):
            continue
        # 截断最后一位\n
        line = line[:-1]
        course, sno, sname, grade = line.split(",")
        if (course not in course_grades):
            course_grades[course] = []
        course_grades[course].append(int(grade))

print(course_grades)

for course, grades in course_grades.items():
    print(
        course,
        max(grades),
        min(grades),
        round(sum(grades) / len(grades), 2)
    )
