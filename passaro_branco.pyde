x0 = 1.0
y0 = 5.0
vx = 6.0
vy = -6.0
t0 = millis()
oldt = t0/1000.0
u = -10
k=-10

import copy

def setup():
  size(1200,600)

def draw():
    global oldt, x0, y0, vx, vy,u,k,v
    t = (millis()-t0)/1000.0  
    x = 100*(x0 + vx*t)
    y = 100*(y0 + vy*t+ 5*t*t)
    background(169, 216, 229)
    stroke(0)
    fill(255)
    ellipse(x,y, 20, 20)
    fill(0,255,0)
    ellipse(685,585,30,30)
    oldt = t
    if mousePressed:
        u = copy.copy(x)
        k = copy.copy(y)
        vk = copy.copy(vy)
        vy = 1.1*vy
    vu = 0
    vk = vy
    v = (k + vk*t + 50*t*t)
    fill(255)
    ellipse(u,v,10,15)
