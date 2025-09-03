import random
num=list(range(1,101))
cr=random.choice(num)
while True:
    usr=int(input('Enter Number: '))
    if usr==cr:
        print('You win!')
        break
    elif usr>cr:
        print('Lower')
    elif usr<cr:
        print('Higher')
    try+=1
print(f'You did it in {try} tries!')