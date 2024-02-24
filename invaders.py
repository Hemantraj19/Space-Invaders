from turtle import Turtle
import random
from laser import Laser

direction = 1


class Invaders:
    def __init__(self) -> None:
        self.invaders_list = []
        self.place_invaders()
        self.invd_to_drop_bomb = []
        self.bomb = None
        self.move_invader_id = None

    def make_new_invader(self):
        invader = Turtle()
        invader.penup()
        invader.shape("invader_shape")
        self.invaders_list.append(invader)
        return invader

    def place_invaders(self):
        startig_x = -560
        starting_y = 260
        gap_x = 60
        gap_y = 40
        rows = 3
        columns = 8
        for _ in range(rows):
            for _ in range(columns):
                invader = self.make_new_invader()
                invader.goto(startig_x, starting_y)
                startig_x += gap_x
            startig_x = -560
            starting_y -= gap_y

    def move_invaders(self, screen):
        global direction

        # Calculate boundaries dynamically based on the number of invaders
        right_boundary = (len(self.invaders_list) // 2) * 50 - 40
        left_boundary = -right_boundary

        if self.invaders_list[-1].xcor() > right_boundary:
            direction = -1
        elif self.invaders_list[0].xcor() < left_boundary:
            direction = 1

        screen.tracer(0)
        for invader in self.invaders_list:
            invader.setx(invader.xcor() + 10 * direction)
        screen.tracer(1)
        self.move_invader_id = screen.ontimer(lambda: self.move_invaders(screen), 100)

    def can_drop_bombs(self, screen):
        self.invd_to_drop_bomb = []
        for i in range(8, 16):
            if not self.invaders_list[i + 8]:
                self.invd_to_drop_bomb.append(self.invaders_list[i])

        for i in range(8):
            if (
                not self.invaders_list[i + 8]
                and self.invaders_list[i] in self.invd_to_drop_bomb
            ):
                self.invd_to_drop_bomb.append(self.invaders_list[i])

        for i in range(16, 24):
            if self.invaders_list[i]:
                self.invd_to_drop_bomb.append(self.invaders_list[i])

    def drop_bomb(self, screen):
        random_invader = random.choice(self.invd_to_drop_bomb)
        screen.tracer(0)
        self.bomb = Turtle("circle")
        self.bomb.penup()
        self.bomb.color("red")
        self.bomb.goto(random_invader.xcor(), random_invader.ycor())
        screen.tracer(1)

        def move_bomb():
            if self.bomb.ycor() > -260:
                self.bomb.goto(self.bomb.xcor(), self.bomb.ycor() - 20)
                screen.update()
                screen.ontimer(move_bomb, 5)
            else:
                self.bomb.clear()
                self.bomb.hideturtle()
                self.bomb = None

        move_bomb()
