def find_leap_year(year):
    if year%100==0 and year%400==0 and year%100==0:
        return 'a leap year'
    else:
        return 'not leap year'

year=int(input('Enter year: '))
print(f'{year} is {find_leap_year(year)}')