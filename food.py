# food class for the snake game

from random import randint
from turtle import Turtle

# Possible shapes: classic, turtle,
# cirle, square, triangle, arrow.
FOOD_SHAPE = 'square'


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.update()

    def update(self):
        self.clear()
        self.shape(FOOD_SHAPE)
        self.penup()
        self.speed('fastest')
        self.color(randint(0, 255), randint(0, 255), randint(0, 255))
        self.goto(randint(-11, 11) * 20, randint(-11, 11) * 20)
