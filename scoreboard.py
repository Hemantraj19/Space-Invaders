from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(
        self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True
    ) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-550, -280)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(
            f"Score: {self.score}",
            False,
            align="center",
            font=("Arial", 16, "normal"),
        )

    def increase_score(self):
        self.score += 1
