from turtle import Turtle

LIST_POS = [(0,0), (-20,0), (-40,0)]
UP = 90
RIGHT = 0
LEFT = 180
DOWN = 270
class Snake:
    def __init__(self):
        self.turtles = []
        self.Create()
        self.head = self.turtles[0]
    def Create(self):
        for i in LIST_POS:
            self.Createbody(i)

    def Createbody(self,position):
        tim = Turtle(shape="square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.turtles.append(tim)

    def Addnew(self):
        self.Createbody(self.turtles[-1].position())
    def Move(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            txcor = self.turtles[i - 1].xcor()
            tycor = self.turtles[i - 1].ycor()
            self.turtles[i].goto(txcor, tycor)

        self.head.forward(20)
    def Up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def Down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def Right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def Left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)