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
k = 400

def setup():
  size(1200,600)

def draw():
    global x0, y0, vx0, vy0,p_ovox,p_ovoy, t0,x,y,k
    t = (millis()-t0)/1000.0  
    x = (x0 + vx0*t)
    vy = vy0 + 1000*t
    y = (y0 + vy0*t+ 500*t*t)
    background(169, 216, 229)
    stroke(0)
    fill(238,231,203)
    ellipse(x,y, 25, 25)
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
    v = (p_ovoy + vovo*t + 500*t*t)
    fill(255)
    ellipse(p_ovox,v,10,15)
    if (x-685-k)**2 + (y-575)**2 <= 900 or (p_ovox-685-k)**2 + (v-575)**2 <= 900:
      fill(169,216,229)
      noStroke()
      ellipse(685+k,575, 80,80)
    
def mouseClicked():
    global x,y,vy0,t0,x0,y0,p_ovoy,p_ovox,vovo
    t = (millis()-t0)/1000.0
    p_ovox = x
    p_ovoy = y
    vy = vy0 + 1000*t
    vy0 = vy - 1000
    vovo = vy
    x0 = x
    y0 = y
    t0 = millis()
