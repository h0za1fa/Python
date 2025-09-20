weight=int(input('Enter weight: '))
hieght=float(input('Enter hieght: '))
bmi=round(weight/hieght**2,2)
print(f'Your BMI is {bmi}') 
if bmi<18.5:
    status='Under weight'
elif bmi<25:
    status='Normal weight'
elif bmi<30:
    status='Slightly overweight'
elif bmi<35:
    status='Obese'
else:
    status='Clinicaly Obese'
print(f'You are {status}')