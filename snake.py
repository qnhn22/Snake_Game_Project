from turtle import Turtle
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for position in POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.penup()
        segment.setpos(position)
        segment.color("white")
        self.snake_segments.append(segment)

    def extend(self):
        new_pos = self.snake_segments[-1].pos()
        self.add_segment(new_pos)

    def move(self):
        for i in range(len(self.snake_segments) - 1, 0, -1):
            self.snake_segments[i].setpos(self.snake_segments[i - 1].pos())
        self.snake_segments[0].forward(MOVE_DISTANCE)

    def reset_snake(self):
        for segment in self.snake_segments:
            segment.setpos(1000, 1000)
        self.snake_segments.clear()
        self.create_snake()
        self.head = self.snake_segments[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)



