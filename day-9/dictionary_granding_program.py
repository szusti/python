
def scores_to_grades(name, score):
    if 91 <= score <= 100:
        student_grades[name] = "Outstanding"
    elif 81 <= score <= 90:
        student_grades[name] = "Exceeds Expectations"
    elif 71 <= score <= 80:
        student_grades[name] = "Acceptable"
    else:
        student_grades[name] = "Fail"


students_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermiona": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for student_name in students_scores:
    scores_to_grades(student_name, students_scores[student_name])

print(student_grades)
