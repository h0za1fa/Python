import random
print('Welcome to treassure hunt!')
list1=['o','o','o']
list2=['o','o','o']
list3=['o','o','o']
map=[list1,list2,list3]
print(f'{list1} \n {list2} \n {list3}')
tries=0

def colpos(list, colmn):
    cell=list[colmn]
    return cell

def jackpot(inpu,tressure,listg,colmn):
    if inpu==tressure:
        win="You win!"
        listg[colmn]='!'
    else:
        win=''

    return win

rows=['a','b','c']
cols=[1,2,3]
tres_row=random.choice(rows)
tres_cols=str(random.choice(cols))
tressure=tres_row+tres_cols
while True:
    pos=input('Enter postion: ')
    row=pos[0].lower()
    colm=int(pos[1])
    if row not in ['a','b','c']:
        print('Worng input!')
        pos=input('renter postion: ')
    if colm>3 and colm<0:
        print('Worng input!')
        pos=input('renter postion: ')
    colmn=colm-1
    if row=='a':
        cell=colpos(list1,colmn)
        list1[colmn]='x'
        status=jackpot(pos,tressure,list1,colmn)
    elif row=='b':
        cell=colpos(list2,colmn)
        list2[colmn]='x'
        status=jackpot(pos,tressure,list2,colmn)
    elif row=='c':
        cell=colpos(list3,colmn)
        list3[colmn]='x'
        status=jackpot(pos,tressure,list3,colmn)
    print(f'{list1} \n {list2} \n {list3}')
    tries+=1
    if status=='You win!':
        break
print(status)    
print(f'You did it in {tries} tries')

