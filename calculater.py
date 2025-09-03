num1=int(input('Enter Num1: '))
while True:
    op=input('Operator (+ , - , * , /): ')
    if op not in ['+','-','*','/']:
        print('Wrong operator')
        continue
    else:
        break
num2=int(input('Enter Num2: '))
if op=='+':
    print(f'sum is {num1+num2}')
if op=='-':
    print(f'Diff is {num1-num2}')
if op=='*':
    print(f'prod is {num1*num2}')
if op=='/':
    print(f'quotient is {num1/num2}')


