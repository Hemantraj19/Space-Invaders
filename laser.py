from turtle import Turtle
import time


class Laser:
    def __init__(self) -> None:
        self.laser = None

    # def shoot(self, x_cor, y_cor, screen):
    #     if not self.laser:
    #         screen.tracer(0)
    #         self.laser = Turtle("square")
    #         self.laser.penup()
    #         self.laser.shapesize(stretch_len=0.3, stretch_wid=2)
    #         self.laser.color("white")
    #         self.laser.goto(x_cor, y_cor)
    #         screen.tracer(1)
    #         while self.laser.ycor() < 260:
    #             self.laser.goto(self.laser.xcor(), self.laser.ycor() + 10)
    #             time.sleep(0.01)
    #         self.laser = None

    def shoot(self, x_cor, y_cor, screen):
        if not self.laser:
            screen.tracer(0)
            self.laser = Turtle("square")
            self.laser.penup()
            self.laser.shapesize(stretch_len=0.3, stretch_wid=2)
            self.laser.color("white")
            self.laser.goto(x_cor, y_cor)
            screen.tracer(1)

            def move_laser():
                if self.laser and self.laser.ycor() < 260:
                    self.laser.goto(self.laser.xcor(), self.laser.ycor() + 20)
                    screen.update()
                    screen.ontimer(
                        move_laser, 5
                    )  # Move laser again after 10 milliseconds

                elif self.laser and self.laser.ycor() >= 260:
                    self.laser.clear()  # Clear the laser once it reaches its destination
                    self.laser.hideturtle()
                    self.laser = None

            move_laser()
