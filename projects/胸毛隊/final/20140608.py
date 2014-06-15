
import sys, time, random, copy, os
from math import *
import pygame as pyg
import pygame.display as dsp
pyg.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50,50)

##Color
BLACK = (0,0,0) 
GRAY = (220,220,220)  
WHITE=(255,255,255)
BLUE=(0,0,255)
RED=(255,0,0)
YELLOW=(255,255,0)
SKYBLUE=(0,255,255)
GREEN=(0,255,0)
PINK=(255,0,255)

##parameter
spd_player = 10
size_player = 20,20

spd_enemy = 15
size_enemy = 15,15
dist_enemy = 300

spd_shoot = 7
line_shoot = 10.0

##Frame initializtion
size = width, height = 1600, 900
scr_main = dsp.set_mode(size)     #build a frame
dsp.set_caption("New game")     #set a name for this game
pyg.mouse.set_visible(False)
dsp.flip()

## status
size_s = 10, height
scr_s = pyg.Surface(size_s)
scr_s.fill(BLACK)   
     
## player
size_p = width_p, height_p = width-10, height
scr_p = pyg.Surface(size_p)

## Refresh
def Refresh (scr,scr_p,scr_s):    
    scr.blit(scr_p,(0,0))
    scr.blit(scr_s,(width_p,0))
    dsp.flip()
     
##Player
class Player(pyg.sprite.Sprite) :
    #image = pyg.image.load(r'C:\Users\evanliu\Desktop\software\python\final\aircraft_1.jpg').convert()    
    rect = pyg.Rect((0,0),size_player)
    pos = 0,0
    spd = spd_player
    t = 0
    def __init__(self,pos):
        pyg.sprite.Sprite.__init__(self)
        self.rect.center = pos
        self.pos = self.rect.center
    def PlayerMove (self,scr_p):    
        KeyMove = [pyg.K_LEFT,pyg.K_RIGHT,pyg.K_UP,pyg.K_DOWN]
        KeyMove2 = [pyg.K_a,pyg.K_d,pyg.K_w,pyg.K_s]
        press = pyg.key.get_pressed()
        x,y = self.rect.topleft
        dx = dy = self.spd
        Test = [press[i] for i in KeyMove]
        t_bc = test_bc(player,scr_p)
        if Test[0] == 1 and t_bc[0]:
            x -= dx
        if Test[1] == 1 and t_bc[1]:
            x += dy
        if Test[2] == 1 and t_bc[2]:
            y -= dy 
        if Test[3] == 1 and t_bc[3]:
            y += dy
        Test = [press[i] for i in KeyMove2]
        t_bc = test_bc(player,scr_p)
        if Test[0] == 1 and t_bc[0]:
            x -= dx
        if Test[1] == 1 and t_bc[1]:
            x += dy
        if Test[2] == 1 and t_bc[2]:
            y -= dy 
        if Test[3] == 1 and t_bc[3]:
            y += dy
        self.rect.topleft = x,y
        self.pos = self.rect.center
        #pyg.draw.circle(scr_p,GRAY,self.rect.center,dist_enemy)
        pyg.draw.rect(scr_p,GREEN,self.rect)
        
##enemy
class Enemy(pyg.sprite.Sprite) :
    rect = pyg.Rect((0,0),size_enemy)
    pos = 0,0
    vel = 0,0
    spd = spd_enemy
    detect, run, sleep = False, 1, 30
    def __init__(self,pos):
        pyg.sprite.Sprite.__init__(self)
        self.rect = pyg.Rect(pos,size_enemy)
        self.pos = self.rect.center
        spd = self.spd
        self.vel = random.randint(-spd/2,spd/2),random.randint(-spd/2,spd/2)
        
    def EnemyMove (self,player,scr_p):
        x,y = self.pos
        vx,vy = self.vel
        dx,dy = player.pos
        dx,dy = dx-x,dy-y
        l = sqrt(dx*dx+dy*dy)
        #Detection
        if  (l < dist_enemy) and (self.detect is False):
            vx,vy = dx/l*self.spd,dy/l*self.spd
            self.detect = True
            self.run = -5
        #Color
        if self.detect is True:
            self.color = RED
        else:
            self.color = BLUE
        #Boundary
        t_bc = test_bc(self,scr_p)
        if (t_bc[0] and t_bc[1]) is False:
            vx = -vx
        if (t_bc[2] and t_bc[3]) is False:
            vy = -vy
        #Move
        if self.run > 0 and self.sleep < 0:         ##if t != 0, enemy dont move
            x, y = x+vx ,y+vy
        #Output         
        self.sleep -= 1
        self.run +=1
        self.pos = x,y
        self.vel = vx,vy
        self.rect.topleft = int(x),int(y)
        pyg.draw.rect(scr_p,self.color,self.rect)
        
def EnemyCreate(enemy,player,n):
    for i in range(n):
        while True:
            x = random.randint(100,width_p-100)     
            y = random.randint(100,height-100)
            dx,dy = player.pos
            dx,dy = dx-x,dy-y
            l = sqrt(dx*dx+dy*dy)
            if l > 1.5*dist_enemy:
                break
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
        pyg.draw.line(scr_p, PINK, (x,y), (x+lx,y+ly),3) ##draw
        t = test_bc(self,scr_p)     ##boundary test
        if False in t:
            return "OUT"
        return "OK"
        
def Fire(enemy,shoot):
    if enemy.t > 0:         ##loading
        enemy.t -= 1
        return "RELOADING"
    press = pyg.key.get_pressed()
    if press[pyg.K_SPACE]:
        shoot.add(Shoot(enemy.rect.center))
        enemy.t = 10

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
    t = pyg.sprite.groupcollide(shoot,enemy,False,False)
    return len(t)
    
def test_sp (shoot,player): 
    t = pyg.sprite.groupcollide(shoot,player,True,False)
    return len(t)
    
def test_pe (player,enemy): 
    t = pyg.sprite.spritecollide(player,enemy,False)
    return t

def test_ee (enemy_red,enemy_blue):
    t = pyg.sprite.groupcollide(enemy_red,enemy_blue,True,True)
    return t

##main
player = Player((width_p/2,height_p/2))
enemy_blue = pyg.sprite.Group()
enemy_red = pyg.sprite.Group()
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
                EnemyCreate(enemy_blue,player,5)
    ##Initialize frame   
    scr_p.fill(WHITE)
    ##PlayerMove
    player.PlayerMove(scr_p)
    ##EnemyShoot
#    Fire(enemy,shoot)
#    for i in shoot.sprites():
#        if False in test_bc(i,scr_p):
#            shoot.remove(i)
#        else:
#            i.Move(scr_p)
    ##Enemy Creation
    if gametime%25 is 0:
        EnemyCreate(enemy_blue,player,gametime/1000+1)
    ##Enemy Blue Moving
    for i in enemy_blue.sprites():
        i.EnemyMove(player,scr_p)
    ##Enemy Red Moving
    for i in enemy_red.sprites():
        i.EnemyMove(player,scr_p)
    ##Color Changing
    for i in enemy_blue.sprites():
        if i.color is RED:
            enemy_blue.remove(i)
            enemy_red.add(i)
    for i in enemy_red.sprites():
        if i.color is BLUE:
            enemy_red.remove(i)
            enemy_blue.add(i)
    ##Enemy Collision
    test = test_ee(enemy_red,enemy_blue)
    score += len(test)
    ##Life
    if test_pe(player,enemy_red) != []:
        run = False
    ##Frame refresh
    Refresh(scr_main,scr_p,scr_s)
    dsp.flip()
    time.sleep(0.01)
    gametime += 1

pyg.quit()
print "Game Over !!"
print "Your Score :", score
raw_input("Press Enter to continue...")
##sys.exit()
