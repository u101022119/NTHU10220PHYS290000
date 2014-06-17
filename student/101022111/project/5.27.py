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

    while True:
        drawPressKeyMsg()

        if checkForKeyPress():
            pygame.event.get() # clear event queue
            return
        pygame.display.update()
        FPSCLOCK.tick(FPS)
def terminate():
    pygame.quit()
    sys.exit()

white_king = [{'x':290 ,'y': 50}] 
white_king.image=pygame.image.load('WKING.png')

    
white_queen = [{'x':230 ,'y': 50}] 
white_queen.image=pygame.image.load('WQUEEN.png')
white_queen.image.midtop=(230,50)

white_bishop1 = [{'x':170, 'y': 50}] 
white_bishop1.image=pygame.image.load('WBISHOP.png')
white_bishop1.image.midtop=(170,50)
   
    white_bishop2 = [{'x':350 ,'y': 50}] 
    white_bishop2.image=pygame.image.load('WBISHOP.png')
    white_bishop2.image.midtop=(350,50)
    
    white_rock1 = [{'x':50 ,'y': 50}] 
    white_rock1.image=pygame.image.load('WROCK.png')
    white_rock1.image.midtop=(50,50)
    
    white_rock2 = [{'x':470 ,'y': 50}] 
    white_rock2.image=pygame.image.load('WROCK.png')
    white_rock2.image.midtop=(470,50)
    
    white_kinght1 = [{'x':110 ,'y': 50}] 
    white_kinght1.image=pygame.image.load('WKNIGHT.png')
    white_kinght1.image.midtop=(110,50)
    
    white_kinght2 = [{'x':410 ,'y': 50}] 
    white_kinght2.image=pygame.image.load('WKNIGHT.png')
    white_kinght2.image.midtop=(410,50)
    
    white_soldier1 = [{'x':50 ,'y': 110}] 
    white_soldier1.image=pygame.image.load('WSOLDIER.png')
    white_soldier1.image.midtop=(50,110)
    
    white_soldier2 = [{'x':110, 'y': 110}] 
    white_soldier2.image=pygame.image.load('WSOLDIER.png')
    white_soldier2.image.midtop=(110,110)
    
    white_soldier3 = [{'x':170, 'y': 110}] 
    white_soldier3.image=pygame.image.load('WSOLDIER.png')
    white_soldier3.image.midtop=(170,110)
   
    white_soldier4 =[{'x':230, 'y': 110}] 
    white_soldier4.image=pygame.image.load('WSOLDIER.png')
    white_soldier4.image.midtop=(230,110)
    
    white_soldier5 = [{'x':290, 'y': 110}] 
    white_soldier5.image=pygame.image.load('WSOLDIER.png')
    white_soldier5.image.midtop=(290,110)    
    
    white_soldier6 = [{'x':350, 'y': 110}] 
    white_soldier6.image=pygame.image.load('WSOLDIER.png')
    white_soldier6.image.midtop=(350,110)
    
    white_soldier7 = [{'x':410, 'y': 110}] 
    white_soldier7.image=pygame.image.load('WSOLDIER.png')
    white_soldier7.image.midtop=(410,110)
    
    white_soldier8 = [{'x':470 ,'y': 110}] 
    white_soldier8.image=pygame.image.load('WSOLDIER.png')
    white_soldier8.image.midtop=(470,110)
    # black
      
    black_king = [{'x':290 ,'y': 470}]
    black_king.image=pygame.image.load('BKING.png')
    black_king.image.midtop=(290,470)
    
    black_queen = [{'x':230 ,'y': 470}]
    black_queen.image=pygame.image.load('BQUEEN.png')
    black_queen.image.midtop=(230,470)
       
    black_bishop1 = [{'x':170, 'y': 470}]
    black_bishop1.image=pygame.image.load('BBISHOP.png')
    black_bishop1.image.midtop=(170,470) 
    
    black_bishop2 = [{'x':350 ,'y': 470}]
    black_bishop2.image=pygame.image.load('BBISHOP.png')
    black_bishop2.image.midtop=(350,470)
    
    black_rock1 = [{'x':50 ,'y': 470}]
    black_rock1.image=pygame.image.load('BROCK.png')
    black_rock1.image.midtop=(50,470)
    
    black_rock2 = [{'x':470 ,'y': 470}]
    black_rock2.image=pygame.image.load('BROCK.png')
    black_rock2.image.midtop=(470,470)
   
    black_kinght1 = [{'x':110 ,'y': 470}]
    black_kinght1.image=pygame.image.load('BKNIGHT.png')
    black_kinght1.image.midtop=(110,470)
    
    black_kinght2 = [{'x':410 ,'y': 470}]
    black_kinght2.image=pygame.image.load('BKNIGHT.png')
    black_kinght2.image.midtop=(410,470)
    
    black_soldier1 = [{'x':50 ,'y': 410}]
    black_soldier1.image=pygame.image.load('BSOLDIER.png')
    black_soldier1.image.midtop=(50,410)
   
    black_soldier2 =  [{'x':110, 'y': 410}]
    black_soldier2.image=pygame.image.load('BSOLDIER.png')
    black_soldier2.image.midtop=(110,410)
    
    black_soldier3 = [{'x':170, 'y': 410}]
    black_soldier3.image=pygame.image.load('BSOLDIER.png')
    black_soldier3.image.midtop=(170,410)
    
    black_soldier4 =  [{'x':230, 'y': 410}]
    black_soldier4.image=pygame.image.load('BSOLDIER.png')
    black_soldier4.image.midtop=(230,410)
    
    black_soldier5 = [{'x':290 ,'y': 410}]
    black_soldier5.image=pygame.image.load('BSOLDIER.png')
    black_soldier5.image.midtop=(290,410)
   
    black_soldier6 = [{'x':350 ,'y': 410}]
    black_soldier6.image=pygame.image.load('BSOLDIER.png')
    black_soldier6.image.midtop=(350,410)
    
    black_soldier7 = [{'x':410, 'y': 410}]
    black_soldier7.image=pygame.image.load('BSOLDIER.png')
    black_soldier7.image.midtop=(410,410)
    
    black_soldier8 = [{'x':470 ,'y': 410}]
    black_soldier8.image=pygame.image.load('BSOLDIER.png')
    black_soldier8.image.midtop=(470,410)
# Game's main point    
def runGame():
    while True:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                for a,b in range(8):
                    if event.pos[0]>(60*a-30) and event.pos[1]>(60*b-30) and event.pos[0]<(60*a+30) and event.pos[1]<(60*b+30):
                        if chess ['x']>(60*a-30) and chess ['y']>(60*b-30) and chess ['x']<(60*a+30) and chess ['y']<(60*b+30):
                            return chess['x','y']
            if event.type == MOUSEBUTTONUP:
                for a,b in range(8):
                    if event.pos[0]>(60*a-30) and event.pos[1]>(60*b-30) and event.pos[0]<(60*a+30) and event.pos[1]<(60*b+30):
                        chess['x','y']=[60*a,60*b]
                        eat(chess['x'],chess['y'])
        
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