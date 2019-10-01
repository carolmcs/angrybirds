x0 = 1.0
y0 = 5.0
vx = 5.0
vy = -5.0
t0 = millis()
oldt = t0/1000.0


def setup():
  size(1200,600)
  
def draw():
  global oldt, x0, y0, vx, vy
  t = (millis()-t0)/1000.0  
  x = 100*(x0 + vx*t)
  y = 100*(y0 + vy*t+ 5*t*t)
  background(169, 216, 229)
  stroke(0)
  fill(240, 0, 30)
  ellipse(x,y, 13, 13)
  fill(0,255,0)
  ellipse(685,585,30,30)
  oldt = t
    
def mouseClicked():
  global oldt, t0
  t0 = millis()
  oldt = t0/1000.0
