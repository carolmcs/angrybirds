# Posição e velocidade inicial
p = PVector(10, 500)
v = PVector(200, 0)
# Gravidade
g = PVector(0, -9.8)
f = 0.01   #constante da força de retardo
# Limites da tela
xmin = 5
xmax = 700
ymin = 0
ymax = 550

oldt = millis()/1000.0 #instante inicial



def setup():
    size(800,800)
    rectMode(CORNERS)
    
def draw():
    global oldt,p, v
    #cálculo da força de retardo para o corpo 1
    F = v.copy()
    F.mult(-f)
    #força total sobre o corpo 1
    F.add(g)
    #tempo transcorrido desde último desenho
    t = millis()/1000.00
    dt = t- oldt
    oldt = t
    #atualização da posição do corpo
    dp = v.copy()
    dp.mult(dt)
    p.add(dp)
    #variação de velocidade (força*delta(t)/masssa)
    F.mult(dt)
    #atualização da velocidade
    v.add(F)
    
    #verificação de colisão
    if p.x > xmax:
        p.x = xmax - (p.x-xmax)
        v.x = -v.x
    if p.x < xmin:
        p.x = xmin + (xmin - p.x)
        v.x = -v.x
    if p.y > ymax:
        p.y = ymax - (p.y - ymax)
        v.y = -v.y
    if p.y < ymin:
        p.y = ymin + (ymin - p.y)
        v.y = -v.y
        
        
    


    
    #desenho dos sorpos 
    background(225)
    fill(255,0,0)
    ellipse(p.x, 600- p.y, 10, 10)
    noFill()
    strokeWeight(3)
    stroke(0)
    rect(xmin, 600 - ymax, xmax, 600 - ymin)
    noStroke()