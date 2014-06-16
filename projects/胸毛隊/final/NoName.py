
import sys, time, random, copy, os
from math import *
import pygame as pyg
import pygame.display as dsp
pyg.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50,50)

##Color
BLACK = (0,0,0)
GRAY_b = (100,100,100)
GRAY = (200,200,200)
WHITE=(255,255,255)
BLUE=(0,0,255)
RED=(255,0,0)
YELLOW=(255,255,0)
SKYBLUE=(0,255,255)
GREEN=(0,255,0)
PINK=(255,0,255)

##parameter
size_font = 24
fps = 100.0
color_background = GRAY_b
dmg_shoot = 1
dmg_enemy = 10

image_player = pyg.image.load('player.png')
spd_player = 15
size_player = image_player.get_rect().size
life = 100

image_red = pyg.image.load('red.png')
image_blue = pyg.image.load('blue.png')
spd_enemy_init = spd_enemy = 15
size_enemy = image_red.get_rect().size
dist_enemy = 150

spd_shoot = 20
line_shoot = 10.0
size_shoot = 7
t_reload = 70
color_shoot = PINK

##Frame initializtion
size = width, height = 1000, 800
scr_main = dsp.set_mode(size)     #build a frame
dsp.set_caption("New game")     #set a name for this game
pyg.mouse.set_visible(False)
dsp.flip()

## status
size_s = width_s, height_s = 100, height 
scr_s = pyg.Surface(size_s)
scr_s.fill(BLACK)   
     
## player
size_p = width_p, height_p = width-width_s, height
scr_p = pyg.Surface(size_p)

## Refresh
def Refresh (scr,scr_p,scr_s):    
    scr.blit(scr_p,(0,0))
    scr.blit(scr_s,(width_p,0))
    dsp.flip()

##Font initialization
def BuildFont(string,pos,scr_s,color = WHITE):
    basicFont = pyg.font.SysFont(None,size_font)
    text = basicFont.render(string, False, color)
    textRect = text.get_rect()
    textRect.center = pos
    scr_s.blit(text,textRect)
  
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
        t_bc = test_bc(self,scr_p)
        if Test[0] == 1 and t_bc[0]:
            x -= dx
        if Test[1] == 1 and t_bc[1]:
            x += dy
        if Test[2] == 1 and t_bc[2]:
            y -= dy 
        if Test[3] == 1 and t_bc[3]:
            y += dy
        Test = [press[i] for i in KeyMove2]
        t_bc = test_bc(self,scr_p)
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
        pyg.draw.circle(scr_p,GRAY,self.rect.center,dist_enemy)
        pyg.draw.rect(scr_p,GREEN,self.rect)
        scr_p.blit(image_player,self.rect.topleft)
    def PlayerMove_Cheat (self,scr_p,key):
        x,y = self.rect.topleft
        dx = dy = self.spd
        Test = key
        t_bc = test_bc(self,scr_p)
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
        pyg.draw.circle(scr_p,GRAY,self.rect.center,dist_enemy)
        pyg.draw.rect(scr_p,GREEN,self.rect)
        scr_p.blit(image_player,self.rect.topleft)
        
##cheat
def Cheat(player,enemy):
    KeyMove = [pyg.K_LEFT,pyg.K_RIGHT,pyg.K_UP,pyg.K_DOWN]
    key = [0,0,0,0]
    lmax = 100
    x,y = player.rect.center
    dx,dy = width_p/2.0,height_p/2.0
    dx,dy = dx-1.0*x,dy-1.0*y
    l = sqrt(dx*dx+dy*dy+1)
    vx,vy = -dx/l,-dy/l
    for i in enemy.sprites():
        dx,dy = i.rect.center
        dx,dy = dx-1.0*x,dy-1.0*y
        l = sqrt(dx*dx+dy*dy)
        if l < lmax:
            lmax = l
            vx,vy = dx/l,dy/l
    if vx < -0.7:
        key[1] = 1
    elif vx > 0.7:
        key[0] = 1
    if vy < -0.7:
        key[3] = 1
    elif vy > 0.7:
        key[2] = 1
    return key
        
##enemy
class Enemy(pyg.sprite.Sprite) :
    rect = pyg.Rect((0,0),size_enemy)
    pos = 0,0
    vel = 0,0
    spd = 0
    detect, run, sleep = False, 1, 30
    t = t_reload
    def __init__(self,pos):
        pyg.sprite.Sprite.__init__(self)
        self.rect = pyg.Rect(pos,size_enemy)
        self.pos = self.rect.center
        self.spd = spd_enemy
        spd = int(self.spd)
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
        if self.color is RED:
            scr_p.blit(image_red,self.rect.topleft)
        elif self.color is BLUE:
            scr_p.blit(image_blue,self.rect.topleft)
        
def EnemyCreate(enemy,player,n):
    for i in range(n):
        while True:
            x = random.randint(100,width_p-100)     
            y = random.randint(100,height-100)
            dx,dy = player.pos
            dx,dy = dx-x,dy-y
            l = sqrt(dx*dx+dy*dy)
            if l > dist_enemy+50:
                break
        enemy.add(Enemy((x,y)))
    return enemy
     
## fire
class Shoot(pyg.sprite.Sprite):
    pos = 0,0
    rect = pyg.Rect((0,0),(1,1))
    v = 0, 0
    line = line_shoot
    def __init__(self,pos,player):
        pyg.sprite.Sprite.__init__(self)
        self.rect = pyg.Rect(pos,(1,1))
        self.pos = self.rect.center
        dx,dy = player.rect.center
        dx,dy = dx - pos[0]*1.0,dy - pos[1]*1.0
        l = sqrt(dx*dx + dy*dy)
        self.v = dx/l*spd_shoot,dy/l*spd_shoot
    def Move(self,scr_p):
        x, y = self.pos
        vx, vy = self.v
        l = self.line/(sqrt(vx**2 + vy**2))
        lx, ly = vx *l, vy*l
        x += vx                   ##new position
        y += vy
        self.pos = (x, y)
        x,y = self.rect.center = int(x),int(y)
        pyg.draw.line(scr_p, color_shoot, (x,y), (x+lx,y+ly),size_shoot) ##draw
        t = test_bc(self,scr_p)     ##boundary test
        if False in t:
            return "OUT"
        return "OK"
        
def Fire(enemy,shoot):
    for i in enemy.sprites():
        if i.t > 0:         ##loading
            i.t -= 1
        else:
            shoot.add(Shoot(i.rect.center,player))
            i.t = t_reload

##collision test
def test_bc (player,screen): 
    rp = player.rect
    rs = screen.get_rect()
    t = [0]*4                       ##initialize
    t[0] = rp.left > rs.left       ##left
    t[1] = rp.right < rs.right     ##right    
    t[2] = rp.top > rs.top         ##top
    t[3] = rp.bottom < rs.bottom   ##bottom
    return t 
    
def test_se (shoot,enemy): 
    t = pyg.sprite.groupcollide(shoot,enemy,False,False)
    return len(t)
    
def test_sp (shoot,player): 
    t = pyg.sprite.spritecollide(player,shoot,True)
    return t
    
def test_pe (player,enemy): 
    t = pyg.sprite.spritecollide(player,enemy,True)
    return t

def test_ee (enemy_red,enemy_blue):
    t = pyg.sprite.groupcollide(enemy_red,enemy_blue,True,True)
    return t

##main
player = Player((width_p/2,height_p/2))
enemy_blue = pyg.sprite.Group()
enemy_red = pyg.sprite.Group()
shoot = pyg.sprite.Group()
score = 0
gametime = 0
run = True
cheat = False
pause = False
time_start = time.clock()
while run:
    for event in pyg.event.get():
        if event.type is pyg.KEYDOWN:
            keyname = event.key
            if keyname is pyg.K_ESCAPE:  
                run = False
##            elif keyname is pyg.K_b:
##                EnemyCreate(enemy_blue,player,100)
            elif keyname is pyg.K_c:
                cheat = not cheat
            elif keyname is pyg.K_z and dist_enemy < 200:
                dist_enemy += 50
            elif keyname is pyg.K_x and dist_enemy > 100:
                dist_enemy -= 50
            elif keyname is pyg.K_SPACE:
                pause = not pause
    ##Pause
    if pause is True:
        continue
    ##Initialize frame   
    scr_p.fill(color_background)
    ##PlayerMove
    if cheat is True:
        key = Cheat(player,enemy_red)
        player.PlayerMove_Cheat(scr_p,key)
    else:
        player.PlayerMove(scr_p)
    ##EnemyShoot
    Fire(enemy_blue,shoot)
    for i in shoot.sprites():
        if False in test_bc(i,scr_p):
            shoot.remove(i)
        else:
            i.Move(scr_p)
    ##Enemy Creation
    if gametime%100 is 0:
        EnemyCreate(enemy_blue,player,int(gametime/500)+1)
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
    score += len(test)*spd_enemy
    ##Speed up
    spd_enemy = int(spd_enemy_init*(1+score/1000))
    ##Life
    if test_pe(player,enemy_red) != []:
        life -= dmg_enemy
    if test_sp(shoot,player) != []:
        life -= dmg_shoot
    if life <= 0:
        run =False
        basicFont = pyg.font.SysFont(None,150)
        text = basicFont.render("GAME OVER", False, BLACK)
        textRect = text.get_rect()
        textRect.center = scr_p.get_rect().center
        scr_p.blit(text,textRect)
    if life > 25:
        BuildFont(str(life)+'%',player.rect.midbottom,scr_p,BLACK)
    else:
        BuildFont(str(life)+'%',player.rect.midbottom,scr_p,RED)
    ##Status
    scr_s.fill(BLACK)
    x = scr_s.get_rect().centerx
    y = 50
    BuildFont('NEW GAME',(x,50),scr_s)
    
    y +=50
    BuildFont('--- Time ---',(x,y),scr_s)
    y +=20
    BuildFont('{:.2f}'.format(time.clock() - time_start),(x,y),scr_s)
    
    y +=50
    BuildFont('--- Score ---',(x,y),scr_s)
    y +=20
    BuildFont(str(score),(x,y),scr_s)
    
    y +=50
    BuildFont('--- Life ---',(x,y),scr_s)
    y +=20
    str_life = str(life)+"%"
    BuildFont(str_life,(x,y),scr_s)
    
    y +=50
    BuildFont('--- Speed ---',(x,y),scr_s)
    y +=20
    BuildFont(str(spd_enemy),(x,y),scr_s)
    
    y +=50
    BuildFont('--- # of Red ---',(x,y),scr_s)
    y +=20
    BuildFont(str(len(enemy_red.sprites())),(x,y),scr_s)
    
    y +=50
    BuildFont('--- # of Blue ---',(x,y),scr_s)
    y +=20
    BuildFont(str(len(enemy_blue.sprites())),(x,y),scr_s)

    ##Cheat
    if cheat is True:
        color_background = GRAY_b
        life = 100
        basicFont = pyg.font.SysFont(None,150)
        text = basicFont.render("C H E A T I N G", False, BLACK)
        textRect = text.get_rect()
        textRect.center = scr_p.get_rect().center
        scr_p.blit(text,textRect)
    ##Frame refresh
    Refresh(scr_main,scr_p,scr_s)
    dsp.flip()
    if cheat is False:
        time.sleep(1/fps)
    gametime += 1

time.sleep(1)

pyg.quit()
print "Game Over !!"
print "Your Score :", score
print "Game Time :", '{:.2f}'.format(time.clock() - time_start)
raw_input("Press Enter to continue...")
##sys.exit()
