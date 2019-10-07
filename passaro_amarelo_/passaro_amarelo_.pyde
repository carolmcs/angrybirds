
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
  fill(137,186,35) #orelha
  stroke(60,108,34)
  ellipse(705,555,15,15)
  fill(137,186,35) #outra orelha
  stroke(60,108,34)
  ellipse(685,547,15,15)
  fill(137,186,35) #cabeça do porco
  stroke(60,108,34)
  ellipse(685,575,50,50)
  fill(179,201,2) #nariz do porco
  stroke(60,108,34)
  ellipse(685,578,21,15)
  fill(255) #olho esquerdo
  stroke(60,108,34)
  ellipse(672,565,10,10)
  fill(255) #olho direito
  stroke(60,108,34)
  ellipse(698,565,10,10)
  fill(0) #pupila direita
  ellipse(698,565,3,3)
  fill(0) #pupila esquerda
  ellipse(672,565,3,3)
  fill(30,59,29) #narina esquerda
  ellipse(680,578,3,3)
  fill(30,59,29) #narina direita
  ellipse(690,578,3,3)


def mouseClicked():
    global vy,vy0, t0,vx,x0,x,y0,y
    t = (millis()-t0)/1000.0
    vy = vy0 + 1000*t
    vy0 = 2*vy
    vx = 2*vx
    x0 = x
    y0 = y
    t0 = millis()
