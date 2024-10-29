#input students score
students_score = input().split()
for i in range(0, len(students_score)):
    students_score[i] = int(students_score[i])

highest_score = 0
for score in students_score:
    if score >= highest_score:
        highest_score = score

print("The highest student score is ", highest_score)
               
