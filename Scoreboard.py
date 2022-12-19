from turtle import Turtle

ALIGNMENT = "center"
FONT_TYPE = ("arial", 18, "italic")


class ScoreBoard(Turtle):
    def __init__(self):
        self.points = 0
        super().__init__()

    def score(self):
        self.clear()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.points}", True, ALIGNMENT, FONT_TYPE)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", True, ALIGNMENT, FONT_TYPE)

