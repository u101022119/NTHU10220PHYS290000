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
        screen.blit(wdData[this.word],coord)
        
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
#==============================================================================
noBrick=Brick(-1,-1,-1)

maxX=8
maxY=16
bricks=[[noBrick]]
for x in range(maxX):
    if x>=1:
        bricks.append([noBrick])
    for y in range(maxY)[1:]:
        bricks[x].append(noBrick)

bricks[0][0]=Brick(0,0,0)
bricks[7][15]=Brick(0,0,0)

controlBricks=[[noBrick]]
for x in range(5):
    if x>=1:
        controlBricks.append([noBrick])
    for y in range(5)[1:]:
        controlBricks[x].append(noBrick)

controlBricks[0][2]=Brick(0,0,0)
controlBricks[1][2]=Brick(0,0,0)
controlBricks[2][2]=Brick(0,0,0)
controlBricks[2][3]=Brick(0,0,0)

control=(maxX/2,maxY-2);

import pygame
pygame.init()

bgData=[pygame.image.load("bg.bmp")]
wdData=[pygame.image.load("wd.bmp")]

size = (288, 544)
screen = pygame.display.set_mode(size)

done=False
ftime=0
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
                pass
        #if event.type == pygame.KEY_PRESS:
            #if event.key == pygame.K_DOWN:
    if(ftime % 30 == 0):
        if not conflict((control[0],control[1]-1)):
            control=(control[0],control[1]-1)
                
    
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
