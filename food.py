from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("blue")
        self.speed("fastest")
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.Move()
    def Move(self):
        self.xcord = random.randint(-270, 270)
        self.ycord = random.randint(-270, 270)
        self.goto(self.xcord, self.ycord)


