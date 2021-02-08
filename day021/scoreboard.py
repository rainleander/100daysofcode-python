from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Serif", 12, "bold")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.setposition(0.00, 280.00)
        self.pencolor("white")
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()


    def game_over(self):
        self.setposition(0.00, 0.00)
        self.write("GAME OVER!! !", False, align=ALIGNMENT, font=FONT)
