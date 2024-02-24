from turtle import Turtle


class Heart:
    def __init__(self) -> None:
        self.heart_list = []
        self.place_hearts()

    def make_hearts(self):
        heart = Turtle()
        heart.penup()
        heart.shape("heart_shape")
        self.heart_list.append(heart)
        return heart

    def place_hearts(self):
        starting_x = 570
        starting_y = -280
        gap = 25
        for _ in range(3):
            heart = self.make_hearts()
            heart.goto(starting_x, starting_y)
            starting_x -= gap
