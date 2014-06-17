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
WINDOWHEIGHT = 520
CELLSIZE = 60
assert Chessboardwidth % CELLSIZE == 0, "Window width must be a multiple of cell size."
assert Chessboardheight % CELLSIZE == 0, "Window height must be a multiple of cell size."
CELLWIDTH = int(Chessboardwidth / CELLSIZE)
CELLHEIGHT = int(Chessboardheight / CELLSIZE)

LIGHTGRAY    = ( 200, 200, 200)
DARKGRAY     = ( 40 , 40 , 40 )
WHITE        = ( 255, 255, 255)
BLACK        = ( 0  , 0  , 0  )
BLUE         = ( 0  , 243, 253)
def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Chess')

    showStartScreen()
    while True:
        runGame()
        showGameOverScreen()
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
def showStartScreen():
    titleFont = pygame.font.Font('freesansbold.ttf', 20)
    titleSurf1 = titleFont.render('Welcome to CHESS world!', True, WHITE)
    degrees1 = 0
    
    while True:
        DISPLAYSURF.fill(BLACK)
        rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
        rotatedRect1 = rotatedSurf1.get_rect()
        rotatedRect1.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        DISPLAYSURF.blit(rotatedSurf1, rotatedRect1)

        drawPressKeyMsg()

        if checkForKeyPress():
            pygame.event.get() # clear event queue
            return
        pygame.display.update()
        FPSCLOCK.tick(FPS)
def terminate():
    pygame.quit()
    sys.exit()

    #  white
        
white_king = pygame.Rect(260, 20, 60, 60) 
white_kingimage = pygame.image.load('WKING.png')

       
white_queen = pygame.Rect(200, 20, 60, 60) 
white_queenimage = pygame.image.load('WQUEEN.png')
       
white_bishop1 = pygame.Rect(140, 20, 60, 60) 
white_bishop1image=pygame.image.load('WBISHOP.png')
   
white_bishop2 = pygame.Rect(320, 20, 60, 60) 
white_bishop2image=pygame.image.load('WBISHOP.png')
   
white_rock1 =pygame.Rect(20, 20, 60, 60)  
white_rock1image=pygame.image.load('WROCK.png')
    
white_rock2 =pygame.Rect(440, 20, 60, 60)  
white_rock2image=pygame.image.load('WROCK.png')

white_knight1 = pygame.Rect(80, 20, 60, 60) 
white_knight1image=pygame.image.load('WKNIGHT.png')
    
white_knight2 = pygame.Rect(380, 20, 60, 60) 
white_knight2image=pygame.image.load('WKNIGHT.png')
    
white_soldier1 =pygame.Rect(20, 80, 60, 60)  
white_soldier1image=pygame.image.load('WSOLDIER.png')
    
white_soldier2 =pygame.Rect(80, 80, 60, 60) 
white_soldier2image=pygame.image.load('WSOLDIER.png')
    
white_soldier3 =pygame.Rect(140, 80, 60, 60) 
white_soldier3image=pygame.image.load('WSOLDIER.png')
   
white_soldier4 =pygame.Rect(200, 80, 60, 60) 
white_soldier4image=pygame.image.load('WSOLDIER.png')
    
white_soldier5 =pygame.Rect(260, 80, 60, 60)  
white_soldier5image=pygame.image.load('WSOLDIER.png')
    
white_soldier6 =pygame.Rect(320, 80, 60, 60)  
white_soldier6image=pygame.image.load('WSOLDIER.png')
    
white_soldier7 =pygame.Rect(380, 80, 60, 60)  
white_soldier7image=pygame.image.load('WSOLDIER.png')
    
white_soldier8 =pygame.Rect(420, 80, 60, 60)  
white_soldier8image=pygame.image.load('WSOLDIER.png')
    # black
      
black_king = pygame.Rect(260, 440, 60, 60)
black_kingimage=pygame.image.load('BKING.png')
    
black_queen = pygame.Rect(200, 440, 60, 60)
black_queenimage=pygame.image.load('BQUEEN.png')
       
black_bishop1 =pygame.Rect(140, 440, 60, 60) 
black_bishop1image=pygame.image.load('BBISHOP.png')

black_bishop2 =pygame.Rect(320, 440, 60, 60) 
black_bishop2image=pygame.image.load('BBISHOP.png')
    
black_rock1 =pygame.Rect(20, 440, 60, 60) 
black_rock1image=pygame.image.load('BROCK.png')
    
black_rock2 =pygame.Rect(440, 440, 60, 60)
black_rock2image=pygame.image.load('BROCK.png')
   
black_knight1 = pygame.Rect(80, 440, 60, 60)
black_knight1image=pygame.image.load('BKNIGHT.png')
    
black_knight2 = pygame.Rect(380, 440, 60, 60)
black_knight2image=pygame.image.load('BKNIGHT.png')

black_soldier1 =pygame.Rect(20, 380, 60, 60)
black_soldier1image=pygame.image.load('BSOLDIER.png')
   
black_soldier2 =pygame.Rect(80, 380, 60, 60)  
black_soldier2image=pygame.image.load('BSOLDIER.png')
    
black_soldier3 =pygame.Rect(140, 380, 60, 60) 
black_soldier3image=pygame.image.load('BSOLDIER.png')

black_soldier4 =pygame.Rect(200, 380, 60, 60)  
black_soldier4image=pygame.image.load('BSOLDIER.png')
    
black_soldier5 =pygame.Rect(260, 380, 60, 60) 
black_soldier5image=pygame.image.load('BSOLDIER.png')
   
black_soldier6 =pygame.Rect(320, 380, 60, 60) 
black_soldier6image=pygame.image.load('BSOLDIER.png')
    
black_soldier7 =pygame.Rect(380, 380, 60, 60) 
black_soldier7image=pygame.image.load('BSOLDIER.png')
    
black_soldier8 =pygame.Rect(440, 380, 60, 60) 
black_soldier8image=pygame.image.load('BSOLDIER.png')
# Game's main point    
def runGame():
    while True:
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
        drawGrid()
def walk():
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            for a,b in range(8):
                if event.pos[0]>(60*a-30) and event.pos[1]>(60*b-30) and event.pos[0]<(60*a+30) and event.pos[1]<(60*b+30):
                    if (black_king.left+30)>(60*a-30) and (black_king.top-30)>(60*b-30) and (black_king.left+30)<(60*a+30) and (black_king.top-30)<(60*b+30):
                        choosen=black_king
                        
                    elif (black_gueen.left+30)>(60*a-30) and (black_gueen.top-30)>(60*b-30) and (black_gueen.left+30)<(60*a+30) and (black_gueen.top-30)<(60*b+30):
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
                        
                    elif (white_gueen.left+30)>(60*a-30) and (white_gueen.top-30)>(60*b-30) and (white_gueen.left+30)<(60*a+30) and (white_gueen.top-30)<(60*b+30):
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
                        
                    elif:
                        
        if event.type == MOUSEBUTTONUP:
            for a,b in range(8):
                if event.pos[0]>(60*a-30) and event.pos[1]>(60*b-30) and event.pos[0]<(60*a+30) and event.pos[1]<(60*b+30):
                    for c,d in range((-a,-b),(8-a,8-b),1):
                        if choosen==black_king:
                            
                    choosen.left=(60*a-30)
                    choosen.top =(60*b+30)
                   
        
        for chess in chess[:]:
             if eat(chess ['rect'], chess ['rect']):
                chess.remove(chess)

def eat(rect1,rect2): 
    for a,b in [(rect1,rect2),(rect2,rect1)]:
        if ((isPointInsideRect(a.left, a.top, b)) or
            (isPointInsideRect(a.left, a.bottom, b)) or
            (isPointInsideRect(a.right, a.top, b)) or
            (isPointInsideRect(a.right, a.bottom, b))):
            return True
    return False
def draw_where_can_chess_move(x,y,chess):
    if chees==black_king:
        if x=1 and y=1:
            for m,n in range((x,y),(x+1,y+1),1):
                plase = pygame.Rect(x*60-30, y*60+30, CELLSIZE, CELLSIZE)
                pygame.draw.rect(DISPLAYSURF, BLUE, plase)
        if x=1
            for m,n in range((x-1,y-1),(x+1,y+1),1)
                plase = pygame.Rect(x*60-30, y*60+30, CELLSIZE, CELLSIZE)
                pygame.draw.rect(DISPLAYSURF, BLUE, plase)
def isPointInsideRect(x, y, rect):
    if (x > rect.left) and (x < rect.right) and (y > rect.top) and (y < rect.bottom):
        return True
    else:
        return False  
    
def drawGrid():
    
    for x in range(20, Chessboardwidth+20, CELLSIZE): # draw vertical lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 20), (x, Chessboardheight+20))
       
    for y in range(20, Chessboardheight+20, CELLSIZE): # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (20, y), (Chessboardwidth+20, y))
 
# When game is over        
def game_over():
    if white_king():
       
       return 'Black'
    if black_king():
        
       return 'White'
    
def showGameOverScreen():
    gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
    gameSurf = gameOverFont.render('(%s)', True, WHITE) % (game_over())
    overSurf = gameOverFont.render('Win', True, WHITE)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (WINDOWWIDTH / 2, 10)
    overRect.midtop = (WINDOWWIDTH / 2, gameRect.height + 10 + 25)

    DISPLAYSURF.blit(gameSurf, gameRect)
    DISPLAYSURF.blit(overSurf, overRect)
    drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress() # clear out any key presses in the event queue

    while True:
        if checkForKeyPress():
            pygame.event.get() # clear event queue
if __name__ == '__main__':
    main()