MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# be able to check resources
# when order is placed fetch all the details
# subtract the used materials from resources

balance=0

def fetch_details(order,resources):
    order_dict=MENU[order]
    order_ing=order_dict['ingredients']
    order_cost=order_dict['cost']
    return order_ing,order_cost

def check_resourse(resources,ingredients):
    resource_unavailable=[]
    availability='sufficient'
    for n in ['water','milk','coffee']:
        if resources[n]<ingredients[n]:
            availability='insufficient'
            resource_unavailable.append(n)
    return availability, resource_unavailable
        
def use_resources(resources,ingredients):
    for n in ['water','milk','coffee']:
        resources[n]=resources[n]-ingredients[n]
    return resources

def display_unavailable_resources(resource_unavailable):
    disp=''
    if len(resource_unavailable)>1:
        for res in resource_unavailable:
            disp+=res+' and '
        disp=disp[:-3]
    else:
        for res in resource_unavailable:
            disp+=res
    return disp

def payment_verification(cost,payment):
    change=0
    if cost > payment:
        verified = False
    elif cost == payment:
        verified = True
    elif cost < payment:
        verified = True
    change=payment-cost
    return verified,change

def process_payment(coin):
    coin_det=coin.split()
    num_of_coins=int(coin_det[0])
    coin_type=coin_det[1]
    coin_dict={
    'quarters': 0.25,
    'dimes': 0.10,
    'nickles': 0.05,
    'pennies': 0.01,  
    }
    payment=num_of_coins*coin_dict[coin_type]
    return payment
   
def display_report(resources):
    for res in resources:
        print(f'{res}: {resources[res]}')
        
def order_placed(order,MENU,resources):
    balance=0
    
    # fetch details of tehe order
    ingredients,cost=fetch_details(order,resources)
    
    # check resources
    availabilty, resource_unavailable=check_resourse(resources,ingredients)
    if availabilty=='insufficient':
        print(f'Sorry we are out of {display_unavailable_resources(resource_unavailable)}')
    # use up the resources
    else:
        resources=use_resources(resources,ingredients)
    print(resources)
        
    # display cost and ask payment
    print(f'That would be ${cost}')
    verified = False
    while verified == False:
        coin=input('quarters = $0.25\ndimes = $0.10\nnickles = $0.05\npennies = $0.01\nPlease insert coin:\n')
        payment = process_payment(coin)
        print(f'Balance: ${round(payment,2)}')
    
    # verify the payment
        verified,change=payment_verification(cost,payment)
        if verified == False:
            print(f'Insufficent amount')
        elif verified == True:
            print(f'Thank You! Here is your change ${change}')
            
            # order completed
            print(f'Here enjoy your {order}')
        balance+=balance
        
while True:
    
    # place order
    order=input('What would you like? (espresso/latte/cappuccino): ').lower()
    
    # display resources
    if order == 'report':
        display_report(resources)
    # power off
    elif order == 'off':
        break
    else:
        order_placed(order,MENU,resources)
    
