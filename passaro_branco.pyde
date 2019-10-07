x0 = 100.0
y0 = 500.0
vx0 = 600.0
vy0 = -600.0
t0 = millis()
p_ovox = -10
p_ovoy=-10
x = 0
y = 0
vovo = 0

def setup():
  size(1200,600)

def draw():
    global x0, y0, vx0, vy0,p_ovox,p_ovoy, t0,x,y
    t = (millis()-t0)/1000.0  
    x = (x0 + vx0*t)
    vy = vy0 + 1000*t
    y = (y0 + vy0*t+ 500*t*t)
    background(169, 216, 229)
    stroke(0)
    fill(255)
    ellipse(x,y, 20, 20)
    fill(0,255,0)
    ellipse(685,585,30,30)
    v = (p_ovoy + vovo*t + 500*t*t)
    fill(255)
    ellipse(p_ovox,v,10,15)
    print(p_ovoy)
    print(p_ovox)
    
def mouseClicked():
    global x,y,vy0,t0,x0,y0,p_ovoy,p_ovox,vovo
    t = (millis()-t0)/1000.0
    p_ovox = x
    p_ovoy = y
    vy = vy0 + 1000*t
    vy0 = 1.5*vy
    vovo = abs(0.95*vy)
    x0 = x
    y0 = y
    t0 = millis()
