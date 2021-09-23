student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
for key in student_scores:
    print(key)
student_grades = {}
for key in student_scores:
    marks = student_scores[key]
    print(marks)

    if marks >= 91 and marks <= 100:
        student_grades[key] = "Outstanding"
    elif marks >= 81 and marks <= 90:
        student_grades[key] = "Exceeds Expectation"
    elif marks >= 71 and marks <= 80:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"
print(student_grades)