import random

player_cards=[]
dealer_cards=[]

def play_game():
    result=False
    while result == False:
        # deal 2 cards to player and 1 to dealer
        for n in range (2):
            player_cards.append(deal_card())
        dealer_cards.append(deal_card())
        result=blackjack(player_cards)
        # display decks an write score
        cards_and_score(player_cards,dealer_cards)
        # hit or stand
        hit_or_stand=input('Do you want to hit(i) or stand(o): ')
        # hit
        if hit_or_stand == 'i':
            result = hit(player_cards)
            result=blackjack(player_cards)
        # stand
        elif hit_or_stand == 'o':
            stand(player_cards,dealer_cards)
            result=True
        # if result declared break the loop
        if result == True:
            break

def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

def cards_and_score(player,dealer):
    print(f'Your cards are {player} Score: {sum(player)}')
    print(f'Dealers cards are {dealer} Score: {sum(dealer)}')

def hit(player):
    player.append(deal_card())
    print(f'Your cards are {player} Score: {sum(player)}')
    result = False
    if sum(player) > 21:
        print('Bust, You lose!')
        result = True
    return result

def ace_change(cards):
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)

def blackjack(cards):
    result=False
    if sum(cards) == 21:
        print('Blackjack!! \nYou win!')
        result=True

def stand(player,dealer):
    # if Ace is present
    ace_change(player)
    # if the dealer is less than 17
    while 17 > sum (dealer):
        dealer.append(deal_card())
        ace_change(dealer)
    print(f'Dealers cards are {dealer} Score: {sum(dealer)}')
    # win or loose
    if 21 < sum (dealer):
        print('You win, the dealer bust')
    elif sum(player) > sum (dealer):
        print('You win')
    elif sum(player) < sum (dealer):
        print('You lose')
    elif sum(player) == sum (dealer):
        print('You draw')
    result = True

while True:
    play_game()
    print('--------------------------------------------------------')
    wanna_play=input('Do you wanna play again?\n')
    player_cards=[]
    dealer_cards=[]
    if wanna_play == 'no':
        break