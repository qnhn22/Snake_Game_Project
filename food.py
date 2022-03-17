from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.resizemode("user")
        self.shapesize(0.5, 0.5)
        self.color("black")
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.setpos(random_x, random_x)
