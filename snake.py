from turtle import Turtle

new_turtles = []


class Snake:

    def __init__(self):
        self.new_turtles = []
        self.create_snake()

    def create_snake(self):

        # print(self.new_turtles)
        for turtles in range(3):
            new_turtle = Turtle("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(0 - turtles * 20, 0)
            self.new_turtles.append(new_turtle)

    def move(self):
        for seg_num in range(len(self.new_turtles) - 1, 0, -1):
            new_x = self.new_turtles[seg_num - 1].xcor()
            new_y = self.new_turtles[seg_num - 1].ycor()
            self.new_turtles[seg_num].goto(new_x, new_y)
        self.new_turtles[0].forward(10)

    def up(self):
        if not self.new_turtles[0].heading() == 270:
            self.new_turtles[0].setheading(90)
        # print(self.new_turtles[0].heading())

    def down(self):
        if not self.new_turtles[0].heading() == 90:
            self.new_turtles[0].setheading(270)

    def left(self):
        if not self.new_turtles[0].heading() == 0:
            self.new_turtles[0].setheading(180)

    def right(self):
        if not self.new_turtles[0].heading() == 180:
            self.new_turtles[0].setheading(0)

    def food_eaten(self):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(self.new_turtles[-1].xcor(), self.new_turtles[-1].ycor())
        self.new_turtles.append(new_turtle)

    def go_to_center(self):
        for tut in self.new_turtles:
            tut.hideturtle()
        self.new_turtles.clear()
        self.create_snake()
