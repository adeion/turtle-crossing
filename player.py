from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.time_delay = 0.1
        self.shape('turtle')
        self.color('white')
        self.penup()
        self.go_to_start()
        self.lt(90)

    def move(self):
        self.fd(MOVE_DISTANCE)

    def finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            self.time_delay -= 0.01
            return True
        else:
            return False

    def go_to_start(self):
        self.clear()
        self.goto(STARTING_POSITION)
