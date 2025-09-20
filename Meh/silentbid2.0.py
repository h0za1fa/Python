import os
from art import logogavel

def highest_bid(bids_dict):
    
    highest_bid=0

    for bid_increment in bids_dict:
        if bids_dict[bid_increment] > highest_bid:
            highest_bid=bids_dict[bid_increment]
            highest_bidder=bid_increment
        
    print(f'The highest bidder is {highest_bidder} with ${highest_bid}')

bids_dict={}

print(logogavel)

while True:
    name=input('Enter name: ')
    bid=int(input('Enter bid: $'))

    bids_dict[name]=bid
    
    # print(bids_dict)

    choice=input('Any other bidders? ')

    if choice=='no':
        highest_bid(bids_dict)
        break
    else:
        os.system('clear' if os.name == 'posix' else 'cls')

    