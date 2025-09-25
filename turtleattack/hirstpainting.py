import colorgram
import turtle as t
import random

rgb_colors = []
colors=colorgram.extract('turtleattack\Capture001.png' , 30)
tim = t.Turtle()
t.colormode(255)
tim.penup()
y = -250


for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    color_tuple = ( r , g , b )
    rgb_colors.append(color_tuple)

for _ in range (10):
    tim.setpos( -250, y )
    for i in range (10):
        tim.color(random.choice(rgb_colors))
        tim.dot(20)
        tim.forward(50)
    # tim.setpos(0 , 0)
    y += 50    

my_screen = t.Screen()
my_screen.exitonclick()