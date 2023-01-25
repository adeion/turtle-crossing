from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-250, 250)
        self.clear()

    def game_over(self):

        self.goto(-100, 0)
        self.color("red")
        self.write("Game Over ", True, align='center', font=('Arial', 38, 'bold'))

    def update_score(self):
        self.clear()
        self.color('white')
        self.write(f"level:{self.level} ", False, align='center', font=('Arial', 18, 'bold'))

    def increase_level(self):
        self.level += 1
        self.update_score()
