import random
value={'R':1,'P':2,'S':3}
choice={'R':'Rock','P':'Paper','S':'Scissor'}
win=0
draw=0
lose=0
while True:
    user=input('Rock Paper or Scissors (R/P/S): ')
    user1=user.capitalize()
    comp=['R','P','S']
    comp1=random.choice(comp)
    # comp1='P'
    U1=value[user1]
    C1=value[comp1]
    user2=choice[user1]
    comp2=choice[comp1]
    print(f'You chose {user2}')
    print(f'Computer chose {comp2}')
    if C1==U1:
        res='draw'
    elif C1>U1 and U1!=3:
        res='lose'
    elif C1<U1 and C1!=3:
        res='win'
    elif user1=='S':
        res='lose'
    elif comp1=='S':
        res='win'
    else:
        print('error')
        res='gg'
    print(f'You {res}')
    if res=='win':
        win+=1
    elif res=='draw':
        draw+=1
    elif res=='lose':
        lose+=1
    print(f'{win}/{draw}/{lose}')
    t=input('Play again(Y/N): ')
    tr=t.capitalize()
    if tr=='N':
        break
print(f'Final result is: {win}/{draw}/{lose}')


