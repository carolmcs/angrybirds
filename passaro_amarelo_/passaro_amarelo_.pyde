x0 = 1.0
y0 = 5.0
vx = 5.0
vy0 = -5.0
t0 = millis()
oldt = t0/1000.0
g = 10


def setup():
  size(1200,600)
  
def draw():
  global oldt, x0, y0, vx, vy0, g
  t = (millis()-t0)/1000.0  
  vy = vy0 + g*t
  x = 100*(x0 + vx*t)
  y = 100*(y0 + (vy-g*t)*t+ (g/2)*t*t)
  background(169, 216, 229)
  stroke(0)
  fill(240, 240, 0)
  ellipse(x,y, 13, 13)
  fill(0,255,0)
  ellipse(685,585,30,30)
  oldt = t
  if keyPressed == True:
      vx = 2*vx
      vy = 2*vy
