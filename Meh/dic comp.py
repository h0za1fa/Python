# import random as ran

# names = ['Alex','Beth','Caroline','Dave','Eleanor','Freddie']

# student_scores = {student:ran.randint(0,100) for student in names}

# passed_students = {students: scores for (students, scores) in student_scores.items() if scores > 50}

# print(student_scores)
# print(passed_students)

#--------------------------------------------------------------------------------------------------------------

# sentence = input().split()

# len_of_words = {word: len(word) for word in sentence }

# print(len_of_words)

#--------------------------------------------------------------------------------------------------------------

weather_c = {
    'Monday': 12,
    'Tuesday': 14,
    'Wednessday': 13,
    'Thursday': 18,
    'Friday': 13,
    'Saturday': 15,
    'Sunday': 20,
}

weather_f = {
    day: round((temp*(9/5)) + 32 , 1) for (day,temp) in weather_c.items()
}

print(weather_f)