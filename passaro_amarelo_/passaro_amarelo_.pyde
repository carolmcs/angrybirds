x0 = 100.0
y0 = 500.0
vx = 500.0
vy0 = -500.0
t0 = millis()
oldt = t0/1000.0
g = 1000
x = 0
y = 0

def setup():
  size(1200,600)

def draw():
  global oldt, x0, y0, vx, vy0, g,x,y
  t = (millis()-t0)/1000.0  
  x = (x0 + vx*t)
  y = (y0 + vy0*t+ (g/2)*t*t)
  vy = vy0 + 1000*t
  background(169, 216, 229)
  stroke(0)
  fill(240, 240, 0)
  ellipse(x,y, 13, 13)
  fill(0,255,0)
  ellipse(685,585,30,30)
  print(vy)

def mouseClicked():
    global vy,vy0, t0,vx,x0,x,y0,y
    t = (millis()-t0)/1000.0
    vy = vy0 + 1000*t
    vy0 = 2*vy
    vx = 2*vx
    x0 = x
    y0 = y
    t0 = millis()
