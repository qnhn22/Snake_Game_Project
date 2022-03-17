from turtle import Turtle, Screen
import time
from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("deepskyblue1")
screen.title("The Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.

    if snake.head.distance(food) < 28:
        print("hehe")
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -280:
        print("Game over!")
        scoreboard.reset_high_score()
        snake.reset_snake()

    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 15:
            scoreboard.reset_high_score()
            snake.reset_snake()

screen.exitonclick()
