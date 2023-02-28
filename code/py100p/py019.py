# 实现不同文件关联
#  course_teacher.txt -> 数学,老师


course_teacher_map = {}
with open("./datas/course_teacher.txt", encoding="utf-8") as fin:
    for line in fin:
        line = line[:-1]
        course, teacher = line.split(",")
        course_teacher_map[course] = teacher

print(course_teacher_map)

with open("./student_course_grade_input.txt", encoding="utf-8") as fin:
    for line in fin:
        if (len(line) <= 1):
            continue
        line = line[:-1]
        course, sno, sname, grade = line.split(",")
        teacher = course_teacher_map.get(course)
        print(f"{teacher},{course},{sno},{sname},{grade}")
