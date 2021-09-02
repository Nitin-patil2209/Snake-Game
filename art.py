from snake import Snake
from turtle import Screen
from scoreboard import Scoreboard
import food
import time
import random
screen = Screen()
score = Scoreboard()
screen.listen()
screen.setup(600,600)
screen.tracer(8)
screen.title("Snake game")
screen.bgcolor("black")
player = Snake()
feed = food.Food()

is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)
    player.Move()
    screen.onkey(fun=player.Up, key="Up")
    screen.onkey(fun=player.Down, key="Down")
    screen.onkey(fun=player.Left, key="Left")
    screen.onkey(fun=player.Right, key="Right")
    if player.head.distance(feed) < 15:
        feed.Move()
        score.Increment()
        player.Addnew()
    if player.head.xcor() > 290 or player.head.xcor() < -290 or player.head.ycor() > 290 or player.head.ycor() < -290:
        is_on = False
        score.Gameover()
    for i in player.turtles[1:]:
        # if i == player.head:
        #     pass
        if player.head.distance(i)<10:
            score.Gameover()
            is_on = False








screen.exitonclick()