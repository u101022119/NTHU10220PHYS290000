import pygame, sys, random
from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()

TEXTCOLOR = (255, 255, 255)
font = pygame.font.SysFont(None, 48)

def terminate():
    pygame.quit()
    sys.exit()

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # pressing escape quits
                    terminate()
                return


WINDOWWIDTH = 1000
WINDOWHEIGHT = 600
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('block')

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

drawText('Block', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
drawText('Press a key to start.', font, windowSurface, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3) + 50)
pygame.display.update()
waitForPlayerToPressKey()


while True:
    MOVESPEED = 4
    ballmovespeed = 2
    ballspeed=0

    playerleft = 450
    playertop = 570
    
    ballleft = 470
    balltop = 540

    player = pygame.Rect(playerleft, playertop, 100, 30)

    ball = pygame.Rect(ballleft,balltop,30,30)
    
    ballup = True
    ballright = True

    moveLeft = False
    moveRight = False

    blocks=[]
    for i in range(30):
        if i <10:
            blocks.append(pygame.Rect((i)*100,90,100,30))
        elif i >=10 and i<20:
            blocks.append(pygame.Rect((i-10)*100,120,100,30))
        else :
            blocks.append(pygame.Rect((i-20)*100,150,100,30))

    while True:
        windowSurface.fill(BLACK)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit() 
            if event.type == KEYDOWN:
                if event.key == K_LEFT :
                    moveLeft = True
                    moveRight = False
                if event.key == K_RIGHT :
                    moveRight = True
                    moveLeft = False
               
                                                     
                
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_RIGHT :
                    moveRight = False
                if event.key == K_LEFT :               
                    moveLeft = False
              
        if moveLeft and player.left > 0:
            player.left -=  MOVESPEED        
        if moveRight and player.right < WINDOWWIDTH:
            player.right += MOVESPEED
    
            
        
        for block in blocks[:]:
            if ball.colliderect(block):
                if ball.right >= block.left and ballright == True and ball.top+3 <= block.bottom and ball.bottom-3 >= block.top:
                    ballright = False
                elif ball.left <= block.right and ballright == False and ball.top+3 <= block.bottom and ball.bottom-3 >= block.top:
                    ballright = True
                if ball.top <= block.bottom  and ballup == True and ball.right-3 >= block.left and ball.left+3 <= block.right :
                    ballup = False
                elif ball.bottom >= block.top and ballup == False and ball.right-3 >= block.left and ball.left+3 <= block.right :
                    ballup = True
                break
            

        if player.colliderect(ball):
            if moveRight == True:
                ballright = True
            elif moveLeft == True:
                ballright = False
            ballup = True
            ballspeed = 1+0.1*random.randint(0 ,10)

    
        for block in blocks[:]:
            if ball.colliderect(block):
                blocks.remove(block)

               
        if ball.top <= 0:
            ballup = False

        if ball.left <= 0 :
            ballright = True
        
        if ball.right >= WINDOWWIDTH:
            ballright = False

            
        for i in range(len(blocks)):
            pygame.draw.rect(windowSurface, GREEN, blocks[i])

        if ballup==True:
            ball.top -= ballmovespeed
        if ballup==False:
            ball.top+= ballmovespeed
        if ballright==True:
            ball.left +=ballspeed
        if ballright==False:
            ball.left -=ballspeed

        pygame.draw.rect(windowSurface, WHITE, player)
        pygame.draw.rect(windowSurface, RED, ball)
        pygame.display.update()
        if len(blocks) == 0:
            break

        if ball.bottom > WINDOWHEIGHT :
            ballspeed=0
            ballmovespeed=0
            break
    
        mainClock.tick(150)
    if len(blocks) == 0:
        drawText('YOU WIN', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
        drawText('Press a key to play again.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
        pygame.display.update()
        waitForPlayerToPressKey()
    else :
        drawText('GAME OVER', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
        drawText('Press a key to play again.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
        pygame.display.update()
        waitForPlayerToPressKey()
