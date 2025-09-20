import random

cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
dealers_hand=[]
players_hand=[]

def random_card(cards):
    return random.choice(cards)

def score(hand):
    return sum(hand)

def win_or_lose(player,dealer):
    if player > dealer:
        print('You win!')
    elif dealer > player:
        print('You lose :(') 
    else:
        print('Draw')
    print('--------------------------')   

def ace_switch(hand):
    if sum(hand) > 21:
        if 11 in hand:
            index_11=hand.index(11)
            hand[index_11]=1
    return hand

continuence=True
while continuence==True:
    choice=input('Do you want to play? \n')
    if choice == 'no':
        continuence=False
        break
    else:
        dealers_hand=[]
        players_hand=[]
    for n in range (0,2):
        players_hand.append(random_card(cards))
    dealers_hand.append(random_card(cards))
    print(f'Your hand is {players_hand}   score: {score(players_hand)} \n ')
    print(f'Dealers hand is {dealers_hand}   score: {score(dealers_hand)} \n ')
    
    stand = False
    while stand == False:
        if score(players_hand) > 21:
            print('Bust! you lose')
            break
        hold_hit=input('Hit(i) or stand(o) \n')

        if hold_hit == 'o':     #stand
            print('Stand! ')
            dealers_hand.append(random_card(cards))
            while True:
                if score(dealers_hand) < 17:
                    print(f'Dealers hand is {dealers_hand}   score: {score(dealers_hand)}')
                    dealers_hand.append(random_card(cards))
                else:
                    break
            if score(dealers_hand) > 21:
                print('You win! The dealer bust')
            print(f'Dealers hand is {dealers_hand}   score: {score(dealers_hand)}')
            ace_switch(players_hand)
            ace_switch(dealers_hand)
            win_or_lose(score(players_hand),score(dealers_hand))
            stand=True
            break

        elif hold_hit == 'i':   #hit
            print('Hit! ')
            players_hand.append(random_card(cards))
            print(f'Your hand is {players_hand}   score: {score(players_hand)} \n ')
            print(f'Dealers hand is {dealers_hand}   score: {score(dealers_hand)} \n ')

