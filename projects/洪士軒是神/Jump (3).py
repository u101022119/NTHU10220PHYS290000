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
pygame.display.set_caption('jump')

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

score = 0

drawText('Jump', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
drawText('Press a key to start.', font, windowSurface, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3) + 50)
pygame.display.update()
waitForPlayerToPressKey()


while True:
    
    MOVESPEED = 0
    ballmovespeed = 5   
    g = 0
    b = 0
    c = 0
    ballleft = 470
    balltop = 540
    win = True
    ball = pygame.Rect(ballleft,balltop,30,30)
    
    ballup = True
    
    moveLeft = False
    moveRight = False
    collidetime = [0, 0, 0, 0]
    fallrock = []
    rocktime = []
    for i in range(3):
        fallrock.append(pygame.Rect(30*random.randint(0,33),0,30,30))
        rocktime.append(100*random.randint(1, 3))
    blocks = []
    blocks.append(pygame.Rect(450,450,100,30))
    for i in range(3):
        blocks.append(pygame.Rect(100*random.randint(0 ,9),150*(2-i),100,30))

    blockspeed = []
    blockspeed.append(0)
    for i in range(3):
        blockspeed.append(random.randint(0,1))

    TF = [True ,False]
    blockspeedright = []
    for i in range(4):
        blockspeedright.append(random.choice(TF))
              
    while True:
        windowSurface.fill(BLACK)
        drawText('score: %s'%(score), font, windowSurface, 0, 0)
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
                if event.key == ord('x'):
                    score += 10000
                if event.key == ord('z'):
                    score -= 10000   
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_RIGHT :                    
                    moveRight = False
                if event.key == K_LEFT :                    
                    moveLeft = False
                    
        ball.left -=  MOVESPEED
        
        if moveLeft :
            if MOVESPEED <=6:
                MOVESPEED += 0.2
                
        if ball.right < 0:
            ball.left = WINDOWWIDTH-30
            
        if moveRight :            
            if MOVESPEED >= -6:
                MOVESPEED -= 0.2
                
        if ball.left > WINDOWWIDTH:
            ball.left = 0

        if moveLeft == False and moveRight == False :
            if MOVESPEED >= 0.4 :
                MOVESPEED -= 0.2
            elif MOVESPEED <= -0.4 :
                MOVESPEED += 0.2
            elif MOVESPEED < 0.4 and -0.4 < MOVESPEED :
                MOVESPEED = 0
            
        if score > 30000:            
            
            for i in range(3):
                if rocktime[i] > 0:
                    rocktime[i] -= 1
                if rocktime[i] == 0:
                    fallrock[i].top += 5
                
            for rock in fallrock[:]:                        
                if rock.top >= WINDOWHEIGHT:
                    rocktime[fallrock.index(rock)] += 100*random.randint(1, 3)
                    rock.top = 0
                    rock.left = 30*random.randint(0,33)                    
                if ball.colliderect(rock):
                    ballmovespeed = -10
                    win = False
                        
                    
            
    
        ballmovespeed -= 0.0625
           
        for block in blocks[:]:
            if block.left <= 0:
                blockspeedright[blocks.index(block)] = True
            if block.right >= WINDOWWIDTH:
                blockspeedright[blocks.index(block)] = False
                
            if blockspeedright[blocks.index(block)] == True and block.right <=WINDOWWIDTH :
                block.left += blockspeed[blocks.index(block)]
            if blockspeedright[blocks.index(block)] == False and block.left >=0 :
                block.left -= blockspeed[blocks.index(block)]
                
            if ball.colliderect(block) and ballmovespeed < 0 and win:
                ballmovespeed = 5
                if collidetime[blocks.index(block)] < 2:
                    collidetime[blocks.index(block)] += 1
                
        if ball.top <= 150:
            if ballmovespeed >= 2:
                score =score +ballmovespeed
            for block in blocks[:]:
                block.top += ballmovespeed
                if block.top >= WINDOWHEIGHT:
                    blocks.remove(block)
                    blockspeed.remove(blockspeed[0])
                    blockspeedright.remove(blockspeedright[0])
                    collidetime.remove(collidetime[0])
                    if score <= 5000:
                        blockspeed.append(random.randint(0,1))
                    elif score <= 10000 and score > 5000:
                        blockspeed.append(random.randint(0,4))
                    elif score > 10000:
                        blockspeed.append(random.randint(2,4))
                    blockspeedright.append(random.choice(TF))
                    blocks.append(pygame.Rect(100*random.randint(0 ,9),0,100,30))
                    collidetime.append(0)
                    
            ball.top = 150
            
        
        if score > 15000 and b < 200:
            b += 1
        if b == 200:
            b = 0
            
        for i in range(len(blocks)):
            if score < 10000:
                pygame.draw.rect(windowSurface, GREEN, blocks[i])
            elif score >= 10000 and score <= 20000:
                pygame.draw.rect(windowSurface, (0, 250-125*collidetime[i], 0), blocks[i])
            elif score > 20000 and b <= 150:                
                pygame.draw.rect(windowSurface, (0, 200-b, 0), blocks[i])
            elif score > 20000 and b < 200 and b > 150:                
                pygame.draw.rect(windowSurface, BLACK, blocks[i])
                
        if score > 30000:
            for i in range(len(fallrock)):
                pygame.draw.rect(windowSurface, YELLOW, fallrock[i])

        if ballup == True:
            ball.top -= ballmovespeed
        
        pygame.draw.rect(windowSurface, RED, ball)
        pygame.display.update()
        

        if ball.bottom > WINDOWHEIGHT :
            ballmovespeed=0
            score = 0
            break
    
        mainClock.tick(100)
        
    drawText('GAME OVER', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
    drawText('Press a key to play again.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
    pygame.display.update()
    waitForPlayerToPressKey()
