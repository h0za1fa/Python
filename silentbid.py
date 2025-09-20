import os
from art import logogavel

bids=[]
    
def highest_bid(bids):
    bid_list=[]
    name_list=[]
    for n in range (0,len(bids)):
        bid_dict=bids[n]
        name_dict=bids[n]
        bid=bid_dict['bid']
        name=name_dict['Name']
        bid_list.append(bid)
        name_list.append(name)
    highest=max(bid_list)
    name_highest=name_list[bid_list.index(highest)]
    return highest , name_highest


def take_bid(name,bid):
    bids={}
    bids['Name']=name
    bids['bid']=bid
    return bids

print(logogavel)

while True:
    name=input('Enter name: ')
    bid=int(input('Enter bid: $'))
    bids.append(take_bid(name,bid))
    # print(bids)
    choice=input('Do you want to continue: ')
    if choice == 'no':
        highest_bid , highest_name = highest_bid (bids)
        print(f'The highest bid is {highest_bid} from {highest_name}')
        break
    else:
        os.system('cls' if os.name == 'posix' else 'clear')
