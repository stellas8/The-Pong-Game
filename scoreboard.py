from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "bold"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "bold"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def middle_line(self):
        self.color("white")
        self.pensize(5)
        self.hideturtle()
        self.penup()
        self.goto(0, 290)
        self.setheading(270)
        for _ in range(1, 20):
            self.pendown()
            self.forward(30)
            self.penup()
            self.forward(30)
