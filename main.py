from turtle import Screen
from roads import Road
from frog import Frog
from cars import Car
from gameover import GameOver, Score
import random
import time


screen = Screen()
screen.bgcolor("gray")
screen.setup(width=800, height=600)
screen.title("Frogger!")
screen.tracer(0)
screen.colormode(255)

# TODO 1: make screen

roads = Road()
roads.make_road()
game_is_on = True

# TODO 2: make little froggy
frog = Frog()
score = 0
level = 0.1
screen.listen()
screen.onkey(frog.up, "Up")
screen.onkey(frog.down, "Down")
screen.onkey(frog.left, "Left")
screen.onkey(frog.right, "Right")

# TODO 3: make cars go vroom-vroom

car_gen = 7
car_list = []
scorey = Score()

while game_is_on:

    if car_gen % random.randint(7, 11) == 0:
        car = Car()
        car_list.append(car)

    for x in car_list:
        x.move(10)
    car_gen += 1

    for x in car_list:
        if frog.distance(x) < 60:
            game_is_on = False
            GameOver()

    if frog.ycor() > 280:
        scorey.add_score()
        frog.goto(x=0, y=-300)
        level *= 0.9
    screen.update()
    time.sleep(level)


# TODO 4: hit by car is oh-no!

# TODO 5: end of road is score!

# TODO 6: score is go faster!



screen.exitonclick()
