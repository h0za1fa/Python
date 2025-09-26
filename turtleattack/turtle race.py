import turtle as t
import random

screen = t.Screen()
screen.setup(width=500,height=400)

t.colormode(255)
turtles_list = []
pos = [ 0 , 50 , -50 , 100 , -100]
colors = [ 'red' , 'blue' , 'green' , 'purple' , 'orange' ]

for _ in range (5):
    tim = t.Turtle()
    tim.shape('turtle')
    tim.color(colors[_])
    tim.setpos(-230,pos[_])
    turtles_list.append(tim)

bet = screen.textinput('bet', 'Enter your bet: ')

race_on = True
while race_on == True:
    for turtle in turtles_list:
        turtle.forward(random.randint(1,10))
        if turtle.xcor() >= 220:
            if bet == turtle.pencolor():
                print('Congrats you won!')
            else:
                print(f'You lost! {turtle.pencolor()} won')
            race_on = False
            break
screen.exitonclick()