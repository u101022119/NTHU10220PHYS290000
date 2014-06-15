
import sys, time, random, copy
from math import *
import pygame as pyg
import pygame.display as dsp
pyg.init()

##Color
BLACK = (0,0,0)   
WHITE=(255,255,255)
BLUE=(0,0,255)
RED=(255,0,0)
GREEN=(0,255,0)

##parameter
spd_player = 10
reload_player = 5

num_shoot = 1

spd_enemy = 5
size_enemy = 20,20

spd_shoot = 7
line_shoot = 10.0

##Frame initializtion
size = width, height = 800, 800
scr_main = dsp.set_mode(size)     #build a frame
dsp.set_caption("New game")     #set a name for this game
pyg.mouse.set_visible(True)
dsp.flip()

## status
size_s = 100, height
scr_s = pyg.Surface(size_s)
scr_s.fill(BLACK)   
     
## player
size_p = width_p, height_p = width-100, height
scr_p = pyg.Surface(size_p)

## Refresh
def Refresh (scr,scr_p,scr_s):    
    scr.blit(scr_p,(0,0))
    scr.blit(scr_s,(width_p,0))
    dsp.flip()
     
##Player
class Player(pyg.sprite.Sprite) :
    image = pyg.image.load(r'C:\Users\evanliu\Desktop\software\python\final\aircraft_1.jpg').convert()
    rect = image.get_rect()
    rect2 = image.get_rect()
    spd = spd_player
    t = 0
    def __init__(self,pos):
        pyg.sprite.Sprite.__init__(self)
        w,h = self.rect.size
        self.rect2.size = int(w*0.5),int(h*0.5)
        self.rect.topleft = pos
        self.rect2.topleft = pos
    def PlayerMove (self,scr_p):    
        KeyMove = [pyg.K_LEFT,pyg.K_RIGHT,pyg.K_UP,pyg.K_DOWN]
        press = pyg.key.get_pressed()
        Test = [press[i] for i in KeyMove]
        t_bc = test_bc(player,scr_p)
        x,y = self.rect.topleft
        dx = dy = self.spd
        if Test[0] == 1 and t_bc[0]:
            x -= dx
        if Test[1] == 1 and t_bc[1]:
            x += dy
        if Test[2] == 1 and t_bc[2]:
            y -= dy 
        if Test[3] == 1 and t_bc[3]:
            y += dy
        self.rect.topleft = (x,y)
        self.rect2.center = self.rect.center
        scr_p.blit(self.image,(self.rect.topleft))
        
##enemy
class Enemy(pyg.sprite.Sprite) :
    #image = pyg.image.load(r'C:\Users\evanliu\Desktop\software\python\final\aircraft_1.jpg').convert()
    rect = pyg.Rect((0,0),size_enemy)
    spd = spd_enemy
    def __init__(self,pos):
        pyg.sprite.Sprite.__init__(self)
        self.rect = pyg.Rect(pos,size_enemy)
    def EnemyMove (self,player,scr_p):
        #scr_p.blit(self.image,(self.rect.topleft))
        x,y = self.rect.topleft
        dx,dy = player.rect.center
        dx,dy = dx-x,dy-y
        l = sqrt(dx*dx+dy*dy)
        dx,dy = dx/l*self.spd,dy/l*self.spd
        #if dy <= 0:
        #    dy = 10
        x,y = x+dx,y+dy
        self.rect.topleft = (x,y)
        pyg.draw.rect(scr_p,GREEN,self.rect)
        
def EnemyCreate(enemy,n):
    for i in range(n):
        x = random.randint(0,width_p)     
        y = random.randint(0,100)
        enemy.add(Enemy((x,y)))
    return enemy
     


## fire
class Shoot(pyg.sprite.Sprite):
    rect = pyg.Rect((0,0),(1,1))
    v = 0, -spd_shoot
    line = line_shoot
    def __init__(self,pos):
        pyg.sprite.Sprite.__init__(self)
        self.rect = pyg.Rect(pos,(1,1))
    def Move(self,scr_p):
        x, y = self.rect.center
        vx, vy = self.v
        l = self.line/(sqrt(vx**2 + vy**2))
        lx, ly = vx *l, vy*l
        x += vx                   ##new position
        y += vy
        self.rect.center = (x, y)
        pyg.draw.line(scr_p, RED, (x,y), (x+lx,y+ly),3) ##draw
        t = test_bc(self,scr_p)     ##boundary test
        if False in t:
            return "OUT"
        return "OK"
        
def Fire(player,shoot):
    if player.t > 0:         ##loading
        player.t -= 1
        return "RELOADING"
    press = pyg.key.get_pressed()
    if press[pyg.K_SPACE]:
        x,y = player.rect.midtop
        for i in range(-num_shoot+1,num_shoot):
            lx = i*10
            shoot.add(Shoot((x+lx,y)))
        player.t = reload_player

##collision test
def test_bc (player,screen): 
    rp = player.rect
    rs = screen.get_rect()
    t = [0]*4                       ##initialize
    t[0] = rp.left >= rs.left       ##left
    t[1] = rp.right <= rs.right     ##right    
    t[2] = rp.top >= rs.top         ##top
    t[3] = rp.bottom <= rs.bottom   ##bottom
    return t 
    
def test_se (shoot,enemy): 
    t = pyg.sprite.groupcollide(shoot,enemy,True,False)
    return len(t)
    
def test_pe (player,enemy): 
    temp = player.rect
    player.rect = player.rect2    
    t = pyg.sprite.spritecollide(player,enemy,False)
    player.rect = temp
    return t
           
##main
player = Player((width_p/2,height_p-100))
enemy = pyg.sprite.Group()
shoot = pyg.sprite.Group()
gametime = 0
score = 0
run = True
while run:
    for event in pyg.event.get():
        if event.type is pyg.KEYDOWN:
            keyname = event.key
            if keyname is pyg.K_ESCAPE:  
                run = False
            if keyname is pyg.K_b:
                EnemyCreate(enemy,5)
                
    scr_p.fill(WHITE)
    
    score += test_se(shoot,enemy)
    if test_pe(player,enemy) != []:
        run = False
    
    player.PlayerMove(scr_p)
    
    if score > num_shoot**2*45:
        num_shoot += 1 
    Fire(player,shoot)
    for i in shoot.sprites():
        if False in test_bc(i,scr_p):
            shoot.remove(i)
        else:
            i.Move(scr_p)
    
    if gametime%100 is 0:
        EnemyCreate(enemy,gametime/100)
    for i in enemy.sprites():
        if False in test_bc(i,scr_p):
            enemy.remove(i)
        else:
            i.EnemyMove(player,scr_p)
                
    Refresh(scr_main,scr_p,scr_s)
    dsp.flip()
    time.sleep(0.01)
    gametime += 1

pyg.quit()
print "Game Over !!"
print "Your Score :", score
raw_input("Press Enter to continue...")
##sys.exit()
