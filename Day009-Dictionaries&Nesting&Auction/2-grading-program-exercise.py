student_scores = {
    "Harry":81,
    "Ron":78,
    "Hermione":99,
    "Draco":74,
    "Neville":62,
}

# 创建名叫 student_grades 的空字典
student_grades = {}

# 添加等级到 student_grades 字典中
for student in student_scores:
    scores = student_scores[student]
    if scores > 90:
        student_grades[student] = "Outstanding"
    elif scores > 80:
        student_grades[student] = "Exceeds Expections"
    elif scores > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)