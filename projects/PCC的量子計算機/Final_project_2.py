import pygame, sys, random
import time
import random
from pygame.locals import *

def doRectsOverlap(rect1, rect2):
    for a, b in [(rect1, rect2), (rect2, rect1)]:
        # Check if a's corners are inside b
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

def drawScore(score):
    scoreSurf = BasicFont.render('Score: %s' % (score), True, BLACK)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 140, 10)
    windowSurface.blit(scoreSurf, scoreRect)

def drawlife(life):
    lifeSurf = BasicFont.render('Life: %s' % (life), True, BLACK)
    lifeRect = lifeSurf.get_rect()
    lifeRect.topleft = (WINDOWWIDTH - 270, 10)
    windowSurface.blit(lifeSurf, lifeRect)

def drawsupporttime(supporttime):
    supporttimeSurf = BasicFont.render('powertime: %s' % (supporttime), True, BLACK)
    supporttimeRect = supporttimeSurf.get_rect()
    supporttimeRect.topleft = (WINDOWWIDTH - 470, 10)
    windowSurface.blit(supporttimeSurf, supporttimeRect)

def drawsupportnumber(supportnumber):
    supportnumberSurf = BasicFont.render('supportnumber: %s' % (supportnumber), True, BLACK)
    supportnumberRect = supportnumberSurf.get_rect()
    supportnumberRect.topleft = (WINDOWWIDTH - 680, 10)
    windowSurface.blit(supportnumberSurf, supportnumberRect)
    
def DrawText(text, font, surface, x, y):  
    text_obj = font.render(text, 1,WHITE)  
    text_rect = text_obj.get_rect()  
    text_rect.topleft = (x, y)  
    surface.blit(text_obj, text_rect)

def Terminate():  
    pygame.quit()  
    sys.exit() 

def WaitForPlayerToPressKey():  
    while True:  
        for event in pygame.event.get():  
            if event.type == QUIT:  
                Terminate()  
            if event.type == KEYDOWN:  
                if event.key == K_ESCAPE:  
                    Terminate()  
                return  
# set up pygame
pygame.init()
mainClock = pygame.time.Clock()


basicFont = pygame.font.SysFont(None, 96)
BasicFont = pygame.font.SysFont(None, 32)
game_start_font = pygame.font.SysFont(None, 48)  
game_over_font  = pygame.font.SysFont(None, 48)  

# set up the window
WINDOWWIDTH = 800
WINDOWHEIGHT = 650
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('dodge')

# set up the colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# set up the player and food data structure
foodCounter = 0
supportcounter = 0
NEWFOOD = 50
newsupport = 800
FOODSIZE = 20
supportsize = 20
playersize = 30
player = pygame.Rect(WINDOWWIDTH/2, WINDOWHEIGHT/2, playersize, playersize)
times = 0
support = []
clock = pygame.time.Clock()
time_passed = clock.tick(30)  
time_passed_seconds = time_passed / 1000.
score = 0
life = 5
supporttime = 10
wait = 0.0

DrawText('dodge', game_start_font, windowSurface,   
         (WINDOWWIDTH/3+60), (WINDOWHEIGHT/3 + 50))  
DrawText('Press any key to start.', game_start_font, windowSurface,   
         (WINDOWWIDTH/3)-60, (WINDOWHEIGHT)/3+100)  
pygame.display.update()  
WaitForPlayerToPressKey()


DOWNLEFT = 1
DOWNRIGHT = 3
UPLEFT = 7
UPRIGHT = 9

AA = []
aa = []

for i in range(10):
    WAY = random.randint(1,4)
    if WAY == 1:
        WAY = DOWNLEFT
    elif WAY ==2:
        WAY = DOWNRIGHT
    elif WAY == 3:
        WAY = UPLEFT
    elif WAY == 4:
        WAY = UPRIGHT
    a = {'rect':pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE), 'dir':WAY}    
    AA.append(a)
    aa.append(a['rect'])
    
    

for i in range(5):
    support.append(pygame.Rect(random.randint(0, WINDOWWIDTH - supportsize), random.randint(0, WINDOWHEIGHT - supportsize), supportsize, supportsize))
    
# set up movement variables
moveLeft = False
moveRight = False
moveUp = False
moveDown = False
XXX = False
YY = 3
ZZZ = False
CCC = False
running = True
deadtime = 0.0

MOVESPEED = 6
movespeed = 6


# run the game loop
while running == True:
   
    # check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    
        if event.type == KEYDOWN:
            # change the keyboard variables
            if event.key == K_LEFT or event.key == ord('a'):
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == ord('d'):
                moveLeft = False
                moveRight = True
            if event.key == K_UP or event.key == ord('w'):
                moveDown = False
                moveUp = True
            if event.key == K_DOWN or event.key == ord('s'):
                moveUp = False
                moveDown = True
            if event.key == ord('x'):
                if CCC == True:
                    YY = YY
                else:
                    YY = YY-1
                    if YY > -1:
                        XXX = True
                        MOVESPEED = 12   
                    else:
                        YY = 0
                        supporttime = 10
                        XXX = False
            if event.key == ord('c'):
                if XXX == True:
                    YY = YY
                else:
                    YY = YY-1
                    if YY > -1:
                        CCC = True
                        movespeed = 3
                    else:
                        YY = 0
                        supporttime = 10
                        CCC = False
            
    
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == ord('a'):
                moveLeft = False
            if event.key == K_RIGHT or event.key == ord('d'):
                moveRight = False
            if event.key == K_UP or event.key == ord('w'):
                moveUp = False
            if event.key == K_DOWN or event.key == ord('s'):
                moveDown = False 
    
    if XXX == True:
        wait += time_passed_seconds
        supporttime = supporttime - time_passed_seconds
        if wait > 10:
            XXX = False
            MOVESPEED = 6
            supporttime = 10
            wait = 0.0
            
    if CCC == True:
        wait += time_passed_seconds
        supporttime =supporttime  - time_passed_seconds
        if wait > 10:
            CCC = False
            movespeed = 6
            supporttime = 10
            wait = 0.0
            
    if score>-10000:  
        score += 1
        if XXX ==True:
            score += 1


    foodCounter += 1
    if foodCounter >= NEWFOOD:
        # add new food
        foodCounter = 0
        FOODSIZE = 20
        WAY = random.randint(1,4)
        if WAY == 1:
            WAY = DOWNLEFT
        elif WAY ==2:
            WAY = DOWNRIGHT
        elif WAY == 3:
            WAY = UPLEFT
        elif WAY == 4:
            WAY = UPRIGHT
        b = {'rect':pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE), 'dir':WAY}
        AA.append(b)
        aa.append(b['rect'])        
    
    
    
    supportcounter += 1
    if supportcounter >= newsupport:
        # add new support
        supportcounter = 0
        support.append(pygame.Rect(random.randint(0, WINDOWWIDTH - supportsize), random.randint(0, WINDOWHEIGHT - supportsize), supportsize, supportsize))
    # draw the black background onto the surface
    windowSurface.fill(WHITE)

    # move the player
    if moveDown and player.bottom < WINDOWHEIGHT:
        player.top += MOVESPEED
    if moveUp and player.top > 0:
        player.top -= MOVESPEED
    if moveLeft and player.left > 0:
        player.left -= MOVESPEED
    if moveRight and player.right < WINDOWWIDTH:
        player.right += MOVESPEED
    if XXX is True:
       for food in aa[:]:
           if doRectsOverlap(player, food):
            aa.remove(food)

    

    # draw the player onto the surface
    pygame.draw.rect(windowSurface, RED, player)

                
    if ZZZ == True:
        text = basicFont.render('You are infected !! ', True, WHITE, BLUE)
        textRect = text.get_rect()
        textRect.centerx = windowSurface.get_rect().centerx
        textRect.centery = windowSurface.get_rect().centery
        windowSurface.blit(text, textRect)
        running = False

            
    for XX in support[:]:
        if doRectsOverlap(player, XX):
            support.remove(XX)
            YY = YY+1
            print YY
            
    # check if the player has intersected with any food squares.
    for food in aa[:]:
        if player.colliderect(food):
            aa.remove(food)
            life =  life - 1
            if life < 1:
                ZZZ = True
                deadtime = 0.0

    # draw the food
    for i in range(len(aa)):
        pygame.draw.rect(windowSurface, GREEN, aa[i])
    for i in range(len(support)):
        pygame.draw.rect(windowSurface, BLUE, support[i])
    
    supportnumber = YY
    drawScore(score)
    drawlife(life)
    drawsupporttime(supporttime)
    drawsupportnumber(supportnumber)
    
    for c in AA:
        # move the block data structure
        if c['dir'] == DOWNLEFT:
            c['rect'].left -= movespeed
            c['rect'].top += movespeed
        if c['dir'] == DOWNRIGHT:
            c['rect'].left += movespeed
            c['rect'].top += movespeed
        if c['dir'] == UPLEFT:
            c['rect'].left -= movespeed
            c['rect'].top -= movespeed
        if c['dir'] == UPRIGHT:
            c['rect'].left += movespeed
            c['rect'].top -= movespeed

        # check if the block has move out of the window
        if c['rect'].top < 0:
            # block has moved past the top
            if c['dir'] == UPLEFT:
                c['dir'] = DOWNLEFT
            if c['dir'] == UPRIGHT:
                c['dir'] = DOWNRIGHT
        if c['rect'].bottom > WINDOWHEIGHT:
            # block has moved past the bottom
            if c['dir'] == DOWNLEFT:
                c['dir'] = UPLEFT
            if c['dir'] == DOWNRIGHT:
                c['dir'] = UPRIGHT
        if c['rect'].left < 0:
            # block has moved past the left side
            if c['dir'] == DOWNLEFT:
                c['dir'] = DOWNRIGHT
            if c['dir'] == UPLEFT:
                c['dir'] = UPRIGHT
        if c['rect'].right > WINDOWWIDTH:
            # block has moved past the right side
            if c['dir'] == DOWNRIGHT:
                c['dir'] = DOWNLEFT
            if c['dir'] == UPRIGHT:
                c['dir'] = UPLEFT


    # draw the window onto the screen
    pygame.display.update()
    mainClock.tick(40)
