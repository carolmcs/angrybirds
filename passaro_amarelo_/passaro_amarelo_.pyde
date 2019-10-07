x0 = 100.0
y0 = 500.0
vx = 600.0
vy0 = -700.0
t0 = millis()
oldt = t0/1000.0
g = 1000
x = 0
y = 0
k = 400

def setup():
  size(1200,600)

def draw():
  global oldt, x0, y0, vx, vy0, g,x,y,k
  t = (millis()-t0)/1000.0  
  x = (x0 + vx*t)
  y = (y0 + vy0*t+ (g/2)*t*t)
  vy = vy0 + 1000*t
  background(169, 216, 229)
  stroke(0)
  fill(255, 216, 53)
  ellipse(x,y, 20, 20)
  fill(137,186,35) #orelha
  stroke(60,108,34)
  ellipse(705+k,555,15,15)
  fill(137,186,35) #outra orelha
  stroke(60,108,34)
  ellipse(685+k,547,15,15)
  fill(137,186,35) #cabeça do porco
  stroke(60,108,34)
  ellipse(685+k,575,50,50)
  fill(179,201,2) #nariz do porco
  stroke(60,108,34)
  ellipse(685+k,578,21,15)
  fill(255) #olho esquerdo
  stroke(60,108,34)
  ellipse(672+k,565,10,10)
  fill(255) #olho direito
  stroke(60,108,34)
  ellipse(698+k,565,10,10)
  fill(0) #pupila direita
  ellipse(698+k,565,3,3)
  fill(0) #pupila esquerda
  ellipse(672+k,565,3,3)
  fill(30,59,29) #narina esquerda
  ellipse(680+k,578,3,3)
  fill(30,59,29) #narina direita
  ellipse(690+k,578,3,3)
  if (x-685-k)**2 + (y-575)**2 <= 900:
      fill(169,216,229)
      noStroke()
      ellipse(685+k,575, 80,80)


def mouseClicked():
    global vy,vy0, t0,vx,x0,x,y0,y
    t = (millis()-t0)/1000.0
    vy = vy0 + 1000*t
    vy0 = 2*vy
    vx = 2*vx
    x0 = x
    y0 = y
    t0 = millis()
