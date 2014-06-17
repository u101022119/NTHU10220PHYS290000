# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 17:42:35 2014

@author: riverbird
"""

import pygame,sys,os,random
pygame.init()
        #catcher
class rect():
    def __init__(self,filename,initial_position):
        self.image=pygame.image.load(filename)
        self.rect=self.image.get_rect()
        self.rect.topleft=initial_position
        #the ball
class goldrect(pygame.sprite.Sprite):
    def __init__(self,ball_position,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('image\\x.jpg')
        self.rect=self.image.get_rect()
        self.rect.topleft=ball_position
        self.speed=speed
    def move(self):
        self.rect=self.rect.move(self.speed)

        
        

       #背景圖片
def drawback(): 
    background=pygame.image.load('image\\background.jpg') 
    bakscreen.blit(background,[0,0])

        #繪出成績、level、最高分等
def loadtext(levelnum,score,highscore):
    my_font=pygame.font.SysFont(None,24)
    levelstr='Level:'+str(levelnum)
    text_screen=my_font.render(levelstr, True, (255, 0, 0))
    bakscreen.blit(text_screen, (650,50))
    highscorestr='Higescore:'+str(highscore)
    text_screen=my_font.render(highscorestr, True, (255, 0, 0))
    bakscreen.blit(text_screen, (650,80))
    scorestr='Score:'+str(score)
    text_screen=my_font.render(scorestr, True, (255, 0, 0))
    bakscreen.blit(text_screen, (650,110))    
          #繪出GAME OVER 
def loadgameover(scorenum,highscore):
    gg_sister=pygame.image.load('image\\gg.jpg')
    bakscreen.blit(gg_sister,[0,0])
    gg_handsome=pygame.image.load('image\\handsome.jpg')
    bakscreen.blit(gg_handsome,[0,300])
    my_font=pygame.font.SysFont(None,50)
    levelstr='GAME OVER'
    over_screen=my_font.render(levelstr, True, (255, 0, 0))
    bakscreen.blit(over_screen, (300,240))
    highscorestr='YOUR SCORE IS '+str(scorenum)
    over_screen=my_font.render(highscorestr, True, (255, 0, 0))
    bakscreen.blit(over_screen, (280,290))
            #寫入最高分
    if scorenum>int(highscore):
        highscorestr='YOUR HAVE GOT THE HIGHEST SCORE!'
        text_screen=my_font.render(highscorestr, True, (255, 0, 0))
        bakscreen.blit(text_screen, (100,340))
        highfile=open('highscore','w')
        highfile.writelines(str(scorenum))  
        highfile.close()
            #讀取最高分
def gethighscore(): 
    if os.path.isfile('highscore'):
        highfile=open('highscore','r')
        highscore=highfile.readline() 
        highfile.close() 
    else:
        highscore=0
    return highscore
                  
bakscreen=pygame.display.set_mode([800,600])
bakscreen.fill([0,160,233])
pygame.display.set_caption('xul4s')
drawback()


#起始條件
levelnum=1
scorenum=0
highscore=gethighscore()
ileft=1  #向左移動步數
iright=10 #向右移動步數
x=100
y=450
filename='image\\1.jpg'
backimg_ren=rect(filename,[x,y])
bakscreen.blit(backimg_ren.image,backimg_ren.rect)
loadtext(levelnum,scorenum,highscore)
ballx=random.randint(0,700)
V=3*levelnum #速度＝等級五倍
speed=[random.randint(-V,V),V]
my_ball=goldrect([ballx,100],speed) 
pygame.display.update()

while True:
    if scorenum>0 and scorenum/50.0==int(scorenum/50.0):#當得分是50的倍數時修改level
        levelnum=scorenum/50+1
        V=5*levelnum
        speed=[random.randint(-V,V),V]
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()    
             #移動
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_LEFT]:#按下左鍵

        drawback()  
        loadtext(levelnum,scorenum,highscore)

        if iright > 14 :iright=10
        iright=iright+1
        filename='image\\'+str(iright)+'.jpg'
        if x<0 :
            x=0
        else:
            x=x-20

        backimg_surface=rect(filename,[x,y])
        bakscreen.blit(backimg_surface.image,backimg_surface.rect)

        
    if pressed_keys[pygame.K_RIGHT]:#按下右鍵

        drawback()
        loadtext(levelnum,scorenum,highscore)

        if ileft > 4 :ileft=0
        ileft=ileft+1
        filename='image\\'+str(ileft)+'.jpg'
        if x>700:
            x=700
        else:
            x=x+20

        backimg_surface=rect(filename,[x,y])
        bakscreen.blit(backimg_surface.image,backimg_surface.rect)

    
    if pressed_keys[pygame.K_DOWN]:#按下下鍵

        drawback()
        loadtext(levelnum,scorenum,highscore)

        if y>500:
            y=500
        else:
            y=y+20

        backimg_surface=rect(filename,[x,y])
        bakscreen.blit(backimg_surface.image,backimg_surface.rect)
        

    if pressed_keys[pygame.K_UP]:#按下上鍵

        drawback()
        loadtext(levelnum,scorenum,highscore)

        if y<0:
            y=0
        else:
            y=y-20

        backimg_surface=rect(filename,[x,y])
        bakscreen.blit(backimg_surface.image,backimg_surface.rect)
    drawback()
    loadtext(levelnum,scorenum,highscore)
    my_ball.move()
    bakscreen.blit(my_ball.image,my_ball.rect) 
    
    backimg_surface=rect(filename,[x,y])
    bakscreen.blit(backimg_surface.image,backimg_surface.rect)
    if my_ball.rect.top>600:#判斷ball是否着地，一但着地，遊戲結束
        loadgameover(scorenum,highscore)
    if my_ball.rect.colliderect(backimg_surface.rect):#判斷ball是否與catcher接觸
        scorenum+=5
        loadtext(levelnum,scorenum,highscore)
        ballx=random.randint(00,700)
        speed=[random.randint(-V,V),V]
        my_ball=goldrect([ballx,100],speed) 
    pygame.display.update()