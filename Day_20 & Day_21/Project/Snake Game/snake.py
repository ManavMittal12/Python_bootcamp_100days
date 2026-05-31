from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.my_snake = []
        self.create_a_snake()
        self.head = self.my_snake[0]

    # These two functions will create our snake
    def create_a_snake(self):
        """
        Creates a Snake body when initialized
        """
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake_body = Turtle(shape="square")
        snake_body.color("white")
        snake_body.penup()
        snake_body.goto(position)
        self.my_snake.append(snake_body)


    def move(self):
        """
        Makes the snake move forward
        """
        for snake in range(len(self.my_snake) - 1, 0 ,-1 ):
            new_x = self.my_snake[snake - 1].xcor()
            new_y = self.my_snake[snake - 1].ycor()
            self.my_snake[snake].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)




    def extend_snake(self):
        # add a new segment to the snake
        self.add_segment(self.my_snake[-1].position())
