from turtle import Turtle, Screen

sides = 3
a=0
colors = [
    "red",
    "green",
    "blue",
    "yellow",
    "orange",
    "purple",
    "pink",
    "brown",
    "black",
    "white",
    "gray",
    "cyan",
    "magenta",
    "lime",
    "teal",
    "navy",
    "maroon",
    "olive",
    "silver",
    "gold"
]

print(colors)


timm = Turtle()
while True:
    timm.color(colors[a])
    for _ in range(sides):
        timm.forward(100)
        timm.left(360/sides)
    sides+=1
    a+=1



my_screen = Screen()
my_screen.exitonclick()