x = 1.0
y = 500.0
vx = 200.0
vy = -200.0
t0 = millis()/1000
g = 200

def setup():
    size(1200,600)
  
def draw():
    global  x, y, vx, vy, g, t0
    t = millis()/1000.0 
    dt=t-t0
    t0=t
    y = (y + vy*dt)
    vy = vy + g*dt
    x = (x + vx*dt)
    background(169, 216, 229)
    stroke(0)
    fill(240, 240, 0)
    ellipse(x,y, 13, 13)
    fill(0,255,0)
    ellipse(685,585,30,30)
    if keyPressed == True:
        vx = 1.5*vx
        vy = 1.5*vy
