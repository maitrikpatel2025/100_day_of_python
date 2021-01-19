student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆


# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
for key in student_scores:
    print(key)
    print(f"{student_scores[key]}")
    if int(student_scores[key]) in range(91, 101):
        student_grades[key] = "Outstanding"
    if int(student_scores[key]) in range(81, 91):
        student_grades[key] = "Exceeds Expectations"
    if int(student_scores[key]) in range(71, 81):
        student_grades[key] = "Acceptable"
    if int(student_scores[key]) in range(0, 71):
        student_grades[key] = "Fail"
# TODO-2: Write your code below to add the grades to student_grades.👇


# 🚨 Don't change the code below 👇
print(student_grades)
