import turtle as t
import time
from food import Food
from snake import Snake

snake = Snake()
screen = t.Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.listen()
screen.tracer(0)

for _ in range(6):
    snake.make_segments()
food = Food()
food.refresh()

game_on = True
while game_on == True:
    screen.update()
    time.sleep(0.1)
    screen.onkeypress(snake.turn_left, "d")
    screen.onkeypress(snake.turn_right, "a")
    snake.movement()
    if snake.segments[0].distance(food.xcor(),food.ycor()) < 20:
        food.refresh()
        snake.make_segments()
    if snake.self_collision() == True:
        print('You lost')
        break
screen.exitonclick()
