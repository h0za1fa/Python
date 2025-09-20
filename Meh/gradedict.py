student_marks={
    'harry': 81,
    'harmoine': 99,
    'ron': 78,
    'draco': 74,
    'Neville': 63,
}

student_grades={

}

for student in student_marks:
    if student_marks[student]>91:
        grade='Outstanding'
    elif student_marks[student]>81:
        grade='Excedes expectations'
    elif student_marks[student]>71:
        grade='Acceptable'
    else:
        grade='Fail'
    student_grades[student]=grade
print(student_grades)
    