
num=int(input('Enter number: '))

def prime(num):
    for i in range (2,num):
        if num in [2,3,5,7]:
            status='prime'
        elif num/i > int(num/i):
            status='not prime'
        else:
            status='prime'
    return status

print(f'{num} is {prime(num)}')