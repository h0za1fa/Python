# name = 'hozaifa'
# new_list = [letter for letter in name]
# print(new_list)

# new_list = [ n*2 for n in range (1,5) ]
# print(new_list)

# names = ['Alex','Beth','Caroline','Dave','Eleanor','Freddie']
# name_list = [name.upper() for name in names if len(name) >= 5]
# print(name_list)

# numbers = [1 ,1 ,2 ,3 ,5 ,8 ,13 ,21 ,34 ,55]
# squared_numbers = [n*n for n in numbers]
# print(squared_numbers)

list_of_strings = input().split(',')

list_of_numbers = [int(number) for number in list_of_strings]
result = [nums for nums in list_of_numbers if nums%2==0]

print(result)