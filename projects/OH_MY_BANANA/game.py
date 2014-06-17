# -*- coding: utf-8 -*-
"""
Created on Sat May 31 15:29:34 2014

@author: Saber
"""

import sys,time,pygame,math,random
from pygame.locals import *
from numpy import *

pygame.init()
#mouse collition --------------------------------------------
def mouseclick(x,y,x1,y1,x_,y_):
    if x>x1 and x<x1+x_:
        if y>y1 and y<y1+y_:
            return True
        else:
            pass
        
#ball collition ---------------------------------------------
def ballcol(x,y,x1,y1,r,r1):
    rr=int(((x-x1)**2+(y-y1)**2)**0.5)
    if rr<=r+r1:
        return True
    else:
        pass
#light collition---------------------------------------------
def lightcol(x,y,x1,y1):
    rrx = abs(x-x1)
    rry = abs(y-y1)
    if rrx <= 26 or rry <= 26:
        return True
    else:
        pass
dex=1
#creat balltraps----------------------------------------------
class balltraps(object):
    number = 0
    vb = []
    bax = []
    bay = []
    vorh_ball = []
    warnx = []
    warny = []
    def _init_(self):
        self.number = 0
        self.vb = []
        self.bax = []
        self.bay = []
        self.vorh_ball = []
        self.warnx = []
        self.warny = []
    def creatballs(self,number):  #產生球的屬性資料
        self.number = number
        self.bax = zeros(number, int)
        self.bay = zeros(number, int)
        self.vb = zeros(number, int)
        self.vorh_ball = zeros(number,int)
        self.warnx=zeros(number,int)
        self.warny=zeros(number,int)
        for i in range(number):
            self.vb[i] = random.randint(3,7)
            self.vorh_ball[i]=random.randint(0,4)
            if self.vorh_ball[i] == 0:
                self.bax[i] = 100
                self.warnx[i]=self.bax[i]
                ky = random.randint(0,9)        #從左邊進場       
                self.bay[i] = 150 + 50*ky
                self.warny[i]=self.bay[i]
            elif self.vorh_ball[i] == 1:
                kx = random.randint(0,9)
                self.bax[i] = 150 + 50*kx#從上邊進場
                self.warnx[i]=self.bax[i]
                self.bay[i] = 100
                self.warny[i]=self.bay[i]
            elif self.vorh_ball[i] == 2:
                ky = random.randint(0, 9)
                self.bax[i] = 600
                self.bay[i] = 150 + 50*ky
                self.warnx[i] = self.bax[i]
                self.warny[i] = self.bay[i]
            elif self.vorh_ball[i] == 3:
                kx = random.randint(0,9)
                self.bax[i] = 150 + 50*kx#從下邊進場
                self.warnx[i]=self.bax[i]
                self.bay[i] = 600
                self.warny[i]=self.bay[i]
# create light trap ---------------------------------------
class lighttrap(object):
    number=0
    lix=[]
    liy=[]
    def _init_(self):
        self.number=0
        self.lix=[]
        self.liy=[]
        self.vorh_light=[]
    def createlights(self,number):
        self.number=number
        self.lix=zeros(number,int)
        self.liy=zeros(number,int)
        self.vorh_light=zeros(number,int)
        self.warnx=zeros(number,int)
        self.warny=zeros(number,int)
        for i in range(number):
            self.vorh_light[i]=random.randint(0,2)
            if self.vorh_light[i]==0:
                self.lix[i]=74
                self.warnx[i]=self.lix[i]
                ky=random.randint(0,10)
                self.liy[i]=125+50*ky
                self.warny[i]=self.liy[i]
            elif self.vorh_light[i]==1:
                kx=random.randint(0,10)
                self.lix[i]=125+50*kx
                self.warnx[i]=self.lix[i]
                self.liy[i]=74
                self.warny[i]=self.liy[i]
                
                
#gamestart -----------------------------------------------
def gamestart(dex):
    ball = balltraps()
    ball2 = balltraps()
    light=lighttrap()
    traptype=0
    leftbound = 100
    rightbound = 600
    upbound = 100
    lowbound = 600
    overmove_ball1 = 0
    overmove_ball2 = 0
    overmove_light=0
    done=False
    font1=pygame.font.SysFont('Calibri',25,True,False)
    pygame.mouse.set_visible(False)
    velocity=5
    dx=0
    dy=0
    velocity=velocity*dex
    radius=10
    radius_rock=20
    show=1
    change=-1
    wait=0
    wait2=3
    traptype=0
    lit=1
    ball2start = 0
    a = 0
    s=0
#vb=velocity of ball   

    px=(leftbound+rightbound)/2
    py=(upbound+lowbound)/2

    time=0
    while not done:
        temp=0
        templ=0
        tempball2=0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:            
                done=True
            if event.type == pygame.KEYDOWN:
                if event.key==K_LEFT:
                    dx=-1*velocity
                if event.key==K_RIGHT:
                    dx=1*velocity
                if event.key==K_UP:
                    dy=-1*velocity
                if event.key==K_DOWN:
                    dy=1*velocity
                if event.key==K_s:
                    show=show*(-1)
                if event.key==K_m:
                    change=change*(-1)
                print('user pressed a button')
            if event.type == pygame.KEYUP:
                if event.key==K_LEFT or event.key==K_RIGHT:
                    dx=0
                if event.key==K_UP or event.key==K_DOWN:                    
                    dy=0
                print('user release a button')
            if event.type == pygame.MOUSEBUTTONDOWN:
                print('user pressed mouse button')
                done=True
            if event.type == pygame.MOUSEBUTTONUP:
                print('user release a mouse button')
        
        if (time/60)>30 :
            traptype = 1
            
        if traptype==0:#產生球
            if overmove_ball1 == ball.number:     #判斷是否要產生新球
                number_of_balls = random.randint(1+int(time/300),5+int(time/300))
                ball.creatballs(number_of_balls)      #產生新球
                wait=0
                a=0
            
            for i in range(ball.number):
                if ball.vorh_ball[i] == 0 or ball.vorh_ball[i] == 1:                
                    if ball.bax[i] > rightbound or ball.bay[i] > lowbound:
                        temp+=1
                if ball.vorh_ball[i] == 2 or ball.vorh_ball[i] == 3:
                    if ball.bax[i] < leftbound or ball.bay[i] < upbound:
                        temp+=1
            overmove_ball1 = temp
            if overmove_ball2 == ball2.number and ball2start == 1:
                number_of_balls2 = random.randint(1+int(time/300), 5+int(time/300))
                ball2.creatballs(number_of_balls2)
                wait2=0
            for i in range(ball2.number):
                if ball2.vorh_ball[i] == 0 or ball2.vorh_ball[i] ==1:              
                    if ball2.bax[i] > rightbound or ball2.bay[i] > lowbound:
                        tempball2+=1
                if ball2.vorh_ball[i] == 2 or ball2.vorh_ball[i] ==3:               
                    if ball2.bax[i] < leftbound or ball2.bay[i] < upbound:
                        tempball2+=1
            overmove_ball2 = tempball2
        elif traptype==1:
            # generate light            
            if overmove_light==light.number:
                number_of_light=random.randint(1+int(time/300),5+int(time/300))
                light.createlights(number_of_light)
                wait=0
                
            
            for i in range(light.number):
                if lit==5:
                    templ+=1
            overmove_light = templ
            
                
        screen.fill(BLACK)
        if traptype==0:
            if wait==3:
                for i in range(ball.number):
                    if ball.vorh_ball[i] == 0 or ball.vorh_ball[i] == 1:
                        if ball.bax[i]<=rightbound and ball.bay[i]<=lowbound:
                            if ball.vorh_ball[i] == 0 :
                                pygame.draw.circle(screen,BLUE,[ball.bax[i]+ball.vb[i],ball.bay[i]],radius_rock,0)
                                ball.bax[i]+=ball.vb[i] 
                            if ball.vorh_ball[i] == 1 :
                                pygame.draw.circle(screen,BLUE,[ball.bax[i],ball.bay[i]+ball.vb[i]],radius_rock,0)
                                ball.bay[i]+=ball.vb[i]
                    if ball.vorh_ball[i] == 2 or ball.vorh_ball[i] == 3:
                        if ball.bax[i]>=leftbound and ball.bay[i]>=upbound:
                            if ball.vorh_ball[i] == 2 :
                                pygame.draw.circle(screen,BLUE,[ball.bax[i]-ball.vb[i],ball.bay[i]],radius_rock,0)
                                ball.bax[i]-=ball.vb[i] 
                            if ball.vorh_ball[i] == 3:
                                pygame.draw.circle(screen,BLUE,[ball.bax[i],ball.bay[i]-ball.vb[i]],radius_rock,0)
                                ball.bay[i]-=ball.vb[i]
            
                for i in range(ball.number):
                    if ballcol(px,py,ball.bax[i],ball.bay[i],radius,radius_rock):
                        done=True
                
                ball2start = 1
            if wait2 >= 3:
                for i in range(ball2.number):
                    if ball2.vorh_ball[i] == 0 or ball2.vorh_ball[i] ==1: 
                        if ball2.bax[i]<=rightbound and ball2.bay[i]<=lowbound:
                            if ball2.vorh_ball[i] == 0 :
                                pygame.draw.circle(screen,BLUE,[ball2.bax[i]+ball2.vb[i],ball2.bay[i]],radius_rock,0)
                                ball2.bax[i]+=ball2.vb[i] 
                            if ball2.vorh_ball[i] == 1 :
                                pygame.draw.circle(screen,BLUE,[ball2.bax[i],ball2.bay[i]+ball2.vb[i]],radius_rock,0)
                                ball2.bay[i]+=ball2.vb[i]
                    if ball2.vorh_ball[i] == 2 or ball2.vorh_ball[i] ==3:
                        if ball2.bax[i]>=leftbound and ball2.bay[i]>=upbound:
                            if ball2.vorh_ball[i] == 2 :
                                pygame.draw.circle(screen,BLUE,[ball2.bax[i]-ball2.vb[i],ball2.bay[i]],radius_rock,0)
                                ball2.bax[i]-=ball2.vb[i] 
                            if ball2.vorh_ball[i] == 3:
                                pygame.draw.circle(screen,BLUE,[ball2.bax[i],ball2.bay[i]-ball2.vb[i]],radius_rock,0)
                                ball2.bay[i]-=ball2.vb[i]
                for i in range(ball2.number):
                    if ballcol(px,py,ball2.bax[i],ball2.bay[i],radius,radius_rock):
                        done=True
        if traptype==1:
            if wait == 3:
                for i in range(light.number):
                    if light.vorh_light[i]==0:
                        pygame.draw.line(screen,YELLOW,[leftbound,light.liy[i]],[rightbound,light.liy[i]],18+lit)
                    if light.vorh_light[i]==1:
                        pygame.draw.line(screen,YELLOW,[light.lix[i],upbound],[light.lix[i],lowbound],18+lit)
                for i in range(light.number):
                    if lightcol(px,py,light.lix[i],light.liy[i]):
                        done=True
        if time%30==0 and lit<5:
            lit+=1
        elif lit==5:
            lit=1
        if time%30==0 and wait<3:
            wait+=1
        if time%30==0 and wait2<10:
            wait2+=1
        # collition dectect-------------------------------------------------
        
        pos=pygame.mouse.get_pos()
        x=pos[0]
        y=pos[1]
        if px-radius<=leftbound:
            px=leftbound+radius
        if px+radius>=rightbound:
            px=rightbound-radius
        if py-radius<=upbound:
            py=upbound+radius
        if py+radius>=lowbound:
            py=lowbound-radius
        pygame.draw.circle(screen,WHITE,[px,py],radius,0)
        if change==1:        
            px+=dx
            py+=dy
        if change==-1:
            px=x
            py=y
        lines=[[leftbound,upbound],[leftbound,lowbound],[rightbound,lowbound],[rightbound,upbound]]
        #title=font1.render('Game starting~',True,WHITE)
        if show==-1:
            position=font1.render('position x:'+str(px)+'position y:'+str(py),True,WHITE)
            screen.blit(position,[0,0])
            waittext=font1.render('wait:'+str(wait),True,WHITE)
            screen.blit(waittext,[450,0])
        
        if traptype==0:
            if not wait==3:
                for i in range(ball.number):
                    if ball.vorh_ball[i]==0:
                        warning=font1.render('Warn',True,RED)
                        screen.blit(warning,[ball.warnx[i]-60,ball.warny[i]-10])
                    if ball.vorh_ball[i]==1:
                        warning=font1.render('Warn',True,RED)
                        screen.blit(warning,[ball.warnx[i]-25,ball.warny[i]-30])
                    if ball.vorh_ball[i]==2:
                        warning=font1.render('Warn',True,RED)
                        screen.blit(warning,[ball.warnx[i]+40,ball.warny[i]-10])
                    if ball.vorh_ball[i]==3:
                        warning=font1.render('Warn',True,RED)
                        screen.blit(warning,[ball.warnx[i]-25,ball.warny[i]+30])
            if not wait2>=3:
                for i in range(ball2.number):
                    if ball2.vorh_ball[i]==0:
                        warning=font1.render('Warn',True,RED)
                        screen.blit(warning,[ball2.warnx[i]-60,ball2.warny[i]-10])
                    if ball2.vorh_ball[i]==1:
                        warning=font1.render('Warn',True,RED)
                        screen.blit(warning,[ball2.warnx[i]-25,ball2.warny[i]-30])
                    if ball2.vorh_ball[i]==2:
                        warning=font1.render('Warn',True,RED)
                        screen.blit(warning,[ball2.warnx[i]+40,ball2.warny[i]-10])
                    if ball2.vorh_ball[i]==3:
                        warning=font1.render('Warn',True,RED)
                        screen.blit(warning,[ball2.warnx[i]-25,ball2.warny[i]+30])
                    
        if traptype==1:
            if not wait==3:    
                for i in range(light.number):
                    if light.vorh_light[i]==0:
                        warningl=font1.render('Warn',True,YELLOW)
                        screen.blit(warningl,[light.warnx[i]-50,light.warny[i]-10])
                    if light.vorh_light[i]==1:
                        warningl1=font1.render('Warn',True,YELLOW)
                        screen.blit(warningl1,[light.warnx[i]-25,light.warny[i]-10])
            
                
        pygame.draw.circle(screen,RED,[x,y],5,0)
        pygame.draw.lines(screen,WHITE,True,lines,5)
        
        #screen.blit(title,[600,200])
        if time/60 <60:
            s=int(time/60*100)
        else:
            s=int((time/60-60)*200+6000)
        
        time+=1
        timing=font1.render('Time:'+str(int(time/60)),True,WHITE)
        scoring=font1.render('Score:'+str(s),True,WHITE)
        screen.blit(timing,[350,0])
        screen.blit(scoring,[450,0])
        clock=pygame.time.Clock()
        pygame.display.flip()
        clock.tick(60)
    return s

#rank_score -------------------------------------------
def rank_score(s):    

    file=open("rank.txt","r")

    x1,x2,x3,x4,x5,x6='a','a','a','a','a','a'
    
    x1=file.readline()
    x2=file.readline()
    x3=file.readline()
    x4=file.readline()
    x5=file.readline()
    x6=file.readline()

    x1=int(x1)
    x2=int(x2)
    x3=int(x3)
    x4=int(x4)
    x5=int(x5)

    score=[x1,x2,x3,x4,x5,x6]
    temp=[x1,x2,x3,x4,x5,x6]

    file.close()    

#rank --------------------------------------------------

    score[5]=s
    temp[5]=s
    for i in range(6):
        for j in range(6-i):
            if i+j+1<6:
                if score[i+j+1]>score[i]:
                    score[i]=score[i+j+1]
                    score[i+j+1]=temp[i]
                    
    file1=open("rank.txt","w")    

    x1=str(score[0])
    x2=str(score[1])
    x3=str(score[2])
    x4=str(score[3])
    x5=str(score[4])




    file1.write(x1+'\n')
    file1.write(x2+'\n')
    file1.write(x3+'\n')
    file1.write(x4+'\n')
    file1.write(x5+'\n')

 
    
    file1.close()

# score -------------------------------------------------
def score():
    done=False
    font1=pygame.font.SysFont('Calibri',25,True,False)
    pygame.mouse.set_visible(False)
    file=open("rank.txt","r")
    
    x1=str(int(file.readline()))
    x2=str(int(file.readline()))
    x3=str(int(file.readline()))
    x4=str(int(file.readline()))
    x5=str(int(file.readline()))
    file.close()
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:            
                done=True
            if event.type == pygame.KEYDOWN:
                print('user pressed a button')
            if event.type == pygame.KEYUP:
                print('user release a button')
            if event.type == pygame.MOUSEBUTTONDOWN:
                print('user pressed mouse button')
                done=True
            if event.type == pygame.MOUSEBUTTONUP:
                print('user release a mouse button') 
        screen.fill(RED)
        pos=pygame.mouse.get_pos()
        x=pos[0]
        y=pos[1]
        title=font1.render('Score:',True,WHITE)
        sco1=font1.render(x1,True,WHITE)
        sco2=font1.render(x2,True,WHITE)
        sco3=font1.render(x3,True,WHITE)
        sco4=font1.render(x4,True,WHITE)
        sco5=font1.render(x5,True,WHITE)
    
        pygame.draw.circle(screen,BLACK,[x,y],5,0)
        screen.blit(title,[600,200])
        screen.blit(sco1,[600,230])
        screen.blit(sco2,[600,260])
        screen.blit(sco3,[600,290])
        screen.blit(sco4,[600,320])
        screen.blit(sco5,[600,350])
        clock=pygame.time.Clock()
        pygame.display.flip()
        clock.tick(60)
    return

# rule ------------------------------------------------
def rule():
    done=False
    font1=pygame.font.SysFont('Calibri',25,True,False)
    pygame.mouse.set_visible(False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:            
                done=True
            if event.type == pygame.KEYDOWN:
                print('user pressed a button')
            if event.type == pygame.KEYUP:
                print('user release a button')
            if event.type == pygame.MOUSEBUTTONDOWN:
                print('user pressed mouse button')
                done=True
            if event.type == pygame.MOUSEBUTTONUP:
                print('user release a mouse button') 
        screen.fill(RED)
        pos=pygame.mouse.get_pos()
        x=pos[0]
        y=pos[1]
        title=font1.render('Rule',True,WHITE)
        pygame.draw.circle(screen,BLACK,[x,y],5,0)
        screen.blit(title,[600,200])
        clock=pygame.time.Clock()
        pygame.display.flip()
        clock.tick(60)
    return
    
# set -------------------------------------------------
def setting(dex):
    
    dex_in_setting=dex
    done=False
    font1=pygame.font.SysFont('Calibri',25,True,False)
    pygame.mouse.set_visible(False)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:            
                done=True
            if event.type == pygame.KEYDOWN:
                print('user pressed a button')
            if event.type == pygame.KEYUP:
                print('user release a button')
            if event.type == pygame.MOUSEBUTTONDOWN:
                print('user pressed mouse button')
                done=True
            if event.type == pygame.MOUSEBUTTONUP:
                print('user release a mouse button')
        screen.fill(BLACK)
        pos=pygame.mouse.get_pos()
        x=pos[0]
        y=pos[1]
        title=font1.render('setting',True,WHITE)
        print('1 ok')
        pygame.draw.line(screen,WHITE,(200,200),(600,200),10)
        if x>600:
            x=600   
        if x<200:
            x=200
        pygame.draw.rect(screen,RED,(200,200,x-200,5),0)
        print('2 ok')
        dex_in_setting = x
        dex_in_setting = dex_in_setting / 100
        screen.blit(title,[600,200])
        clock=pygame.time.Clock()
        pygame.display.flip()
        print('3 ok')
        clock.tick(2)
        print(done ,'1')
        if done ==True:
            done=True
        print(done ,'2')
    return dex_in_setting
    
# set size of the screen ----------------------------------
screen= pygame.display.set_mode((1280,720),0,32)
pygame.display.set_caption('Hello World')

# text setting --------------------------------------------
font1=pygame.font.SysFont('Calibri',25,True,False)
font2=pygame.font.SysFont('Calibri',40,True,False)

# color define --------------------------------------------
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)

# drawing varible -----------------------------------------
x_offset=0
y_offset=0
i=0
c1=100
c2=100
time=0
show=1
# time define ---------------------------------------------
clock=pygame.time.Clock()

# menu ----------------------------------------------------
done=False

while not done:
    pygame.mouse.set_visible(True)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
        if event.type == pygame.KEYDOWN:
            if event.key == K_s:
                show=show*(-1)
            print('user pressed a button')
        if event.type == pygame.KEYUP:
            print('user release a button')
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('user pressed mouse button')
            if mouseclick(x,y,600,300,120,20):
                point=gamestart(dex)
                rank_score(point)
            if mouseclick(x,y,600,330,60,20):
                score()
            #if mouseclick(x,y,600,360,120,20):
                #rule()
            #if mouseclick(x,y,600,390,120,20):
                #setting(dex)
                #dex=setting(dex)
            if mouseclick(x,y,600,420,40,20):
                done=True
        if event.type == pygame.MOUSEBUTTONUP:
            print('user release a mouse button')
    



# clean the screen ----------------------------------------
    screen.fill(BLACK)
    
# drawing screen ------------------------------------------
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
    title=font2.render('Mr.Gin Ron Chen',True,RED)
    if show==-1:
        pixel=font1.render('x:'+str(int(x))+'y:'+str(int(y)),True,RED)
        screen.blit(pixel,[0,0])    
    choose1=font1.render('Game Start',True,WHITE)
    choose2=font1.render('Score',True,WHITE)
    #choose3=font1.render('Game Rule',True,WHITE)
    #choose4=font1.render('Setting',True,WHITE)
    choose5=font1.render('Exit',True,WHITE)
    screen.blit(title,[512,205])
    screen.blit(choose1,[600,300])
    screen.blit(choose2,[600,330])
    #screen.blit(choose3,[600,360])
    #screen.blit(choose4,[600,390])
    screen.blit(choose5,[600,420])
    time+=1

# flip the screen -----------------------------------------
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()
