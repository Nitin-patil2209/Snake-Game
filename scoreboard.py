from turtle import Turtle
ALIGN = "center"
FONT = ("courier", 15, "normal")
class Scoreboard(Turtle):


    def __init__(self):
        self.num = 0
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.Update()
        self.hideturtle()

    def Update(self):
        self.write(f"Score = {self.num}", move=False, align=ALIGN, font=FONT)
    def Gameover(self):
        self.goto(0,0)
        self.write(f"Game Over", move=False, align=ALIGN, font=FONT)

    def Increment(self):

        self.num += 1
        self.clear()
        self.Update()

