# the snake game using
# the turtle module
# main file

from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

# create and set screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Simple but Cool Snake Game')
screen.tracer(0)
screen.colormode(255)

# create a snake
snake = Snake()
screen.update()

# screen events
screen.listen()
screen.onkey(snake.go_north, 'Up')
screen.onkey(snake.go_south, 'Down')
screen.onkey(snake.go_east, 'Right')
screen.onkey(snake.go_west, 'Left')

# create a meal for the snake
meal = Food()
screen.update()

# set score
score = Score()
screen.title('Snake Game. Current Score: ' + str(score.current))
screen.update()

# snake moves
while True:
    screen.update()
    snake.move()
    time.sleep(0.1)
    # detect colision with food
    if snake.head.distance(meal) < 10:
        score.increase()
        snake.add_segment()
        screen.title('Score: ' + str(score.get()))
        meal.update()
    # detect illegal contact
    if snake.illegal_contact():
        break

# display final score
screen.title('Final Score: * ' + str(score.get()) + ' * Awesome!')
screen.update()

# exit-on-click screen property
screen.exitonclick()
