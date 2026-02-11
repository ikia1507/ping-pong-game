from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self,score_xcor,player):
        super().__init__()
        self.hideturtle()
        self.score_xcor=score_xcor
        self.player=player
        self.score=0
        self.teleport(self.score_xcor,320)
        self.color("white")
        self.write(f"PLAYER {self.player}: {self.score}", move=False, align='center',
                   font=('open sans', 10, 'normal'))


    def scores(self):
        self.score+=1
        self.clear()
        self.write(f"SCORE PLAYER {self.player}: {self.score}", move=False, align='center',
                   font=('open sans', 10, 'normal'))

    #def score_display(self,plr):
    #    self.clear()
    #    self.teleport(0,0)
    #    self.write(f"PLAYER {plr} SCORED 1 POINT", move=False, align='center',
    #               font=('open sans', 10, 'normal'))
#
