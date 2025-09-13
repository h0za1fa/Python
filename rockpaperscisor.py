import random
def random_() -> str :
    rps=['R','P','S']
    com=random.choice(rps)
    return com
# print(com)
# print(user)
wi=dr=lo=0
def res(user, comp) -> str:
    if user not in ('R','P','S'):
        print('Wrong input!')
    elif user == comp:
        result = 'Draw'
    elif (user, comp) in [('R', 'S'), ('S', 'P'), ('P', 'R')]:
        result = 'Win'
    else:
        result = 'lose'
    return result

def score_(res,w,d,l) -> int:
    if res=='Win':
        w=w+1
    elif res=='Draw':
        d=d+1
    elif res=='lose':
        l=l+1
    return w,d,l

while True:
    com=random_()
    user=input('choose your hand(R/P/S): ')
    if user=='stop':
        break
    user=user.capitalize()
    result = res(user, com)
    print(f"Computer chose: {com} \n\nyou {result}!")
    wi,dr,lo=score_(result,wi,dr,lo)
    print(f'{wi}/{dr}/{lo}')
