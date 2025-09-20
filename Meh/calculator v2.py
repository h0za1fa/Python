import re
exp=input('Enter expression: ')
num=[]

def find_char(st):
    ch=['+','-','*','/']
    for op in ch:
        match=re.search(re.escape(op),st)
        if match:
            return op, match.start()
    return None,-1

def find_digits(st):
    nums=[]
    for num in st:
        if num.isdigit():
            nums.append(int(num))
    return nums

def find_nums(lis,index,st):
    list=lis[::-1]
    num2=list[0]
    l=len(st)
    num1=list[index]
    for num in list[1:index:]:
        num2+=num*10
    for num in list[index+1::]:
        num1+=num*10
    return num1,num2

def calc(num1,num2,ope):
    if ope=='+':
        ans=num1+num2
    elif ope=='-':
        ans=num1-num2
    elif ope=='*':
        ans=num1*num2
    elif ope=='/':
        ans=num1/num2
    return ans

ope , pos =find_char(exp)
# print(ope,pos)
nums=find_digits(exp)
# print(nums)
num1,num2=find_nums(nums,pos,exp)
# print(num1,num2)
ans=calc(num1,num2,ope)
print(f'Awnser: {ans}')