# 实现学生按成绩排序

# 复杂列表排序,元素是字典或者元组

# 字典
students = [
    {"sno": 101, "sname": "小张", "sgrade": 88},
    {"sno": 102, "sname": "小玩", "sgrade": 100},
    {"sno": 103, "sname": "小里", "sgrade": 77},
    {"sno": 104, "sname": "小赵", "sgrade": 66},
]

# students_sort = sorted(students, key=lambda x: x["sgrade"])
students_sort = sorted(students, key=lambda x: x["sgrade"], reverse=True)

print(students)
print(students_sort)
