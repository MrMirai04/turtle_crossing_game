from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"
SCORE_POS = (-210, 250)
MAX_LEVEL = 2

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.pencolor("white")
        self.hideturtle()
        self.score = 1
        self.set_up()
        self.pendown()

    def set_up(self):
        self.goto(SCORE_POS)
        self.write(f"Level: {self.score}", align=ALIGNMENT, font=FONT)

    def increase(self):
        self.clear()
        self.penup()
        self.score += 1
        if not self.last_level():
            self.pendown()
            self.write(f"Level: {self.score}", align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.pendown()
        self.write(f"Pierdut :(", align=ALIGNMENT, font=FONT)

    def end(self):
        self.goto(0, 0)
        self.write(f"Ai castigat!", align=ALIGNMENT, font=FONT)

    def last_level(self):
        return self.score > MAX_LEVEL






