print('Welcome to python pizza! ')
size=input('What size do you want (s,m,l): ')
peparo=input('Do you want peparoni(Y/N): ')
cheez=input('Do you want extra cheese(Y/N): ')
peparo=peparo.capitalize()
cheez=cheez.capitalize()
price={'s': 10 , 'm': 12 , 'l': 15}
sizprice=price[size]
if peparo == 'Y':
    sizprice+=3
if cheez == 'Y':
    sizprice+=5


print(f'Total is {sizprice}')


