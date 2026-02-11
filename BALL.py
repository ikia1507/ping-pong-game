from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(1,1)
        self.color("white")
        self.xcor_moves=7
        self.ycor_moves=7
        self.speed_parameter=0.1

    def move_ball(self):
        #self.seth(45)    #will create problem in bounce logic
        #self.forward(5)
        new_x=self.xcor()+self.xcor_moves
        new_y=self.ycor()+self.ycor_moves
        self.goto(new_x,new_y)
    def restart(self):
        self.goto(0,0)
        #reversing the direction toward the other candidate
        self.xcor_moves*=-1
        #reverting the speed back while restarting the game
        self.speed_parameter=0.1

    def bounce_boundary(self):
        #new_y=self.ycor()-10  local variable not an attribute hence no effect so need to define new attribute
        self.ycor_moves*=-1  #reversing the direction

    def bounce_paddle(self):
        self.xcor_moves*=-1
        self.speed_parameter*=0.8
