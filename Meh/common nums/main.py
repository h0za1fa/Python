file1 = open('common nums/file1.txt')
file2 = open('common nums/file2.txt')

list_1 = [int(nums) for nums in file1.readlines() if nums != '\n' ]
list_2 = [int(nums) for nums in file2.readlines() if nums != '\n' ]

file1.close()
file2.close()

result = [nums for nums in list_1 if nums in list_2]

print(result)