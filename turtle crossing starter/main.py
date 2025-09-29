import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

tim = Player()
score = Scoreboard()

screen.onkey(tim.movement, 'w')

car_index = []
car_delay = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    if car_delay % 6 == 0:
        cars = CarManager()
        car_index.append(cars)
    
    for _ in range (len(car_index)) :
        car_index[_].movement()
        if tim.distance(car_index[_]) < 20:
            score.game_over()
            game_is_on = False
    
    if tim.ycor() > 260:
        tim.goto(0, -280)
        score.levelup()
        for _ in range (len(car_index)) :
            car_index[_].level_up()
    
    car_delay += 1

screen.exitonclick()