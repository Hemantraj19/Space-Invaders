from turtle import Turtle


class Shooter(Turtle):
    def __init__(
        self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True
    ) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.shape("shooter_shape")
        self.penup()
        self.goto(0, -265)
        self.laser_list = []

    def go_left(self):
        if self.xcor() > -560:
            self.goto(self.xcor() - 20, self.ycor())

    def go_right(self):
        if self.xcor() < 560:
            self.goto(self.xcor() + 20, self.ycor())
