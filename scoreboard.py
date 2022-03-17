from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.setpos(0, 260)
        self.update_score()
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"High score: {self.high_score}     Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.setpos(0, 0)
        self.write(arg="Game Over", move=False, align=ALIGNMENT, font=("Arial", 40, "normal"))

    def reset_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.score = 0
            with open("data.txt", "w") as file:
                file.write(str(self.high_score))
        else:
            self.score = 0
        self.update_score()
