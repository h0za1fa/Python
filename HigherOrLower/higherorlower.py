from game_data import data
from random import randint
import os
import art

#display name and disc of th two entities
def name_and_disc(data):
    index_var=randint(0,len(data)-1)
    detail_dict=data[index_var]
    return detail_dict

#ask for higher or lower
def higher_or_lower(again,higher_dict):
    if again == False:
        A_dict=name_and_disc(data)
    else:
        A_dict=higher_dict
    B_dict=name_and_disc(data)
    print(f'Compare A: {A_dict['name']} a {A_dict['description']} from {A_dict['country']}')
    print(art.vs)
    print(f'Against B: {B_dict['name']} a {B_dict['description']} from {B_dict['country']}')
    ans=input('A or B Who is higher??? ').upper()
    return ans,A_dict,B_dict,

#verify awnsera
def verify(ans,A_dict,B_dict):
    higher_dict={}
    if ans=='A' and A_dict['follower_count'] > B_dict['follower_count']:
        result='right!'
        higher_dict=A_dict
    elif ans=='B' and A_dict['follower_count'] < B_dict['follower_count']:
        result='right!'
        higher_dict=B_dict
    else:
        result='wrong!'
    return result,higher_dict

#if correct add a point and restart
#else display score and end
def play_game():
    print(art.logo)
    points=0
    again=False
    higher_dict={}
    while True:
        
        ans,A_foll,B_foll=higher_or_lower(again,higher_dict)
        result,higher_dict=verify(ans,A_foll,B_foll)
        if result == 'right!':
            again=True
            points+=1
            os.system('clear' if os.name=='posix' else 'cls' )
            print(art.logo)
            print(f'Your {result}\nPoints: {points}')
        else:
            lost=True
            again=False
            os.system('clear' if os.name=='posix' else 'cls' )
            print(art.logo)
            print(f'Your {result}\nPoints: {points}')
            return lost
while True:
    lost=play_game()
    if lost == True:
        break