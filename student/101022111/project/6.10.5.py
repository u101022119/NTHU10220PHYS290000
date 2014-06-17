# -*- coding: utf-8 -*-
"""
Created on Tue May 06 15:53:40 2014

@author: larry lu
"""

import random, pygame, sys
from pygame.locals import *

FPS = 15
Chessboardwidth = 480
Chessboardheight = 480
WINDOWWIDTH = 900
WINDOWHEIGHT = 540
CELLSIZE = 60
assert Chessboardwidth % CELLSIZE == 0, "Window width must be a multiple of cell size."
assert Chessboardheight % CELLSIZE == 0, "Window height must be a multiple of cell size."
CELLWIDTH = int(Chessboardwidth / CELLSIZE)
CELLHEIGHT = int(Chessboardheight / CELLSIZE)
#color
LIGHTGRAY    = ( 200, 200, 200)
DARKGRAY     = ( 40 , 40 , 40 )
WHITE        = ( 255, 255, 255)
BLACK        = ( 0  , 0  , 0  )
BLUE         = ( 0  , 243, 253)

    #  white
        
white_king = pygame.Rect(270, 30, 60, 60) 
white_kingimage = pygame.image.load('WKING.png')
       
white_queen = pygame.Rect(210, 30, 60, 60) 
white_queenimage = pygame.image.load('WQUEEN.png')
       
white_bishop1 = pygame.Rect(150, 30, 60, 60) 
white_bishop1image=pygame.image.load('WBISHOP.png')
   
white_bishop2 = pygame.Rect(330, 30, 60, 60) 
white_bishop2image=pygame.image.load('WBISHOP.png')
   
white_rock1 =pygame.Rect(30, 30, 60, 60)  
white_rock1image=pygame.image.load('WROCK.png')
    
white_rock2 =pygame.Rect(450, 30, 60, 60)  
white_rock2image=pygame.image.load('WROCK.png')

white_knight1 = pygame.Rect(90, 30, 60, 60) 
white_knight1image=pygame.image.load('WKNIGHT.png')
    
white_knight2 = pygame.Rect(390, 30, 60, 60) 
white_knight2image=pygame.image.load('WKNIGHT.png')
    
white_soldier1 =pygame.Rect(30, 90, 60, 60)  
white_soldier1image=pygame.image.load('WSOLDIER.png')
    
white_soldier2 =pygame.Rect(90, 90, 60, 60) 
white_soldier2image=pygame.image.load('WSOLDIER.png')
    
white_soldier3 =pygame.Rect(150, 90, 60, 60) 
white_soldier3image=pygame.image.load('WSOLDIER.png')
   
white_soldier4 =pygame.Rect(210, 90, 60, 60) 
white_soldier4image=pygame.image.load('WSOLDIER.png')
    
white_soldier5 =pygame.Rect(270, 90, 60, 60)  
white_soldier5image=pygame.image.load('WSOLDIER.png')
    
white_soldier6 =pygame.Rect(330, 90, 60, 60)  
white_soldier6image=pygame.image.load('WSOLDIER.png')
    
white_soldier7 =pygame.Rect(390, 90, 60, 60)  
white_soldier7image=pygame.image.load('WSOLDIER.png')
    
white_soldier8 =pygame.Rect(450, 90, 60, 60)  
white_soldier8image=pygame.image.load('WSOLDIER.png')
    # black
      
black_king = pygame.Rect(270, 450, 60, 60)
black_kingimage=pygame.image.load('BKING.png')
    
black_queen = pygame.Rect(210, 450, 60, 60)
black_queenimage=pygame.image.load('BQUEEN.png')
       
black_bishop1 =pygame.Rect(150, 450, 60, 60) 
black_bishop1image=pygame.image.load('BBISHOP.png')

black_bishop2 =pygame.Rect(330, 450, 60, 60) 
black_bishop2image=pygame.image.load('BBISHOP.png')
    
black_rock1 =pygame.Rect(30, 450, 60, 60) 
black_rock1image=pygame.image.load('BROCK.png')
    
black_rock2 =pygame.Rect(450, 450, 60, 60)
black_rock2image=pygame.image.load('BROCK.png')
   
black_knight1 = pygame.Rect(90, 450, 60, 60)
black_knight1image=pygame.image.load('BKNIGHT.png')
    
black_knight2 = pygame.Rect(390, 450, 60, 60)
black_knight2image=pygame.image.load('BKNIGHT.png')

black_soldier1 =pygame.Rect(30, 390, 60, 60)
black_soldier1image=pygame.image.load('BSOLDIER.png')
   
black_soldier2 =pygame.Rect(90, 390, 60, 60)  
black_soldier2image=pygame.image.load('BSOLDIER.png')
    
black_soldier3 =pygame.Rect(150, 390, 60, 60) 
black_soldier3image=pygame.image.load('BSOLDIER.png')

black_soldier4 =pygame.Rect(210, 390, 60, 60)  
black_soldier4image=pygame.image.load('BSOLDIER.png')
    
black_soldier5 =pygame.Rect(270, 390, 60, 60) 
black_soldier5image=pygame.image.load('BSOLDIER.png')
   
black_soldier6 =pygame.Rect(330, 390, 60, 60) 
black_soldier6image=pygame.image.load('BSOLDIER.png')
    
black_soldier7 =pygame.Rect(390, 390, 60, 60) 
black_soldier7image=pygame.image.load('BSOLDIER.png')
    
black_soldier8 =pygame.Rect(450, 390, 60, 60) 
black_soldier8image=pygame.image.load('BSOLDIER.png')

def main():
    global DISPLAYSURF, BASICFONT

    pygame.init()    
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Chess')
    drawGrid()
    runGame()
    showGameOverScreen(runGame)
# start part
def drawPressKeyMsg():
    pressKeySurf = BASICFONT.render('Press a key to play.', True, WHITE)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 30)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)
def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key

def terminate():
    pygame.quit()
    sys.exit()


# Game's main point    
def runGame():
    while True:
        pygame.display.flip()
        DISPLAYSURF.blit(white_kingimage, white_king)
        DISPLAYSURF.blit(white_queenimage, white_queen)
        DISPLAYSURF.blit(white_knight1image, white_knight1)
        DISPLAYSURF.blit(white_knight2image, white_knight2)
        DISPLAYSURF.blit(white_rock1image, white_rock1)
        DISPLAYSURF.blit(white_rock2image, white_rock2)
        DISPLAYSURF.blit(white_bishop1image, white_bishop1)
        DISPLAYSURF.blit(white_bishop2image, white_bishop2)
        DISPLAYSURF.blit(white_soldier1image, white_soldier1)
        DISPLAYSURF.blit(white_soldier2image, white_soldier2)
        DISPLAYSURF.blit(white_soldier3image, white_soldier3)
        DISPLAYSURF.blit(white_soldier4image, white_soldier4)
        DISPLAYSURF.blit(white_soldier5image, white_soldier5)
        DISPLAYSURF.blit(white_soldier6image, white_soldier6)
        DISPLAYSURF.blit(white_soldier7image, white_soldier7)
        DISPLAYSURF.blit(white_soldier8image, white_soldier8)
        
        DISPLAYSURF.blit(black_kingimage, black_king)
        DISPLAYSURF.blit(black_queenimage, black_queen)
        DISPLAYSURF.blit(black_knight1image, black_knight1)
        DISPLAYSURF.blit(black_knight2image, black_knight2)
        DISPLAYSURF.blit(black_rock1image, black_rock1)
        DISPLAYSURF.blit(black_rock2image, black_rock2)
        DISPLAYSURF.blit(black_bishop1image, black_bishop1)
        DISPLAYSURF.blit(black_bishop2image, black_bishop2)
        DISPLAYSURF.blit(black_soldier1image, black_soldier1)
        DISPLAYSURF.blit(black_soldier2image, black_soldier2)
        DISPLAYSURF.blit(black_soldier3image, black_soldier3)
        DISPLAYSURF.blit(black_soldier4image, black_soldier4)
        DISPLAYSURF.blit(black_soldier5image, black_soldier5)
        DISPLAYSURF.blit(black_soldier6image, black_soldier6)
        DISPLAYSURF.blit(black_soldier7image, black_soldier7)
        DISPLAYSURF.blit(black_soldier8image, black_soldier8) 
        choosen=0
        for event in pygame.event.get():
            
            
                if event.type == MOUSEBUTTONDOWN:
                    choosenchess(event.pos[0],event.pos[1],choosen)
                    walk(event.pos[0],event.pos[1],choosen)
                                                    
                if  white_king.left==0 and white_king.top ==0:
                    return 'BLACK Win'
                if  black_king.left==0 and black_king.top ==0:
                    return 'WHITE Win'
                    
                    
def choosenchess(point1,point2,choosen):       
    for a in range(9):
        for b in range(9):
            if point1>(60*a-30) and point2>(60*b+30) and point1<(60*a+30) and point2<(60*b+90):
                if (black_king.left+30)>(60*a-30) and (black_king.top-30)>(60*b-30) and (black_king.left+30)<(60*a+30) and (black_king.top-30)<(60*b+30):
                    choosen=black_king
                    
                elif (black_queen.left+30)>(60*a-30) and (black_queen.top-30)>(60*b-30) and (black_queen.left+30)<(60*a+30) and (black_queen.top-30)<(60*b+30):
                    choosen=black_queen
            
                elif (black_knight1.left+30)>(60*a-30) and (black_knight1.top-30)>(60*b-30) and (black_knight1.left+30)<(60*a+30) and (black_knight1.top-30)<(60*b+30):
                    choosen=black_knight1
            
                elif (black_knight2.left+30)>(60*a-30) and (black_knight2.top-30)>(60*b-30) and (black_knight2.left+30)<(60*a+30) and (black_knight2.top-30)<(60*b+30):
                    choosen=black_knight2
            
                elif (black_rock1.left+30)>(60*a-30) and (black_rock1.top-30)>(60*b-30) and (black_rock1.left+30)<(60*a+30) and (black_rock1.top-30)<(60*b+30):
                    choosen=black_rock1
            
                elif (black_rock2.left+30)>(60*a-30) and (black_rock2.top-30)>(60*b-30) and (black_rock2.left+30)<(60*a+30) and (black_rock2.top-30)<(60*b+30):
                    choosen=black_rock2
            
                elif (black_bishop1.left+30)>(60*a-30) and (black_bishop1.top-30)>(60*b-30) and (black_bishop1.left+30)<(60*a+30) and (black_bishop1.top-30)<(60*b+30):
                    choosen=black_bishop1
            
                elif (black_bishop2.left+30)>(60*a-30) and (black_bishop2.top-30)>(60*b-30) and (black_bishop2.left+30)<(60*a+30) and (black_bishop2.top-30)<(60*b+30):
                    choosen=black_bishop2
            
                elif (black_soldier1.left+30)>(60*a-30) and (black_soldier1.top-30)>(60*b-30) and (black_soldier1.left+30)<(60*a+30) and (black_soldier1.top-30)<(60*b+30):
                    choosen=black_soldier1
                    
                elif (black_soldier2.left+30)>(60*a-30) and (black_soldier2.top-30)>(60*b-30) and (black_soldier2.left+30)<(60*a+30) and (black_soldier2.top-30)<(60*b+30):
                    choosen=black_soldier2
                        
                elif (black_soldier3.left+30)>(60*a-30) and (black_soldier3.top-30)>(60*b-30) and (black_soldier3.left+30)<(60*a+30) and (black_soldier3.top-30)<(60*b+30):
                    choosen=black_soldier3
            
                elif (black_soldier4.left+30)>(60*a-30) and (black_soldier4.top-30)>(60*b-30) and (black_soldier4.left+30)<(60*a+30) and (black_soldier4.top-30)<(60*b+30):
                    choosen=black_soldier4
                    
                elif (black_soldier5.left+30)>(60*a-30) and (black_soldier5.top-30)>(60*b-30) and (black_soldier5.left+30)<(60*a+30) and (black_soldier5.top-30)<(60*b+30):
                    choosen=black_soldier5
            
                elif (black_soldier6.left+30)>(60*a-30) and (black_soldier6.top-30)>(60*b-30) and (black_soldier6.left+30)<(60*a+30) and (black_soldier6.top-30)<(60*b+30):
                    choosen=black_soldier6
            
                elif (black_soldier7.left+30)>(60*a-30) and (black_soldier7.top-30)>(60*b-30) and (black_soldier7.left+30)<(60*a+30) and (black_soldier7.top-30)<(60*b+30):
                    choosen=black_soldier7
            
                elif (black_soldier8.left+30)>(60*a-30) and (black_soldier8.top-30)>(60*b-30) and (black_soldier8.left+30)<(60*a+30) and (black_soldier8.top-30)<(60*b+30):
                    choosen=black_soldier8
            
                elif (white_king.left+30)>(60*a-30) and (white_king.top-30)>(60*b-30) and (white_king.left+30)<(60*a+30) and (white_king.top-30)<(60*b+30):
                    choosen=white_king
            
                elif (white_queen.left+30)>(60*a-30) and (white_queen.top-30)>(60*b-30) and (white_queen.left+30)<(60*a+30) and (white_queen.top-30)<(60*b+30):
                    choosen=white_queen
            
                elif (white_knight1.left+30)>(60*a-30) and (white_knight1.top-30)>(60*b-30) and (white_knight1.left+30)<(60*a+30) and (white_knight1.top-30)<(60*b+30):
                    choosen=white_knight1
            
                elif (white_knight2.left+30)>(60*a-30) and (white_knight2.top-30)>(60*b-30) and (white_knight2.left+30)<(60*a+30) and (white_knight2.top-30)<(60*b+30):
                    choosen=white_knight2
            
                elif (white_rock1.left+30)>(60*a-30) and (white_rock1.top-30)>(60*b-30) and (white_rock1.left+30)<(60*a+30) and (white_rock1.top-30)<(60*b+30):
                    choosen=white_rock1
            
                elif (white_rock2.left+30)>(60*a-30) and (white_rock2.top-30)>(60*b-30) and (white_rock2.left+30)<(60*a+30) and (white_rock2.top-30)<(60*b+30):
                    choosen=white_rock2
        
                elif (white_bishop1.left+30)>(60*a-30) and (white_bishop1.top-30)>(60*b-30) and (white_bishop1.left+30)<(60*a+30) and (white_bishop1.top-30)<(60*b+30):
                    choosen=white_bishop1
            
                elif (white_bishop2.left+30)>(60*a-30) and (white_bishop2.top-30)>(60*b-30) and (white_bishop2.left+30)<(60*a+30) and (white_bishop2.top-30)<(60*b+30):
                    choosen=white_bishop2
            
                elif (white_soldier1.left+30)>(60*a-30) and (white_soldier1.top-30)>(60*b-30) and (white_soldier1.left+30)<(60*a+30) and (white_soldier1.top-30)<(60*b+30):
                    choosen=white_soldier1
            
                elif (white_soldier2.left+30)>(60*a-30) and (white_soldier2.top-30)>(60*b-30) and (white_soldier2.left+30)<(60*a+30) and (white_soldier2.top-30)<(60*b+30):
                    choosen=white_soldier2
            
                elif (white_soldier3.left+30)>(60*a-30) and (white_soldier3.top-30)>(60*b-30) and (white_soldier3.left+30)<(60*a+30) and (white_soldier3.top-30)<(60*b+30):
                    choosen=white_soldier3
            
                elif (white_soldier4.left+30)>(60*a-30) and (white_soldier4.top-30)>(60*b-30) and (white_soldier4.left+30)<(60*a+30) and (white_soldier4.top-30)<(60*b+30):
                    choosen=white_soldier4
            
                elif (white_soldier5.left+30)>(60*a-30) and (white_soldier5.top-30)>(60*b-30) and (white_soldier5.left+30)<(60*a+30) and (white_soldier5.top-30)<(60*b+30):
                    choosen=white_soldier5
            
                elif (white_soldier6.left+30)>(60*a-30) and (white_soldier6.top-30)>(60*b-30) and (white_soldier6.left+30)<(60*a+30) and (white_soldier6.top-30)<(60*b+30):
                    choosen=white_soldier6
            
                elif (white_soldier7.left+30)>(60*a-30) and (white_soldier7.top-30)>(60*b-30) and (white_soldier7.left+30)<(60*a+30) and (white_soldier7.top-30)<(60*b+30):
                    choosen=white_soldier7
            
                elif (white_soldier8.left+30)>(60*a-30) and (white_soldier8.top-30)>(60*b-30) and (white_soldier8.left+30)<(60*a+30) and (white_soldier8.top-30)<(60*b+30):
                    choosen=white_soldier8
                elif():
                    choosen=0
                print choosen
                                
                        
def walk(point1,point2,choosen):
                                   
    if event.type == MOUSEBUTTONUP:
        print 1
        for a in range(9):
            for b in range(9):
                if point1>(60*a-30) and point2>(60*b+30) and point1<(60*a+30) and point2<(60*b+90):
                    print 3
                    print choosen
                    if choosen==black_king:
                        if 60*a>black_king.left-60 and 60*b>black_king.top-120 and 60*a<black_king.left+120 and 60*b<black_king.top+60:
                            black_king.left=60*a-30
                            black_king.top =60*b+90
                            blackeatwhite(black_king)
                            
                            choosen=0
                        elif():
                            choosen=0
                    elif choosen==white_king:
                        if 60*a>white_king.left-60 and 60*b>white_king.top-120 and 60*a<white_king.left+120 and 60*b<white_king.top+60:
                            white_king.left=60*a-30
                            white_king.top =60*b+90
                            choosen=0
                            whiteeatblack(white_king)
                        elif():
                            choosen=0
                    elif choosen==black_knight1:
                        if 60*a>black_knight1.left-60 and 60*b>black_knight1.top+60 and 60*a<black_knight1.left and 60*b<black_knight1.top+120:
                            black_knight1.left=60*a-30
                            black_knight1.top =60*b+90
                            blackeatwhite(black_knight1)
                            choosen=0
                        if 60*a>black_knight1.left-120 and 60*b>black_knight1.top and 60*a<black_knight1.left-60 and 60*b<black_knight1.top+60:
                            black_knight1.left=60*a-30
                            black_knight1.top =60*b+90
                            blackeatwhite(black_knight1)
                            choosen=0
                        if 60*a>black_knight1.left+60 and 60*b>black_knight1.top+60 and 60*a<black_knight1.left+120 and 60*b<black_knight1.top+120:
                            black_knight1.left=60*a-30
                            black_knight1.top =60*b+90
                            blackeatwhite(black_knight1)
                            choosen=0
                        if 60*a>black_knight1.left+120 and 60*b>black_knight1.top and 60*a<black_knight1.left+180 and 60*b<black_knight1.top+60:
                            black_knight1.left=60*a-30
                            black_knight1.top =60*b+90
                            blackeatwhite(black_knight1)
                            choosen=0
                        if 60*a>black_knight1.left+120 and 60*b>black_knight1.top-120 and 60*a<black_knight1.left+180 and 60*b<black_knight1.top-60:
                            black_knight1.left=60*a-30
                            black_knight1.top =60*b+90
                            blackeatwhite(black_knight1)
                            choosen=0
                        if 60*a>black_knight1.left+60 and 60*b>black_knight1.top-180 and 60*a<black_knight1.left+120 and 60*b<black_knight1.top-120:
                            black_knight1.left=60*a-30
                            black_knight1.top =60*b+90
                            blackeatwhite(black_knight1)
                            choosen=0
                        if 60*a>black_knight1.left-60 and 60*b>black_knight1.top-180 and 60*a<black_knight1.left and 60*b<black_knight1.top-120:
                            black_knight1.left=60*a-30
                            black_knight1.top =60*b+90
                            blackeatwhite(black_knight1)
                            choosen=0
                        if 60*a>black_knight1.left-120 and 60*b>black_knight1.top-120 and 60*a<black_knight1.left-60 and 60*b<black_knight1.top-60:
                            black_knight1.left=60*a-30
                            black_knight1.top =60*b+90
                            blackeatwhite(black_knight1)
                            choosen=0
                        elif():
                            choosen=0
                    elif choosen==black_knight2:
                        if 60*a>black_knight2.left-60 and 60*b>black_knight2.top+60 and 60*a<black_knight2.left and 60*b<black_knight2.top+120:
                            black_knight2.left=60*a-30
                            black_knight2.top =60*b+90
                            blackeatwhite(black_knight2)
                            choosen=0
                        if 60*a>black_knight2.left-120 and 60*b>black_knight2.top and 60*a<black_knight2.left-60 and 60*b<black_knight2.top+60:
                            black_knight2.left=60*a-30
                            black_knight2.top =60*b+90
                            blackeatwhite(black_knight2)
                            choosen=0
                        if 60*a>black_knight2.left+60 and 60*b>black_knight2.top+60 and 60*a<black_knight2.left+120 and 60*b<black_knight2.top+120:
                            black_knight2.left=60*a-30
                            black_knight2.top =60*b+90
                            blackeatwhite(black_knight2)
                            choosen=0
                        if 60*a>black_knight2.left+120 and 60*b>black_knight2.top and 60*a<black_knight2.left+180 and 60*b<black_knight2.top+60:
                            black_knight2.left=60*a-30
                            black_knight2.top =60*b+90
                            blackeatwhite(black_knight2)
                            choosen=0
                        if 60*a>black_knight2.left+120 and 60*b>black_knight2.top-120 and 60*a<black_knight2.left+180 and 60*b<black_knight2.top-60:
                            black_knight2.left=60*a-30
                            black_knight2.top =60*b+90
                            blackeatwhite(black_knight2)
                            choosen=0
                        if 60*a>black_knight2.left+60 and 60*b>black_knight2.top-180 and 60*a<black_knight2.left+120 and 60*b<black_knight2.top-120:
                            black_knight2.left=60*a-30
                            black_knight2.top =60*b+90
                            blackeatwhite(black_knight2)
                            choosen=0
                        if 60*a>black_knight2.left-60 and 60*b>black_knight2.top-180 and 60*a<black_knight2.left and 60*b<black_knight2.top-120:
                            black_knight2.left=60*a-30
                            black_knight2.top =60*b+90
                            blackeatwhite(black_knight2)
                            choosen=0
                        if 60*a>black_knight2.left-120 and 60*b>black_knight2.top-120 and 60*a<black_knight2.left-60 and 60*b<black_knight2.top-60:
                            black_knight2.left=60*a-30
                            black_knight2.top =60*b+90
                            blackeatwhite(black_knight2)
                            choosen=0
                        elif():
                            choosen=0
                    elif choosen==white_knight1:
                        if 60*a>white_knight1.left-60 and 60*b>white_knight1.top+60 and 60*a<white_knight1.left and 60*b<white_knight1.top+120:
                            white_knight1.left=60*a-30
                            white_knight1.top =60*b+30
                            whiteeatblack(white_knight1)
                            choosen=0
                        if 60*a>white_knight1.left-120 and 60*b>white_knight1.top and 60*a<white_knight1.left-60 and 60*b<white_knight1.top+60:
                            white_knight1.left=60*a-30
                            white_knight1.top =60*b+30
                            whiteeatblack(white_knight1)
                            choosen=0
                        if 60*a>white_knight1.left+60 and 60*b>white_knight1.top+60 and 60*a<white_knight1.left+120 and 60*b<white_knight1.top+120:
                            white_knight1.left=60*a-30
                            white_knight1.top =60*b+30
                            whiteeatblack(white_knight1)
                            choosen=0
                        if 60*a>white_knight1.left+120 and 60*b>white_knight1.top and 60*a<white_knight1.left+180 and 60*b<white_knight1.top+60:
                            white_knight1.left=60*a-30
                            white_knight1.top =60*b+30
                            whiteeatblack(white_knight1)
                            choosen=0
                        if 60*a>white_knight1.left+120 and 60*b>white_knight1.top-120 and 60*a<white_knight1.left+180 and 60*b<white_knight1.top-60:
                            white_knight1.left=60*a-30
                            white_knight1.top =60*b+30
                            whiteeatblack(white_knight1)
                            choosen=0
                        if 60*a>white_knight1.left+60 and 60*b>white_knight1.top-180 and 60*a<white_knight1.left+120 and 60*b<white_knight1.top-120:
                            white_knight1.left=60*a-30
                            white_knight1.top =60*b+30
                            whiteeatblack(white_knight1)
                            choosen=0
                        if 60*a>white_knight1.left-60 and 60*b>white_knight1.top-180 and 60*a<white_knight1.left and 60*b<white_knight1.top-120:
                            white_knight1.left=60*a-30
                            white_knight1.top =60*b+30
                            whiteeatblack(white_knight1)
                            choosen=0
                        if 60*a>white_knight1.left-120 and 60*b>white_knight1.top-120 and 60*a<white_knight1.left-60 and 60*b<white_knight1.top-60:
                            white_knight1.left=60*a-30
                            white_knight1.top =60*b+30
                            whiteeatblack(white_knight1)
                            choosen=0
                        elif():
                            choosen=0
                    elif choosen==white_knight2:
                        if 60*a>white_knight2.left-60 and 60*b>white_knight2.top+60 and 60*a<white_knight2.left and 60*b<white_knight2.top+120:
                            white_knight2.left=60*a-30
                            white_knight2.top =60*b+30
                            whiteeatblack(white_knight2)
                            choosen=0
                        if 60*a>white_knight2.left-120 and 60*b>white_knight2.top and 60*a<white_knight2.left-60 and 60*b<white_knight2.top+60:
                            white_knight2.left=60*a-30
                            white_knight2.top =60*b+30
                            whiteeatblack(white_knight2)
                            choosen=0
                        if 60*a>white_knight2.left+60 and 60*b>white_knight2.top+60 and 60*a<white_knight2.left+120 and 60*b<white_knight2.top+120:
                            white_knight2.left=60*a-30
                            white_knight2.top =60*b+30
                            whiteeatblack(white_knight2)
                            choosen=0
                        if 60*a>white_knight2.left+120 and 60*b>white_knight2.top and 60*a<white_knight2.left+180 and 60*b<white_knight2.top+60:
                            white_knight2.left=60*a-30
                            white_knight2.top =60*b+30
                            whiteeatblack(white_knight2)
                            choosen=0
                        if 60*a>white_knight2.left+120 and 60*b>white_knight2.top-120 and 60*a<white_knight2.left+180 and 60*b<white_knight2.top-60:
                            white_knight2.left=60*a-30
                            white_knight2.top =60*b+30
                            whiteeatblack(white_knight2)
                            choosen=0
                        if 60*a>white_knight2.left+60 and 60*b>white_knight2.top-180 and 60*a<white_knight2.left+120 and 60*b<white_knight2.top-120:
                            white_knight2.left=60*a-30
                            white_knight2.top =60*b+30
                            whiteeatblack(white_knight2)
                            choosen=0
                        if 60*a>white_knight2.left-60 and 60*b>white_knight2.top-180 and 60*a<white_knight2.left and 60*b<white_knight2.top-120:
                            white_knight2.left=60*a-30
                            white_knight2.top =60*b+30
                            whiteeatblack(white_knight2)
                            choosen=0
                        if 60*a>white_knight2.left-120 and 60*b>white_knight2.top-120 and 60*a<white_knight2.left-60 and 60*b<white_knight2.top-60:
                            white_knight2.left=60*a-30
                            white_knight2.top =60*b+30
                            whiteeatblack(white_knight2)
                            choosen=0
                        elif():
                            choosen=0
                    elif choosen==white_rock1:
                        if 60*a>white_rock1.left and 60*a<white_rock1.left+60:
                            white_rock1.left=60*a-30
                            white_rock1.top =60*b+30                                    
                            whiteeatblack(white_rock1)
                            choosen=0
                        if 60*b>white_rock1.top-60 and 60*b<white_rock1.top:
                            white_rock1.left=60*a-30
                            white_rock1.top =60*b+30                                  
                            whiteeatblack(white_rock1)
                            choosen=0
                        elif():
                            choosen=0
                    elif choosen==white_rock2:
                        if 60*a>white_rock2.left and 60*a<white_rock2.left+60:
                            white_rock2.left=60*a-30
                            white_rock2.top =60*b+30                                  
                            whiteeatblack(white_rock2)
                            choosen=0
                        if 60*b>white_rock2.top-60 and 60*b<white_rock2.top:
                            white_rock2.left=60*a-30
                            white_rock2.top =60*b+30                                  
                            whiteeatblack(white_rock2)
                            choosen=0
                        elif():
                            choosen=0
                    elif choosen==black_rock1:
                        if 60*a>black_rock1.left and 60*a<black_rock1.left+60:
                            black_rock1.left=60*a-30
                            black_rock1.top =60*b+30                                                                      
                            blackeatwhite(black_rock1)
                            choosen=0
                        if 60*b>black_rock1.top-60 and 60*b<black_rock1.top:
                            black_rock1.left=60*a-30
                            black_rock1.top =60*b+30                                                                      
                            blackeatwhite(black_rock1)
                            choosen=0
                        elif():
                            choosen=0
                    elif choosen==black_rock2:
                        if 60*a>black_rock2.left and 60*a<black_rock2.left+60:
                            black_rock2.left=60*a-30
                            black_rock2.top =60*b+30                                                                      
                            blackeatwhite(black_rock2)
                            choosen=0
                        if 60*b>black_rock2.top-60 and 60*b<black_rock2.top:
                            black_rock2.left=60*a-30
                            black_rock2.top =60*b+30                                                                      
                            blackeatwhite(black_rock2)
                            choosen=0
                        elif():
                            choosen=0
                    elif choosen==black_queen:
                        for c in range(-9,9,1):
                            if 60*a>black_queen.left-60*c and 60*a<black_queen.left-60*c-60 and 60*b>black_queen.top+60*c and 60*b<black_queen.top+60*c+60:
                                black_queen.left=60*a-30
                                black_queen.top =60*b+30                                                                      
                                blackeatwhite(black_queen)
                                choosen=0
                            if 60*a>black_queen.left-60*c and 60*a<black_queen.left-60*c-60 and 60*b>black_queen.top-60*c-120 and 60*b<black_queen.top-60*c-60:
                                black_queen.left=60*a-30
                                black_queen.top =60*b+30                                                                      
                                blackeatwhite(black_queen)
                                choosen=0
                            if 60*a>black_queen.left+60*c+60 and 60*a<black_queen.left+60*c+120 and 60*b>black_queen.top+60*c and 60*b<black_queen.top+60*c+60:
                                black_queen.left=60*a-30
                                black_queen.top =60*b+30                                                                      
                                blackeatwhite(black_queen)
                                choosen=0
                            if 60*a>black_queen.left+60*c+60 and 60*a<black_queen.left+60*c+120 and 60*b>black_queen.top-60*c-120 and 60*b<black_queen.top-60*c-60:
                                black_queen.left=60*a-30
                                black_queen.top =60*b+30                                                                      
                                blackeatwhite(black_queen)
                                choosen=0
                            if 60*a>black_queen.left and 60*a<black_queen.left+60:
                                black_queen.left=60*a-30
                                black_queen.top =60*b+30                                                                      
                                blackeatwhite(black_queen)
                                choosen=0
                            if 60*b>black_queen.top-60 and 60*b<black_queen.top:
                                black_queen.left=60*a-30
                                black_queen.top =60*b+30                                                                      
                                blackeatwhite(black_queen)
                                choosen=0                                        
                            elif():
                                choosen=0
                    elif choosen==white_queen:
                        for c in range(-9,9,1):
                            if 60*a>white_queen.left-60*c and 60*a<white_queen.left-60*c-60 and 60*b>white_queen.top+60*c and 60*b<white_queen.top+60*c+60:
                                white_queen.left=60*a-30
                                white_queen.top =60*b+30                                                                      
                                whiteeatblack(white_queen)
                                choosen=0
                            if 60*a>white_queen.left-60*c and 60*a<white_queen.left-60*c-60 and 60*b>white_queen.top-60*c-120 and 60*b<white_queen.top-60*c-60:
                                white_queen.left=60*a-30
                                white_queen.top =60*b+30                                                                     
                                whiteeatblack(white_queen)
                                choosen=0
                            if 60*a>white_queen.left+60*c+60 and 60*a<white_queen.left+60*c+120 and 60*b>white_queen.top+60*c and 60*b<white_queen.top+60*c+60:
                                white_queen.left=60*a-30
                                white_queen.top =60*b+30                                                                     
                                whiteeatblack(white_queen)
                                choosen=0
                            if 60*a>white_queen.left+60*c+60 and 60*a<white_queen.left+60*c+120 and 60*b>white_queen.top-60*c-120 and 60*b<white_queen.top-60*c-60:
                                white_queen.left=60*a-30
                                white_queen.top =60*b+30                                                                     
                                whiteeatblack(white_queen)
                                choosen=0
                            if 60*a>white_queen.left and 60*a<white_queen.left+60:
                                white_queen.left=60*a-30
                                white_queen.top =60*b+30                                                                     
                                whiteeatblack(white_queen)
                                choosen=0
                            if 60*b>black_queen.top-60 and 60*b<white_queen.top:
                                white_queen.left=60*a-30
                                white_queen.top =60*b+30                                                                     
                                whiteeatblack(white_queen)
                                choosen=0
                            
                            elif():
                                choosen=0
                                
                    elif choosen==white_bishop1:                            
                        for c in range(-8,8,1):
                            if 60*a>white_bishop1.left-60*c and 60*a<white_bishop1.left-60*c-60 and 60*b>white_bishop1.top+60*c and 60*b<white_bishop1.top+60*c+60:
                                white_bishop1.left=60*a-30
                                white_bishop1.top =60*b+30                                                                     
                                whiteeatblack(white_bishop1)
                                choosen=0
                            if 60*a>white_bishop1.left-60*c and 60*a<white_bishop1.left-60*c-60 and 60*b>white_bishop1.top-60*c-120 and 60*b<white_bishop1.top-60*c-60:
                                white_bishop1.left=60*a-30
                                white_bishop1.top =60*b+30                                                                    
                                whiteeatblack(white_bishop1)
                                choosen=0
                            if 60*a>white_bishop1.left+60*c+60 and 60*a<white_bishop1.left+60*c+120 and 60*b>white_bishop1.top+60*c and 60*b<white_bishop1.top+60*c+60:
                                white_bishop1.left=60*a-30
                                white_bishop1.top =60*b+30                                                                    
                                whiteeatblack(white_bishop1)
                                choosen=0
                            if 60*a>white_bishop1.left+60*c+60 and 60*a<white_bishop1.left+60*c+120 and 60*b>white_bishop1.top-60*c-120 and 60*b<white_bishop1.top-60*c-60:
                                white_bishop1.left=60*a-30
                                white_bishop1.top =60*b+30                                                                    
                                whiteeatblack(white_bishop1)
                                choosen=0
                            elif():
                                choosen=0
                    elif choosen==white_bishop2:                            
                        for c in range(-8,8,1):
                            if 60*a>white_bishop2.left-60*c and 60*a<white_bishop2.left-60*c-60 and 60*b>white_bishop2.top+60*c and 60*b<white_bishop2.top+60*c+60:
                                white_bishop2.left=60*a-30
                                white_bishop2.top =60*b+30                                                                    
                                whiteeatblack(white_bishop2)
                                choosen=0
                            if 60*a>white_bishop2.left-60*c and 60*a<white_bishop2.left-60*c-60 and 60*b>white_bishop2.top-60*c-120 and 60*b<white_bishop2.top-60*c-60:
                                white_bishop2.left=60*a-30
                                white_bishop2.top =60*b+30                                                                    
                                whiteeatblack(white_bishop2)
                                choosen=0
                            if 60*a>white_bishop2.left+60*c+60 and 60*a<white_bishop2.left+60*c+120 and 60*b>white_bishop2.top+60*c and 60*b<white_bishop2.top+60*c+60:
                                white_bishop2.left=60*a-30
                                white_bishop2.top =60*b+30                                                                    
                                whiteeatblack(white_bishop2)
                                choosen=0
                            if 60*a>white_bishop2.left+60*c+60 and 60*a<white_bishop2.left+60*c+120 and 60*b>white_bishop2.top-60*c-120 and 60*b<white_bishop2.top-60*c-60:
                                white_bishop2.left=60*a-30
                                white_bishop2.top =60*b+30                                                                    
                                whiteeatblack(white_bishop2)
                                choosen=0
                            elif():
                                choosen=0
                    elif choosen==black_bishop1:                            
                        for c in range(-8,8,1):
                            if 60*a>black_bishop1.left-60*c and 60*a<black_bishop1.left-60*c-60 and 60*b>black_bishop1.top+60*c and 60*b<black_bishop1.top+60*c+60:
                                black_bishop1.left=60*a-30
                                black_bishop1.top =60*b+30                                                                    
                                blackeatwhite(black_bishop1)
                                choosen=0
                            if 60*a>black_bishop1.left-60*c and 60*a<black_bishop1.left-60*c-60 and 60*b>black_bishop1.top-60*c-120 and 60*b<black_bishop1.top-60*c-60:
                                black_bishop1.left=60*a-30
                                black_bishop1.top =60*b+30                                                                    
                                blackeatwhite(black_bishop1)
                                choosen=0
                            if 60*a>black_bishop1.left+60*c+60 and 60*a<black_bishop1.left+60*c+120 and 60*b>black_bishop1.top+60*c and 60*b<black_bishop1.top+60*c+60:
                                black_bishop1.left=60*a-30
                                black_bishop1.top =60*b+30                                                                    
                                blackeatwhite(black_bishop1)
                                choosen=0
                            if 60*a>black_bishop1.left+60*c+60 and 60*a<black_bishop1.left+60*c+120 and 60*b>black_bishop1.top-60*c-120 and 60*b<black_bishop1.top-60*c-60:
                                black_bishop1.left=60*a-30
                                black_bishop1.top =60*b+30                                                                    
                                blackeatwhite(black_bishop1)
                                choosen=0
                            elif():
                                choosen=0
                    elif choosen==black_bishop2:                            
                        for c in range(-8,8,1):
                            if 60*a>black_bishop2.left-60*c and 60*a<black_bishop2.left-60*c-60 and 60*b>black_bishop2.top+60*c and 60*b<black_bishop2.top+60*c+60:
                                black_bishop2.left=60*a-30
                                black_bishop2.top =60*b+30                                                                    
                                blackeatwhite(black_bishop2)
                                choosen=0
                            if 60*a>black_bishop2.left-60*c and 60*a<black_bishop2.left-60*c-60 and 60*b>black_bishop2.top-60*c-120 and 60*b<black_bishop2.top-60*c-60:
                                black_bishop2.left=60*a-30
                                black_bishop2.top =60*b+30                                                                    
                                blackeatwhite(black_bishop2)
                                choosen=0
                            if 60*a>black_bishop2.left+60*c+60 and 60*a<black_bishop2.left+60*c+120 and 60*b>black_bishop2.top+60*c and 60*b<black_bishop2.top+60*c+60:
                                black_bishop2.left=60*a-30
                                black_bishop2.top =60*b+30                                                                    
                                blackeatwhite(black_bishop2)
                                choosen=0
                            if 60*a>black_bishop2.left+60*c+60 and 60*a<black_bishop2.left+60*c+120 and 60*b>black_bishop2.top-60*c-120 and 60*b<black_bishop2.top-60*c-60:
                                black_bishop2.left=60*a-30
                                black_bishop2.top =60*b+30                                                                    
                                blackeatwhite(black_bishop2)
                                choosen=0
                            elif():
                                choosen=0
                    elif choosen==white_soldier1:
                        if white_soldier1.left==30 and white_soldier1.top==150 and 60*a>white_soldier1.left and 60*a<white_soldier1.left+60 and 60*b>white_soldier1.top and 60*b<white_soldier1.top+120:
                            white_soldier1.left=60*a-30
                            white_soldier1.top =60*b+30
                            
                        if white_soldier1.left!=30 and white_soldier1.top!=150 and 60*a>white_soldier1.left and 60*a<white_soldier1.left+60 and 60*b>white_soldier1.top and 60*b<white_soldier1.top+60:
                            white_soldier1.left=60*a-30
                            white_soldier1.top =60*b+30
                        if 60*a>white_soldier1.left-60 and 60*b>white_soldier1.top and 60*a<white_soldier1.left and 60*b<white_soldier1.top+60:
                            white_soldier1.left=60*a-30
                            white_soldier1.top =60*b+30
                            whiteeatblack(white_soldier1)
                            choosen=0
                        if 60*a>white_soldier1.left+60 and 60*b>white_soldier1.top and 60*a<white_soldier1.left+120 and 60*b<white_soldier1.top+60:
                            white_soldier1.left=60*a-30
                            white_soldier1.top =60*b+30
                            whiteeatblack(white_soldier1)
                            choosen=0 
                        elif():
                            choosen=0
                    elif choosen==white_soldier2:
                        if white_soldier2.left==90 and white_soldier2.top==150 and 60*a>white_soldier2.left and 60*a<white_soldier2.left+60 and 60*b>white_soldier2.top and 60*b<white_soldier2.top+120:
                            white_soldier2.left=60*a-30
                            white_soldier2.top =60*b+30
                        if white_soldier2.left!=90 and white_soldier2.top!=150 and 60*a>white_soldier2.left and 60*a<white_soldier2.left+60 and 60*b>white_soldier2.top and 60*b<white_soldier2.top+60:
                            white_soldier2.left=60*a-30
                            white_soldier2.top =60*b+30
                        if 60*a>white_soldier2.left-60 and 60*b>white_soldier1.top and 60*a<white_soldier2.left and 60*b<white_soldier2.top+60:
                            white_soldier2.left=60*a-30
                            white_soldier2.top =60*b+30
                            whiteeatblack(white_soldier2)
                            choosen=0
                        if 60*a>white_soldier2.left+60 and 60*b>white_soldier2.top and 60*a<white_soldier2.left+120 and 60*b<white_soldier2.top+60:
                            white_soldier2.left=60*a-30
                            white_soldier2.top =60*b+30
                            whiteeatblack(white_soldier2)
                            choosen=0 
                        elif():
                            choosen=0
                    elif choosen==white_soldier3:
                        if white_soldier3.left==150 and white_soldier3.top==150 and 60*a>white_soldier3.left and 60*a<white_soldier3.left+60 and 60*b>white_soldier3.top and 60*b<white_soldier3.top+120:
                            white_soldier3.left=60*a-30
                            white_soldier3.top =60*b+30                           
                        if white_soldier3.left!=150 and white_soldier3.top!=150 and 60*a>white_soldier3.left and 60*a<white_soldier3.left+60 and 60*b>white_soldier3.top and 60*b<white_soldier3.top+60:
                            white_soldier3.left=60*a-30
                            white_soldier3.top =60*b+30
                        if 60*a>white_soldier3.left-60 and 60*b>white_soldier3.top and 60*a<white_soldier3.left and 60*b<white_soldier3.top+60:
                            white_soldier3.left=60*a-30
                            white_soldier3.top =60*b+30
                            whiteeatblack(white_soldier3)
                            choosen=0
                        if 60*a>white_soldier3.left+60 and 60*b>white_soldier3.top and 60*a<white_soldier3.left+120 and 60*b<white_soldier3.top+60:
                            white_soldier3.left=60*a-30
                            white_soldier3.top =60*b+30
                            whiteeatblack(white_soldier3)
                            choosen=0 
                        elif():
                            choosen=0
                    elif choosen==white_soldier4:
                        if white_soldier4.left==210 and white_soldier4.top==150 and 60*a>white_soldier4.left and 60*a<white_soldier4.left+60 and 60*b>white_soldier4.top and 60*b<white_soldier4.top+120:
                            white_soldier4.left=60*a-30
                            white_soldier4.top =60*b+30
                        if white_soldier4.left!=210 and white_soldier4.top!=150 and 60*a>white_soldier4.left and 60*a<white_soldier4.left+60 and 60*b>white_soldier4.top and 60*b<white_soldier4.top+60:
                            white_soldier4.left=60*a-30
                            white_soldier4.top =60*b+30
                        if 60*a>white_soldier4.left-60 and 60*b>white_soldier4.top and 60*a<white_soldier4.left and 60*b<white_soldier4.top+60:
                            white_soldier4.left=60*a-30
                            white_soldier4.top =60*b+30
                            whiteeatblack(white_soldier4)
                            choosen=0
                        if 60*a>white_soldier4.left+60 and 60*b>white_soldier4.top and 60*a<white_soldier4.left+120 and 60*b<white_soldier4.top+60:
                            white_soldier4.left=60*a-30
                            white_soldier4.top =60*b+30
                            whiteeatblack(white_soldier4)
                            choosen=0 
                        elif():
                            choosen=0
                    elif choosen==white_soldier5:
                        if white_soldier5.left==270 and white_soldier5.top==150 and 60*a>white_soldier5.left and 60*a<white_soldier5.left+60 and 60*b>white_soldier5.top and 60*b<white_soldier5.top+120:
                            white_soldier5.left=60*a-30
                            white_soldier5.top =60*b+30
                        if white_soldier5.left!=270 and white_soldier5.top!=150 and 60*a>white_soldier5.left and 60*a<white_soldier5.left+60 and 60*b>white_soldier5.top and 60*b<white_soldier5.top+60:
                            white_soldier5.left=60*a-30
                            white_soldier5.top =60*b+30
                        if 60*a>white_soldier5.left-60 and 60*b>white_soldier5.top and 60*a<white_soldier5.left and 60*b<white_soldier5.top+60:
                            white_soldier5.left=60*a-30
                            white_soldier5.top =60*b+30
                            whiteeatblack(white_soldier5)
                            choosen=0
                        if 60*a>white_soldier5.left+60 and 60*b>white_soldier5.top and 60*a<white_soldier5.left+120 and 60*b<white_soldier5.top+60:
                            white_soldier5.left=60*a-30
                            white_soldier5.top =60*b+30
                            whiteeatblack(white_soldier5)
                            choosen=0 
                        elif():
                            choosen=0
                    elif choosen==white_soldier6:
                        if white_soldier6.left==330 and white_soldier6.top==150 and 60*a>white_soldier6.left and 60*a<white_soldier6.left+60 and 60*b>white_soldier6.top and 60*b<white_soldier6.top+120:
                            white_soldier6.left=60*a-30
                            white_soldier6.top =60*b+30
                        if white_soldier6.left!=330 and white_soldier6.top!=150 and 60*a>white_soldier6.left and 60*a<white_soldier6.left+60 and 60*b>white_soldier6.top and 60*b<white_soldier6.top+60:
                            white_soldier6.left=60*a-30
                            white_soldier6.top =60*b+30
                        if 60*a>white_soldier6.left-60 and 60*b>white_soldier6.top and 60*a<white_soldier6.left and 60*b<white_soldier6.top+60:
                            white_soldier6.left=60*a-30
                            white_soldier6.top =60*b+30
                            whiteeatblack(white_soldier6)
                            choosen=0
                        if 60*a>white_soldier6.left+60 and 60*b>white_soldier6.top and 60*a<white_soldier6.left+120 and 60*b<white_soldier6.top+60:
                            white_soldier6.left=60*a-30
                            white_soldier6.top =60*b+30
                            whiteeatblack(white_soldier6)
                            choosen=0 
                        elif():
                            choosen=0
                    elif choosen==white_soldier7:
                        if white_soldier7.left==390 and white_soldier7.top==150 and 60*a>white_soldier7.left and 60*a<white_soldier7.left+60 and 60*b>white_soldier7.top and 60*b<white_soldier7.top+120:
                            white_soldier7.left=60*a-30
                            white_soldier7.top =60*b+30
                        if white_soldier7.left!=390 and white_soldier7.top!=150 and 60*a>white_soldier7.left and 60*a<white_soldier7.left+60 and 60*b>white_soldier7.top and 60*b<white_soldier7.top+60:
                            white_soldier7.left=60*a-30
                            white_soldier7.top =60*b+30
                        if 60*a>white_soldier7.left-60 and 60*b>white_soldier7.top and 60*a<white_soldier7.left and 60*b<white_soldier7.top+60:
                            white_soldier7.left=60*a-30
                            white_soldier7.top =60*b+30
                            whiteeatblack(white_soldier7)
                            choosen=0
                        if 60*a>white_soldier7.left+60 and 60*b>white_soldier7.top and 60*a<white_soldier7.left+120 and 60*b<white_soldier7.top+60:
                            white_soldier7.left=60*a-30
                            white_soldier7.top =60*b+30
                            whiteeatblack(white_soldier7)
                            choosen=0 
                        elif():
                            choosen=0
                    elif choosen==white_soldier8:
                        if white_soldier8.left==450 and white_soldier8.top==150 and 60*a>white_soldier8.left and 60*a<white_soldier8.left+60 and 60*b>white_soldier8.top and 60*b<white_soldier8.top+120:
                            white_soldier8.left=60*a-30
                            white_soldier8.top =60*b+30
                        if white_soldier8.left!=450 and white_soldier8.top!=150 and 60*a>white_soldier8.left and 60*a<white_soldier8.left+60 and 60*b>white_soldier8.top and 60*b<white_soldier8.top+60:
                            white_soldier8.left=60*a-30
                            white_soldier8.top =60*b+30
                        if 60*a>white_soldier8.left-60 and 60*b>white_soldier8.top and 60*a<white_soldier8.left and 60*b<white_soldier8.top+60:
                            white_soldier8.left=60*a-30
                            white_soldier8.top =60*b+30
                            whiteeatblack(white_soldier8)
                            choosen=0
                        if 60*a>white_soldier8.left+60 and 60*b>white_soldier8.top and 60*a<white_soldier8.left+120 and 60*b<white_soldier8.top+60:
                            white_soldier8.left=60*a-30
                            white_soldier8.top =60*b+30
                            whiteeatblack(white_soldier8)
                            choosen=0 
                        elif():
                            choosen=0
                    elif choosen==black_soldier1:
                        print 4
                        if black_soldier1.left==30 and black_soldier1.top==450 and 60*a-30>black_soldier1.left and 60*a+30<black_soldier1.left+60 and 60*b+30>black_soldier1.top and 60*b+90<black_soldier1.top+120:
                            black_soldier1.left=60*a-30
                            black_soldier1.top =60*b+90
                            print black_soldier1
                        if black_soldier1.left!=30 and black_soldier1.top!=450 and 60*a-30>black_soldier1.left and 60*a+30<black_soldier1.left+60 and 60*b+30>black_soldier1.top and 60*b+90<black_soldier1.top+60:
                            black_soldier1.left=60*a-30
                            black_soldier1.top =60*b+90
                            print black_soldier1
                        if 60*a>black_soldier1.left-60 and 60*b>black_soldier1.top-120 and 60*a<black_soldier1.left and 60*b<black_soldier1.top-60:
                            black_soldier1.left=60*a-30
                            black_soldier1.top =60*b+90
                            blackeatwhite(black_soldier1)
                            print black_soldier1
                            choosen=0
                        if 60*a>black_soldier1.left+60 and 60*b>black_soldier1.top-120 and 60*a<black_soldier1.left+120 and 60*b<black_soldier1.top-60:
                            black_soldier1.left=60*a-30
                            black_soldier1.top =60*b+90
                            blackeatwhite(black_soldier1)
                            print black_soldier1
                            choosen=0 
                        elif():
                            print black_soldier1
                            choosen=0
                        print choosen
                    elif choosen==black_soldier2:
                        if black_soldier2.left==90 and black_soldier2.top==450 and 60*a>black_soldier2.left and 60*a<black_soldier2.left+60 and 60*b>black_soldier2.top and 60*b<black_soldier2.top+120:
                            black_soldier2.left=60*a-30
                            black_soldier2.top =60*b+30
                        if black_soldier2.left!=90 and black_soldier2.top!=450 and 60*a>black_soldier2.left and 60*a<black_soldier2.left+60 and 60*b>black_soldier2.top and 60*b<black_soldier2.top+60:
                            black_soldier2.left=60*a-30
                            black_soldier2.top =60*b+30
                        if 60*a>black_soldier2.left-60 and 60*b>black_soldier1.top-120 and 60*a<black_soldier2.left and 60*b<black_soldier2.top-60:
                            black_soldier2.left=60*a-30
                            black_soldier2.top =60*b+30
                            blackeatwhite(black_soldier2)
                            choosen=0
                        if 60*a>black_soldier2.left+60 and 60*b>black_soldier2.top-120 and 60*a<black_soldier2.left+120 and 60*b<black_soldier2.top-60:
                            black_soldier2.left=60*a-30
                            black_soldier2.top =60*b+30
                            blackeatwhite(black_soldier2)
                            choosen=0 
                        elif():
                            choosen=0
                    elif choosen==black_soldier3:
                        if black_soldier3.left==150 and black_soldier3.top==450 and 60*a>black_soldier3.left and 60*a<black_soldier3.left+60 and 60*b>black_soldier3.top and 60*b<black_soldier3.top+120:
                            black_soldier3.left=60*a-30
                            black_soldier3.top =60*b+30                           
                        if black_soldier3.left!=150 and black_soldier3.top!=450 and 60*a>black_soldier3.left and 60*a<black_soldier3.left+60 and 60*b>black_soldier3.top and 60*b<black_soldier3.top+60:
                            black_soldier3.left=60*a-30
                            black_soldier3.top =60*b+30
                        if 60*a>black_soldier3.left-60 and 60*b>black_soldier3.top-120 and 60*a<black_soldier3.left and 60*b<black_soldier3.top-60:
                            black_soldier3.left=60*a-30
                            black_soldier3.top =60*b+30
                            blackeatwhite(black_soldier1)
                            choosen=0
                        if 60*a>black_soldier3.left+60 and 60*b>black_soldier3.top-120 and 60*a<black_soldier3.left+120 and 60*b<black_soldier3.top-60:
                            black_soldier3.left=60*a-30
                            black_soldier3.top =60*b+30
                            blackeatwhite(black_soldier3)
                            choosen=0 
                        elif():
                            choosen=0
                    elif choosen==black_soldier4:
                        if black_soldier4.left==210 and black_soldier4.top==450 and 60*a>black_soldier4.left and 60*a<black_soldier4.left+60 and 60*b>black_soldier4.top and 60*b<black_soldier4.top+120:
                            black_soldier4.left=60*a-30
                            black_soldier4.top =60*b+30
                        if black_soldier4.left!=210 and black_soldier4.top!=450 and 60*a>black_soldier4.left and 60*a<black_soldier4.left+60 and 60*b>black_soldier4.top and 60*b<black_soldier4.top+60:
                            black_soldier4.left=60*a-30
                            black_soldier4.top =60*b+30
                        if 60*a>black_soldier4.left-60 and 60*b>black_soldier4.top-120 and 60*a<black_soldier4.left and 60*b<black_soldier4.top-60:
                            black_soldier4.left=60*a-30
                            black_soldier4.top =60*b+30
                            blackeatwhite(black_soldier4)
                            choosen=0
                        if 60*a>black_soldier4.left+60 and 60*b>black_soldier4.top-120 and 60*a<black_soldier4.left+120 and 60*b<black_soldier4.top-60:
                            black_soldier4.left=60*a-30
                            black_soldier4.top =60*b+30
                            blackeatwhite(black_soldier4)
                            choosen=0 
                        elif():
                            choosen=0
                    elif choosen==black_soldier5:
                        if black_soldier5.left==270 and black_soldier5.top==450 and 60*a>black_soldier5.left and 60*a<black_soldier5.left+60 and 60*b>black_soldier5.top and 60*b<black_soldier5.top+120:
                            black_soldier5.left=60*a-30
                            black_soldier5.top =60*b+30
                        if black_soldier5.left!=270 and black_soldier5.top!=450 and 60*a>black_soldier5.left and 60*a<black_soldier5.left+60 and 60*b>black_soldier5.top and 60*b<black_soldier5.top+60:
                            black_soldier5.left=60*a-30
                            black_soldier5.top =60*b+30
                        if 60*a>black_soldier5.left-60 and 60*b>black_soldier5.top-120 and 60*a<black_soldier5.left and 60*b<black_soldier5.top-60:
                            black_soldier5.left=60*a-30
                            black_soldier5.top =60*b+30
                            blackeatwhite(black_soldier1)
                            choosen=0
                        if 60*a>black_soldier5.left+60 and 60*b>black_soldier5.top-120 and 60*a<black_soldier5.left+120 and 60*b<black_soldier5.top-60:
                            black_soldier5.left=60*a-30
                            black_soldier5.top =60*b+30
                            blackeatwhite(black_soldier5)
                            choosen=0 
                        elif():
                            choosen=0
                    elif choosen==black_soldier6:
                        if black_soldier6.left==330 and black_soldier6.top==450 and 60*a>black_soldier6.left and 60*a<black_soldier6.left+60 and 60*b>black_soldier6.top and 60*b<black_soldier6.top+120:
                            black_soldier6.left=60*a-30
                            black_soldier6.top =60*b+30
                        if black_soldier6.left!=330 and black_soldier6.top!=450 and 60*a>black_soldier6.left and 60*a<black_soldier6.left+60 and 60*b>black_soldier6.top and 60*b<black_soldier6.top+60:
                            black_soldier6.left=60*a-30
                            black_soldier6.top =60*b+30
                        if 60*a>black_soldier6.left-60 and 60*b>black_soldier6.top-120 and 60*a<black_soldier6.left and 60*b<black_soldier6.top-60:
                            black_soldier6.left=60*a-30
                            black_soldier6.top =60*b+30
                            blackeatwhite(black_soldier1)
                            choosen=0
                        if 60*a>black_soldier6.left+60 and 60*b>black_soldier6.top-120 and 60*a<black_soldier6.left+120 and 60*b<black_soldier6.top-60:
                            black_soldier6.left=60*a-30
                            black_soldier6.top =60*b+30
                            blackeatwhite(black_soldier6)
                            choosen=0 
                        elif():
                            choosen=0
                    elif choosen==black_soldier7:
                        if black_soldier7.left==390 and black_soldier7.top==450 and 60*a>black_soldier7.left and 60*a<black_soldier7.left+60 and 60*b>black_soldier7.top and 60*b<black_soldier7.top+120:
                            black_soldier7.left=60*a-30
                            black_soldier7.top =60*b+30
                        if black_soldier7.left!=390 and black_soldier7.top!=450 and 60*a>black_soldier7.left and 60*a<black_soldier7.left+60 and 60*b>black_soldier7.top and 60*b<black_soldier7.top+60:
                            black_soldier7.left=60*a-30
                            black_soldier7.top =60*b+30
                        if 60*a>black_soldier7.left-60 and 60*b>black_soldier7.top-120 and 60*a<black_soldier7.left and 60*b<black_soldier7.top-60:
                            black_soldier7.left=60*a-30
                            black_soldier7.top =60*b+30
                            blackeatwhite(black_soldier7)
                            choosen=0
                        if 60*a>black_soldier7.left+60 and 60*b>black_soldier7.top-120 and 60*a<black_soldier7.left+120 and 60*b<black_soldier7.top-60:
                            black_soldier7.left=60*a-30
                            black_soldier7.top =60*b+30
                            blackeatwhite(black_soldier7)
                            choosen=0 
                        elif():
                            choosen=0
                    elif choosen==black_soldier8:
                        if black_soldier8.left==450 and black_soldier8.top==450 and 60*a>black_soldier8.left and 60*a<black_soldier8.left+60 and 60*b>black_soldier8.top and 60*b<black_soldier8.top+120:
                            black_soldier8.left=60*a-30
                            black_soldier8.top =60*b+30
                        if black_soldier8.left!=450 and black_soldier8.top!=450 and 60*a>black_soldier8.left and 60*a<black_soldier8.left+60 and 60*b>black_soldier8.top and 60*b<black_soldier8.top+60:
                            black_soldier8.left=60*a-30
                            black_soldier8.top =60*b+30
                        if 60*a>black_soldier8.left-60 and 60*b>black_soldier8.top-120 and 60*a<black_soldier8.left and 60*b<black_soldier8.top-60:
                            black_soldier8.left=60*a-30
                            black_soldier8.top =60*b+30
                            blackeatwhite(black_soldier8)
                            choosen=0
                        if 60*a>black_soldier8.left+60 and 60*b>black_soldier8.top-120 and 60*a<black_soldier8.left+120 and 60*b<black_soldier8.top-60:
                            black_soldier8.left=60*a-30
                            black_soldier8.top =60*b+30
                            blackeatwhite(black_soldier8)
                            choosen=0 
                        elif():
                            choosen=0

            
def draw_where_can_chess_move(x,y,chess):
    if chees==black_king:
        if x==1 and y==1:
            for m,n in range((x,y),(x+1,y+1),1):
                plase = pygame.Rect(x*60-30, y*60+30, CELLSIZE, CELLSIZE)
                pygame.draw.rect(DISPLAYSURF, BLUE, plase)
        if x==1 and y!=1:
            for m,n in range((x,y-1),(x+1,y+1),1):
                plase = pygame.Rect(x*60-30, y*60+30, CELLSIZE, CELLSIZE)
                pygame.draw.rect(DISPLAYSURF, BLUE, plase)
        if y==1 and x!=1:
            for m,n in range((x-1,y),(x+1,y+1),1):
                plase = pygame.Rect(x*60-30, y*60+30, CELLSIZE, CELLSIZE)
                pygame.draw.rect(DISPLAYSURF, BLUE, plase)
        if x==8 and y==8:
            for m,n in range((x-1,y-1),(x,y),1):
                plase = pygame.Rect(x*60-30, y*60+30, CELLSIZE, CELLSIZE)
                pygame.draw.rect(DISPLAYSURF, BLUE, plase)
        if x==8 and y!=8:
            for m,n in range((x-1,y-1),(x,y+1),1):
                plase = pygame.Rect(x*60-30, y*60+30, CELLSIZE, CELLSIZE)
                pygame.draw.rect(DISPLAYSURF, BLUE, plase)
        if y==8 and x!=8:
            for m,n in range((x-1,y-1),(x+1,y),1):
                plase = pygame.Rect(x*60-30, y*60+30, CELLSIZE, CELLSIZE)
                pygame.draw.rect(DISPLAYSURF, BLUE, plase)
        elif():
            for m,n in range((x-1,y-1),(x+1,y+1),1):
                plase = pygame.Rect(x*60-30, y*60+30, CELLSIZE, CELLSIZE)
                pygame.draw.rect(DISPLAYSURF, BLUE, plase)

def drawGrid():
    
    for x in range(30, Chessboardwidth+90, CELLSIZE): # draw vertical lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 30), (x, Chessboardheight+30))
       
    for y in range(30, Chessboardheight+90, CELLSIZE): # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (30, y), (Chessboardwidth+30, y))
 
# When game is over        
def game_over(chess):
    if chess==white_king:
       
       return 'Black'
    if chess==black_king:
        
       return 'White'
def blackeatwhite(chees):
    if chees.left==white_knight1.left and chees.top==white_knight1.top :
        white_knight1.remove(white_knight1)
    elif chees.left==white_knight2.left and chees.top==white_knight2.top :
        white_knight2.remove(white_knight2)
    elif chees.left==white_rock1.left and chees.top==white_rock1.top :
        white_rock1.remove(white_rock1)
    elif chees.left==white_rock2.left and chees.top==white_rock2.top :
        white_rock2.remove(white_rock2)
    elif chees.left==white_bishop1.left and chees.top==white_bishop1.top :
        white_bishop1.remove(white_bishop1)
    elif chees.left==white_bishop2.left and chees.top==white_bishop2.top :
        white_bishop2.remove(white_bishop2)
    elif chees.left==white_queen.left and chees.top==white_queen.top :
        white_queen.remove(white_queen)
    elif chees.left==white_soldier1.left and chees.top==white_soldier1.top :
        white_soldier1.remove(white_soldier1)
    elif chees.left==white_soldier2.left and chees.top==white_soldier2.top :
        white_soldier2.remove(white_soldier2)
    elif chees.left==white_soldier3.left and chees.top==white_soldier3.top :
        white_soldier3.remove(white_soldier3)
    elif chees.left==white_soldier4.left and chees.top==white_soldier4.top :
        white_soldier4.remove(white_soldier4)
    elif chees.left==white_soldier5.left and chees.top==white_soldier5.top :
        white_soldier5.remove(white_soldier5)
    elif chees.left==white_soldier6.left and chees.top==white_soldier6.top :
        white_soldier6.remove(white_soldier6)
    elif chees.left==white_soldier7.left and chees.top==white_soldier7.top :
        white_soldier7.remove(white_soldier7)
    elif chees.left==white_soldier8.left and chees.top==white_soldier8.top :
        white_soldier8.remove(white_soldier8)
    elif chees.left==white_king.left and chees.top==white_king.top :
        white_king.left=0
        white_king.top =0
        
def whiteeatblack(chees):
    if chees.left==black_knight1.left and chees.top==black_knight1.top :
        black_knight1.remove(black_knight1)
    elif chees.left==black_knight2.left and chees.top==black_knight2.top :
        black_knight2.remove(black_knight2)
    elif chees.left==black_rock1.left and chees.top==black_rock1.top :
        black_rock1.remove(black_rock1)
    elif chees.left==black_rock2.left and chees.top==black_rock2.top :
        black_rock2.remove(black_rock2)
    elif chees.left==black_bishop1.left and chees.top==black_bishop1.top :
        black_bishop1.remove(black_bishop1)
    elif chees.left==black_bishop2.left and chees.top==black_bishop2.top :
        black_bishop2.remove(black_bishop2)
    elif chees.left==black_queen.left and chees.top==black_queen.top :
        black_queen.remove(black_queen)
    elif chees.left==black_soldier1.left and chees.top==black_soldier1.top :
        black_soldier1.remove(black_soldier1)
    elif chees.left==black_soldier2.left and chees.top==black_soldier2.top :
        black_soldier2.remove(black_soldier2)
    elif chees.left==black_soldier3.left and chees.top==black_soldier3.top :
        black_soldier3.remove(black_soldier3)
    elif chees.left==black_soldier4.left and chees.top==black_soldier4.top :
        black_soldier4.remove(black_soldier4)
    elif chees.left==black_soldier5.left and chees.top==black_soldier5.top :
        black_soldier5.remove(black_soldier5)
    elif chees.left==black_soldier6.left and chees.top==black_soldier6.top :
        black_soldier6.remove(black_soldier6)
    elif chees.left==black_soldier7.left and chees.top==black_soldier7.top :
        black_soldier7.remove(black_soldier7)
    elif chees.left==black_soldier8.left and chees.top==black_soldier8.top :
        black_soldier8.remove(black_soldier8)
    elif chees.left==black_king.left and chees.top==black_king.top :
        black_king.left=0
        black_king.top =0
def showGameOverScreen(runGame):
    gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
    gameSurf = gameOverFont.render('(%s)', True, WHITE) % (runGame)
    gameRect = gameSurf.get_rect()
    gameRect.midtop = (WINDOWWIDTH / 2, 10)
    DISPLAYSURF.blit(gameSurf, gameRect)
    drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress() # clear out any key presses in the event queue

    while True:
        if checkForKeyPress():
            pygame.event.get() # clear event queue
if __name__ == '__main__':
    main()