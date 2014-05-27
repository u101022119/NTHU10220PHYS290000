# -*- coding: utf-8 -*-
"""
Created on Tue May 20 16:22:40 2014

@author: user
"""

class Brick(object):
    """
    ...
    enum bgcolor,wdcolor,word
    """
    def __init__(this,bgc,wdc,wd):
        this.bgcolor=bgc
        this.wdcolor=wdc
        this.word=wd
    def show(this,x,y):
        if this.bgcolor==-1:
            return
        coord=(16+x*32,544-48-y*32)
        screen.blit(bgData[this.bgcolor],coord)
        screen.blit(wdData[this.word][this.wdcolor],coord)
        
def conflict(coord):
    x=coord[0]
    y=coord[1]
    xa=0
    while controlBricks[2-xa][2]!=noBrick:
        xa+=1
        if(xa==3):break
    xb=0
    while controlBricks[2+xb][2]!=noBrick:
        xb+=1
        if(xb==3):break
    ya=0
    while controlBricks[2][2-ya]!=noBrick:
        ya+=1
        if(ya==3):break
    yb=0
    while controlBricks[2][2+yb]!=noBrick:
        yb+=1
        if(yb==3):break
    if x-xa<-1 or x+xb>=maxX+1:
        return True
    if y-ya<-1 or y+yb>=maxY+1:
        return True
    
    for cx in range(5):
        for cy in range(5):
            if controlBricks[cx][cy]!=noBrick:
                if bricks[x-2+cx][y-2+cy]!=noBrick:
                    return True
    return False

def check():
    rec=False
    for y in range(maxY):
        bgc=1
        wdc=1
        wcc=1
        for x in range(maxX)[:-1]:
            if bricks[x][y].bgcolor==bricks[x+1][y].bgcolor:
                bgc+=1
            else:
                if bgc>=3 and bricks[x][y]!=noBrick:
                    for bx in range(bgc):
                        for fy in range(maxY)[y:-1]:
                            bricks[x-bx][fy]=bricks[x-bx][fy+1]
                        bricks[x-bx][maxY-1]=noBrick
                    rec=True
                bgc=1
    for x in range(maxX):
        bgc=1
        wdc=1
        wcc=1
        for y in range(maxY)[:-1]:
            if bricks[x][y].bgcolor==bricks[x][y+1].bgcolor:
                bgc+=1
            else:
                if bgc>=3 and bricks[x][y]!=noBrick:
                    for fy in range(maxY)[y-bgc+1:-bgc]:                    
                        bricks[x][fy]=bricks[x][fy+bgc]
                    for ly in range(maxY)[-bgc:]:
                        bricks[x][ly]=noBrick
                    rec=True
                bgc=1
    if rec:
        check()

def rotate():
    global control
    global controlBricks
    x=control[0]
    y=control[1]
    
    xa=0
    while controlBricks[2-xa][2]!=noBrick:
        xa+=1
        if(xa==3):break
    xb=0
    while controlBricks[2+xb][2]!=noBrick:
        xb+=1
        if(xb==3):break
    ya=0
    while controlBricks[2][2-ya]!=noBrick:
        ya+=1
        if(ya==3):break
    yb=0
    while controlBricks[2][2+yb]!=noBrick:
        yb+=1
        if(yb==3):break
    if x-ya<-1 or x+yb>=maxX+1:
        return True
    if y-xb<-1 or y+xa>=maxY+1:
        return True
        
    for cx in range(3):
        for cy in range(2):
            bx=4-cx
            by=4-cy
            temp=controlBricks[cx][cy]
            controlBricks[cx][cy]=controlBricks[by][cx]
            controlBricks[by][cx]=controlBricks[bx][by]
            controlBricks[bx][by]=controlBricks[cy][bx]
            controlBricks[cy][bx]=temp

def putBrick():
    global control
    x=control[0]
    y=control[1]
    for cx in range(5):
        for cy in range(5):
            if controlBricks[cx][cy]!=noBrick:
                bricks[x-2+cx][y-2+cy]=controlBricks[cx][cy]
                controlBricks[cx][cy]=noBrick

def newBrick():
    global control
    global controlBricks
    nbList=(
        (4,(0,2),(1,2),(2,2),(2,3)),
        (4,(4,2),(3,2),(2,2),(2,3)),
        (4,(3,3),(3,2),(2,2),(2,3)),       
        (4,(0,2),(1,2),(2,2),(3,2)),
        (4,(3,2),(1,2),(2,2),(2,3)),       
        (3,(1,2),(2,2),(3,2)),
        (3,(1,2),(2,2),(2,3)),
        (2,(1,2),(2,2)),
        (1,(2,2))
        )
    i=int(random()*9)
    for j in range(nbList[i][0]):
        controlBricks[nbList[i][j+1][0]][nbList[i][j+1][1]]=Brick(int(random()*4),0,int(random()*4))
#    controlBricks[2][3]=Brick(0,0,0)
    control=(maxX/2,maxY-2)
    
    
#==============================================================================
noBrick=Brick(-1,-1,-1)

maxX=8
maxY=16
bricks=[]
for x in range(maxX):
    bricks.append([])
    for y in range(maxY):
        bricks[x].append(noBrick)

controlBricks=[[noBrick]]
for x in range(5):
    if x>=1:
        controlBricks.append([noBrick])
    for y in range(5)[1:]:
        controlBricks[x].append(noBrick)
        
control=(2,maxY-2)
newBrick()

import pygame
pygame.init()

bgData=[]
wdData=[]
for i in range(4):
    bgData.append(pygame.image.load("bg"+str(i)+".bmp"))
    wdData.append([])
    for j in range(4):
        wdData[i].append(pygame.image.load("wd"+str(i)+"-"+str(0)+".png"))

size = (288, 544)
screen = pygame.display.set_mode(size)

done=False
ftime=0
tpf=30
while not done:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done=True
            elif event.key == pygame.K_RIGHT:
                if not conflict((control[0]+1,control[1])):
                    control=(control[0]+1,control[1])
            elif event.key == pygame.K_LEFT:
                if not conflict((control[0]-1,control[1])):
                    control=(control[0]-1,control[1])
            elif event.key == pygame.K_UP:
                rotate()
            elif event.key == pygame.K_DOWN:
                tpf=5;
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                tpf=30
    
    if(ftime % tpf == 0):
        if not conflict((control[0],control[1]-1)):
            control=(control[0],control[1]-1)
        else:
            putBrick()
            check()
            newBrick()
            if conflict(control):
                break;
    
    screen.fill((14,35,147))
    
    for x in range(maxX):
        for y in range(maxY):
            bricks[x][y].show(x,y)
    for x in range(5):
        for y in range(5):
            controlBricks[x][y].show(control[0]+x-2,control[1]+y-2)
    
    pygame.display.flip();
    pygame.time.wait(15)
    ftime+=1
    #done=True

pygame.quit()
