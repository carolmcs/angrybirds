
x0 = 0.0
y0 = 2.0
vx = 5.0
vy = -5.0
t0 = millis()
oldt = t0/1000.0


def setup():
  size(800,800)
  
def draw():
  global oldt, x0, y0, vx, vy
  t = (millis()-t0)/1000.0  
  x = 100*(x0 + vx*t)
  y = 100*(y0 + vy*t+ 5*t*t)
  background(255)
  stroke(0)
  fill(0)
  ellipse(x,y,20, 20)
  oldt = t
    
def mouseClicked():
  global oldt, t0
  t0 = millis()
  oldt = t0/1000.0