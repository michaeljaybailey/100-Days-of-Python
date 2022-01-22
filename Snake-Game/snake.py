from turtle import Turtle
STARTING_POSITIONS = [0, -20, -40]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for snake_index in STARTING_POSITIONS:
            new_snake = Turtle(shape="square")
            new_snake.color("white")
            new_snake.penup()
            new_snake.goto(x=snake_index, y=0)
            self.segments.append(new_snake)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() != 270:

            self.segments[0].setheading(90)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

