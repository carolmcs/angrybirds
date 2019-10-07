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
  oldt = t
    
def mouseClicked():
  global oldt, t0
  t0 = millis()
  oldt = t0/1000.0
