import pgzrun


TITLE='FLAPPY BALL'
HEIGHT=600
WIDTH=600

GRAVITY=200


class Ball():
  def __init__(self,r,c,x,y):
      self.radius=r
      self.color=c
      self.x=x
      self.y=y
      self.vx=30
      self.vy=0
  def make(self):
      screen.draw.filled_circle((self.x,self.y),self.radius,self.color) 
ball1=Ball(36,"red",100,200)
ball2=Ball(22,"blue",250,250) 
ball3=Ball(50,"purple",186,356)

def draw():
    screen.clear()
    ball1.make()
    ball2.make()
    ball3.make()
    
def update(dt):
    uy=ball1.vy
    ball1.vy+=GRAVITY*dt
    ball1.y+=(uy+ball1.vy)*0.5*dt
    if ball1.y>555:
        ball1.y=555
        ball1.vy=ball1.vy*-0.9
    if ball1.x<45 or ball1.x>555:
        ball1.vx=ball1.vx*-1
    ball1.x=ball1.x+(ball1.vx*dt)    
    if keyboard.space:
        ball1.vy=-500
    uy=ball2.vy
    ball2.vy+=GRAVITY*dt
    ball2.y+=(uy+ball2.vy)*0.5*dt
    if ball2.y>555:
        ball2.y=555
        ball2.vy=ball2.vy*-0.9
    if ball2.x<45 or ball2.x>555:
        ball2.vx=ball2.vx*-1
    ball2.x=ball2.x+(ball2.vx*dt)    
    if keyboard.space:
        ball2.vy=-500
    uy=ball3.vy
    ball3.vy+=GRAVITY*dt
    ball3.y+=(uy+ball3.vy)*0.5*dt
    if ball3.y>555:
        ball3.y=555
        ball3.vy=ball3.vy*-0.9
    if ball3.x<45 or ball3.x>555:
        ball3.vx=ball3.vx*-1
    ball3.x=ball3.x+(ball3.vx*dt)    
    if keyboard.space:
        ball3.vy=-500



pgzrun.go()