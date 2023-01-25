
from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_X = 300


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_turtles = []
        self.hideturtle()
        self.new_cars = None

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 6:
            self.new_cars = Turtle(shape='square')
            self.new_cars.shapesize(stretch_len=2, stretch_wid=1)
            self.new_cars.color(random.choice(COLORS))
            self.new_cars.penup()
            self.new_cars.goto(STARTING_X, random.randint(-250, 250))
            self.all_turtles.append(self.new_cars)

    def move_car(self):
        for cars in self.all_turtles:
            cars.bk(STARTING_MOVE_DISTANCE)

