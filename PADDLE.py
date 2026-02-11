import turtle as t
from turtle import Turtle


class Paddle(Turtle):
     def __init__(self,position):
         super().__init__()
         self.position=position
         self.color("white")
         self.shape("square")
         self.shapesize(5,1)
         self.penup()
         self.speed("fastest")
         self.setposition(self.position)


     def move_up(self):
         new_y=self.ycor()+20
         self.setposition(self.xcor(),new_y)
         #self.paddle_body.forward(20) will give wierd movement hence removed

     def move_down(self):
         new_y = self.ycor() - 20
         self.setposition(self.xcor(), new_y)



















""" THIS IS SNAKE CONCEPT SO NOT USE IT HERE 
         self.paddle_body=[]
         self.create_paddle()

     def create_paddle(self):
         for p in self.position:
             new_body=t.Turtle()
             new_body.shape("square")
             new_body.color("white")
             new_body.penup()
             new_body.setposition(p)
             self.paddle_body.append(new_body)

     def move_up(self):
         for i in range(len(self.paddle_body) - 1, 0, -1):
             new_y=self.paddle_body[i - 1].ycor
             self.paddle_body[i].setposition(new_x,new_y)
         self.paddle_body[0].forward(100)
"""
