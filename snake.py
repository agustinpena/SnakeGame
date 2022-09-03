# snake class for the snake game

from turtle import Turtle

MOVING_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        for i in range(3):
            curr_segment = Turtle('square')
            curr_segment.penup()
            curr_segment.color('white')
            curr_segment.goto((-20) * i - 200, 0)
            self.segments.append(curr_segment)
        self.head = self.segments[0]

    def move(self):
        lx = len(self.segments)
        for j in range(lx - 1, 0, -1):
            new_x = self.segments[j - 1].xcor()
            new_y = self.segments[j - 1].ycor()
            self.segments[j].goto((new_x, new_y))
        self.segments[0].forward(MOVING_DISTANCE)

    def go_east(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def go_west(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def go_north(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def go_south(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def add_segment(self):
        s = self.segments[-1]
        new_segment = Turtle('square')
        new_segment.penup()
        new_segment.color('white')
        new_segment.goto(s.xcor(), s.ycor())
        self.segments.append(new_segment)

    def illegal_contact(self):
        for i in range(1, len(self.segments)):
            if self.head.distance(self.segments[i]) < 10:
                return True
        if self.head.xcor() <= -299 or self.head.xcor() >= 299:
            return True
        if self.head.ycor() <= -299 or self.head.ycor() >= 299:
            return True
        return False
