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
#  white    
def white_king():  
    
def white_queen():
    
def white_bishop1():
    
def white_bishop2():
    
def white_rock1():
    
def white_rock2():
    
def white_kinght1():

def white_kinght2():

def white_soldier1():

def white_soldier2():

def white_soldier3():

def white_soldier4():

def white_soldier5():

def white_soldier6():

def white_soldier7():

def white_soldier8():
# black

def black_king():

def black_queen():

def black_bishop1():

def black_bishop2():

def black_rock1():

def black_rock2():

def black_kinght1():

def black_kinght2():

def black_soldier1():

def black_soldier2():

def black_soldier3():

def black_soldier4():

def black_soldier5():

def black_soldier6():

def black_soldier7():

def black_soldier8():

# Game's main point    
def runGame():
    
    
    
def eat(): 
    
def walk(pieces):
    
def drawGrid():
    n=0
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