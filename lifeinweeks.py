def find_weeks(years) -> int :
    weeks=int((years*365)/7)
    return weeks
age=int(input('Enter your age: '))
age_weeks=find_weeks(age)
total_weeks=find_weeks(90)
left_weeks=total_weeks-age_weeks
print(f'You have only {left_weeks} left!')