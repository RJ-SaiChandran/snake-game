from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.goto(0, 270)
        self.color("white")
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write("Score: " + str(self.score), font=("Courier", 18, "normal"), align="center")
        
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", font=("Courier", 18, "normal"), align="center")