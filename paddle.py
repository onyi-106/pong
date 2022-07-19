from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        """position = (x, y) -> tuple"""
        super().__init__()
        self.penup()
        self.shapesize(5, 1)
        self.shape("square")
        self.color("white")
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 20
        if new_y > 240:
            pass
        else:
            self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        if new_y < -240:
            pass
        else:
            self.goto(self.xcor(), new_y)

