from turtle import Turtle


class Road(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.y_cor = [-200, -100, 0, 100, 200]
        self.x_cor = 400
        self.pensize(5)
        self.hideturtle()

    def make_road(self):
        for number in range(5):
            self.goto(x=400, y=self.y_cor[number])
            self.setheading(180)
            for _ in range(20):
                self.pendown()
                self.fd(20)
                self.penup()
                self.fd(20)
