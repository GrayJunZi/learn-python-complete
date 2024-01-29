student_heights = input("Input a list of student height ").split()

total = 0
for height in student_heights:
    total += int(height)

average = total / len(student_heights)
print(average)
