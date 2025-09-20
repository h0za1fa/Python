def pp(stud, mark, result):
    return f'{stud} with {mark} marks has {result} his exam'

students = []

# Get first student
name = input("Enter student name: ")
marks = int(input("Enter student marks: "))
student = {
    'name': name,
    'marks': marks,
    'result': 'passed' if marks >= 40 else 'failed'
}
students.append(student)

# Ask for more students
while True:
    key = input("Do you want to add more students? (y/n): ").lower()
    if key == 'n':
        break
    
    name = input("Enter student name: ")
    marks = int(input("Enter student marks: "))
    
    student = {
        'name': name,
        'marks': marks,
        'result': 'passed' if marks >= 40 else 'failed'
    }
    students.append(student)

# Print all students
print("\nStudent Results:")
for student in students:
    print(pp(student['name'], student['marks'], student['result']))
