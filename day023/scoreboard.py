from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.goto(-200, 250)
        self.pencolor("black")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.score}", False, align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", False, align=ALIGNMENT, font=FONT)
