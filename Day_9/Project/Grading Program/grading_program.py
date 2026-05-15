# Grading Program

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60,
}


# TODO: Convert their scores to Grades.
# TODO: Have a new dictionary containing names as keys and their assessed grades for values.

student_grades = {}

for students in student_scores:
    if 91 <= student_scores[students] <= 100:
        student_grades[students] = "Outstanding"
    elif 81 <= student_scores[students] <= 90:
        student_grades[students] = "Exceeds Expectations"
    elif 71 <= student_scores[students] <= 80:
        student_grades[students] = "Acceptable"
    else:
        student_grades[students] = "Fail"

print(student_grades)
