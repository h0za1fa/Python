hieghts=input('Enter hieghts: ').split()
sum_of_hieght=0
num_of_people=0
for hieght in hieghts:
    hieght=int(hieght)
    sum_of_hieght+=hieght
    num_of_people+=1
avrg_height=round(sum_of_hieght/num_of_people)
print(f'The average height is {avrg_height}')