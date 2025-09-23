from turtle import Turtle, Screen
from prettytable import PrettyTable

# timmy = Turtle()
# timmy.shape('turtle')
# timmy.color('blue')

# my_screen=Screen()
# my_screen.exitonclick()

table=PrettyTable()
table.add_column ('name',['amash','hozaifa','khizer']),
table.add_column ('marks',[13,57,22])
table.align='l'
print(table)