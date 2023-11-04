from turtle import Screen
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Compare collision with food
    if snake.new_turtles[0].distance(food) < 14:
        snake.food_eaten()
        food.refresh()
        scoreboard.update_scorecard()

    # Detecting collision with wall
    if (snake.new_turtles[0].xcor() > 280 or snake.new_turtles[0].xcor() < -280 or snake.new_turtles[0].ycor() > 280
            or snake.new_turtles[0].ycor() < -280):
        scoreboard.score()
        snake.go_to_center()

    # Detecting collision with tail
    for tut in snake.new_turtles:
        if tut == snake.new_turtles[1:]:
            if snake.new_turtles[0].distance(tut) < 11:
                scoreboard.score()

screen.exitonclick()
