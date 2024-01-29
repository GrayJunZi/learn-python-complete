student_scores = input("Input a student score ").split()

high = int(student_scores[0])
for score in student_scores:
    s = int(score)
    if s > high:
        high = s

print(high)
