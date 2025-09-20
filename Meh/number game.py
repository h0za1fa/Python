import random
num=list(range(1,101))
cr=random.choice(num)
count=0
for i in range(5):
    usr=int(input('Enter Number: '))
    if usr==cr:
        print('You win!')
        break
    elif usr>cr:
        print('Lower')
    elif usr<cr:
        print('Higher')
    count+=1

if usr!=cr:
    print(f'The number was {cr}, try again!')
else:
    print(f'You did it in {count} tries!')