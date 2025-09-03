# Take 5 input in a list
moj = []
even = []
odd = []
for i in range(1, 6):
    num = int(input(f"{i}. "))
    moj.append(num)

for nums in moj:
    if nums % 2 == 0:
        even.append(nums)
    else:
        odd.append(nums)

print(f"All numbers are {moj}")
print(f"Even numbers are {even}")
print(f"Odd numbers are {odd}")
