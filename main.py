from turtle import Turtle, Screen
from invaders import Invaders
from tkinter import PhotoImage
import turtle
from shooter import Shooter
from laser import Laser
from scoreboard import Scoreboard
from heart import Heart

game_is_on = False

screen = Screen()
screen.setup(width=1200, height=600)
screen.bgcolor("black")

# ----------- Register invader shape--------------------------
img = PhotoImage(file="invader.png")
img = img.subsample(8, 8)
shape = turtle.Shape("image", img)
screen.register_shape(name="invader_shape", shape=shape)

# ---------------- Register shooter shape ----------------------
shooter_img = PhotoImage(file="shooter.png")
shooter_img = shooter_img.subsample(11, 11)
shape = turtle.Shape("image", shooter_img)
screen.register_shape(name="shooter_shape", shape=shape)

# ----------------- Register heart shape -------------------------
heart_img = PhotoImage(file="heart.png")
heart_img = heart_img.subsample(11, 11)
shape = turtle.Shape("image", heart_img)
screen.register_shape(name="heart_shape", shape=shape)


def shoot_laser():
    laser.shoot(shooter.xcor(), shooter.ycor(), screen)


def start_bomb_dropping():
    invaders.can_drop_bombs(screen)
    screen.ontimer(drop_single_bomb, 3000)  # Drop a bomb every 10 seconds


def drop_single_bomb():
    if game_is_on:
        invaders.drop_bomb(screen)
        screen.ontimer(drop_single_bomb, 3000)


def start_game():
    global game_is_on
    game_is_on = True
    invaders.move_invaders(screen)
    invaders.can_drop_bombs(screen)
    start_bomb_dropping()
    check_collision()
    check_bomb_collision()


def check_collision():
    global game_is_on
    if invaders.invaders_list:
        for invader in invaders.invaders_list:
            if laser.laser and laser.laser.distance(invader) < 25:
                screen.tracer(0)
                invader.hideturtle()
                invader = None
                laser.laser.reset()
                laser.laser.hideturtle()
                laser.laser = None
                scoreboard.increase_score()
                scoreboard.write_score()
                screen.tracer(1)
                invaders.can_drop_bombs(screen)

    if not invaders.invaders_list:
        game_over()

    if game_is_on:
        screen.ontimer(check_collision, 100)


def check_bomb_collision():
    global game_is_on
    if invaders.bomb is not None:
        if invaders.bomb.distance(shooter) < 20:
            heart.heart_list[0].hideturtle()
            heart.heart_list.pop(0)
            invaders.bomb.reset()
            invaders.bomb.hideturtle()
            invaders.bomb = None
        if not heart.heart_list:
            game_over()
    if game_is_on:
        screen.ontimer(check_bomb_collision, 5)


def game_over():
    global game_is_on
    game_is_on = False
    over = Turtle()
    over.hideturtle()
    over.penup()
    over.color("white")
    over.goto(0, 0)
    over.clear()
    over.write("Game Over", False, align="center", font=("Arial", 36, "bold"))


screen.tracer(0)
invaders = Invaders()
shooter = Shooter()
laser = Laser()
scoreboard = Scoreboard()
heart = Heart()

screen.tracer(1)
screen.listen()
screen.onkeypress(shooter.go_left, "Left")
screen.onkeypress(shooter.go_right, "Right")
screen.onkeypress(shoot_laser, "space")
screen.onkeypress(start_game, "s")


screen.exitonclick()
