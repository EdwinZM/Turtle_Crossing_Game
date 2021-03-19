from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-200, 250)
        self.level = 0
        self.update()
    
    def update(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=(FONT))

    def victory(self):
        self.level += 1
        self.update()
    
    def defeat(self): 
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("courier", 30, "normal"))
 