from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):

        super().__init__()
        super().hideturtle()
        super().goto(0, 275)
        super().color("white")
        with open("high_score.txt") as file:
            high_score = file.read()
        self.i = 0
        self.write(f"Score: {self.i}  High score: {high_score}", False, "center", ('Arial', 15, 'normal'))

    def update_scorecard(self):
        self.i += 1
        self.clear()
        with open("high_score.txt") as file:
            high_score = file.read()
        self.write(f"Score: {self.i}  High score: {high_score}", False, "center", ('Arial', 15, 'normal'))

    def score(self):
        with open("high_score.txt") as file:
            high_score = file.read()
        if self.i > int(high_score):
            # self.high_score = self.i
            with open("high_score.txt", "w") as file:
                file.write(f"{self.i}")
            with open("high_score.txt") as file:
                high_score = file.read()
        self.i = 0
        self.clear()
        self.write(f"Score: {self.i} High score: {high_score}", False, "center", ('Arial', 15, 'normal'))
