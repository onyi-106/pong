from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 190)
        self.write(self.left_score, align="center", font=("Courier", 80, "bold"))
        self.goto(100, 190)
        self.write(self.right_score, align="center", font=("Courier", 80, "bold"))
