def detail(*args, **kwargs):
    return args,kwargs
names=[]
ages=[]
marks=[]
for i in range(1,3):
    name=input('Name: ')
    age=int(input('age: '))
    mark=int(input('marks: '))
    names.append(name)
    ages.append(age)
    marks.append(mark)
print(detail(names,age=ages,mark=marks))