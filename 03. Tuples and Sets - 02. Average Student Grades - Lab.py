# 02. Average Student Grades:
student_count = int(input())
data = {}

for i in range(student_count):
    command = tuple(input().split())
    student, grade = command

    if student not in data:
        data[student] = []
    data[student].append(float(grade))


for key, value in data.items():
    sum_values = 0
    for i in value:
        sum_values += float(i)
    average = sum_values / len(value)
    student_result = ""
    for j in value:
        mark = f"{float(j):.2f} "
        student_result += mark
    print(f"{key} -> {student_result}(avg: {average:.2f})")