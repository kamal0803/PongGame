from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.goto(x, y)

        self.shapesize(stretch_wid=5, stretch_len=1)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def within_upper_bound(self):
        if self.ycor() > 260:
            self.sety(self.ycor()-20)

    def within_lower_bound(self):
        if self.ycor() < -260:
            self.sety(self.ycor()+20)