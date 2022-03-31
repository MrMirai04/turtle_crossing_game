from turtle import Turtle
import random as r

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(180)
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=1)
        self.level = 1
        self.speed = STARTING_MOVE_DISTANCE
        self.color(r.choice(COLORS))
        self.initialize()

    def offscreen(self):
        return self.xcor() < -310

    def initialize(self):
        random_y = r.randint(-240, 240)
        random_x = r.randint(-310, 610)
        self.goto(random_x, random_y)

    def place(self):
        random_y = r.randint(-240, 240)
        random_x = r.randint(310, 910)
        self.goto(random_x, random_y)

    def move(self):
        next_x = self.xcor() - self.speed
        self.goto(next_x, self.ycor())

    def next_level(self):
        self.speed += MOVE_INCREMENT
