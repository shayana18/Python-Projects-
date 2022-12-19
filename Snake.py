from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20


class Snake:

    def __init__(self):
        self.seg_snake = []
        self.create_snake()
        self.head = self.seg_snake[0]

    def create_snake(self):
        for position in POSITIONS:
            self.add_segement(position)


    def snake_move(self):
        for seg_num in range(len(self.seg_snake) - 1, 0, -1):
            new_x = self.seg_snake[seg_num - 1].xcor()
            new_y = self.seg_snake[seg_num - 1].ycor()
            self.seg_snake[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE)

    def up(self):
        current_pos = self.head.heading()
        if current_pos == 0:
            new_pos = current_pos + 90
            self.head.setheading(new_pos)
        elif current_pos == 180.0:
            new_pos = current_pos + 270
            self.head.setheading(new_pos)

        else:
            pass

    def down(self):
        current_pos = self.head.heading()

        if current_pos == 0:
            new_pos = current_pos + 270
            self.head.setheading(new_pos)
        elif current_pos == 180.0:
            new_pos = current_pos + 90
            self.head.setheading(new_pos)
        else:
            pass

    def left(self):
        current_pos = self.head.heading()

        if current_pos == 90.0:
            new_pos = current_pos + 90
            self.head.setheading(new_pos)

        elif current_pos == 270.0:
            new_pos = current_pos + 270
            self.head.setheading(new_pos)

        else:
            pass

    def right(self):
        current_pos = self.seg_snake[0].heading()

        if current_pos == 90.0:
            new_pos = current_pos + 270
            self.seg_snake[0].setheading(new_pos)

        elif current_pos == 270.0:
            new_pos = current_pos + 90
            self.seg_snake[0].setheading(new_pos)

        else:
            pass

    def add_segement(self, position):
        new_segement = Turtle()
        new_segement.shape("square")
        new_segement.color("white")
        new_segement.penup()
        new_segement.goto(position)
        self.seg_snake.append(new_segement)


    def extend(self):
        self.add_segement(self.seg_snake[-1].position())



