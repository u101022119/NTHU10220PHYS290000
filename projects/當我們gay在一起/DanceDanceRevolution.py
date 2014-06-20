#Computation for Physics, 2014 spring
'''
Project Name :  Dance Dance Revolution
Group        :  We Are Gays
Members      :  101022126, 101022218, 101022129, 101022171, 101022217
Last Modified:  2014/06/10
'''
import sys, pygame, random
from pygame.locals import *

#set up window
FPS = 70
WINDOWWIDTH = 640
WINDOWHEIGHT = 500


# set up basic colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


def main():
    global clk, screen, basicFont

    pygame.font.init()
    basicFont = pygame.font.SysFont(None, 36)

    pygame.init()
    SCORE = 0
    clk = pygame.time.Clock()

    screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Dance Dance Revolution')

    while True:
        runGame()

  
def runGame():
    #initial y-axis of falling arrorws 
    left_y   = 0
    up_y     = 0
    down_y   = -100
    right_y  = -150


    #initial parameter of the game
    steps = 2           #concerning the speed of falling arrows
    delife = 15         #decrease lives if one miss/mis-key down the arrows
    ScoreAdd = 100      #basic score increment
    SCORE = 0           #of course 0.0 at the begining
    LIFE = WINDOWWIDTH  #length of life bar is consistent with the windowwidth
    
    while True: # main game loop

        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                
                #arrow_left score judgemanet
                if event.key == K_LEFT:
                    if  390< left_y <410:
                        LIFE += delife
                        SCORE += ScoreAdd
                        left_y = 0
                        
                    if (410< left_y <430) or (370< left_y <390):
                        LIFE += delife
                        SCORE += ScoreAdd*1.6
                        left_y = 0
                        
                    if left_y< 370 or left_y >430:
                        LIFE -=delife
    
                        
                if event.key == K_UP:
                    if  390< up_y <410:
                        LIFE += delife
                        SCORE += ScoreAdd
                        up_y = -50
                        
                    if (410< up_y <430) or (370< up_y <390):
                        LIFE += delife
                        SCORE += ScoreAdd*1.6
                        up_y = -50
                        
                    if up_y<370 or up_y>430:
                        LIFE -=delife
                        
                #arrow_down score judgemanet
                if event.key == K_DOWN:
                    if  390< down_y <410:
                        LIFE += delife
                        SCORE += ScoreAdd
                        down_y = -30
                        
                    if (410< down_y <430) or (370< down_y <390):
                        LIFE += delife
                        SCORE += ScoreAdd*1.6
                        down_y = -30
                        
                    if down_y<370 or down_y>430:
                        LIFE -=delife

                #arrow_right score judgemanet
                if event.key == K_RIGHT:
                    if  390< right_y <410:
                        LIFE += delife
                        SCORE += ScoreAdd
                        right_y = -10
                        
                    if (410< right_y <430) or (370< right_y <390):
                        LIFE += delife
                        SCORE += ScoreAdd*1.6
                        right_y = -10
                        
                    if down_y<370 or down_y>430:
                        LIFE -=delife
                        

        #adjustment of game parameters for advance level

            
        if SCORE <1000:      #do not use 'operator=', reminding these expressions
            steps = 3        #           are in an infinite loop.

        if SCORE >1000:
            steps = 4
            ScoreAdd = 130
            delife = 20
            
        if SCORE>2500:
            steps = 5
            ScoreAdd = 170
            delife = 23
            
        if SCORE>3500:
            steps = 6
            ScoreAdd = 200
            delife = 27
            

        screen.fill(BLACK)
        drawArrowEmpty()
        
        #left arrorw missed            
        ArrowFalling_LEFT(40,left_y)
        left_y+=steps
        if left_y >=WINDOWHEIGHT+50:
            left_y = 0
            LIFE -=delife
            
        #up arrorw missed  
        ArrowFalling_UP(40,up_y)
        up_y+=steps
        if up_y >=WINDOWHEIGHT+50:
            up_y = -50
            LIFE -=delife
            
        #down arrorw missed  
        ArrowFalling_DOWN(40,down_y)
        down_y+=steps
        if down_y >=WINDOWHEIGHT+50:
            down_y = -20
            LIFE -=delife

            
        #right arrorw missed  
        ArrowFalling_RIGHT(40,right_y)
        right_y+=steps
        if right_y >=WINDOWHEIGHT+50:
            right_y = -10
            LIFE -=delife

        drawLifeBar(LIFE)  
        drawScore(SCORE)            

        #gameover
        if LIFE <=0:
            showGameOver(SCORE)
            pygame.display.update()
            pygame.time.wait(3000) #restart in 3 sceonds
            return
        
        clk.tick(FPS)
        pygame.display.update()



def terminate():
    pygame.quit()
    SystemExit()


def ArrowFalling_LEFT(x,y):
    #set arrow variables
    BORDER = 4
    COLOR =  (255, 255, 255)
 
    for i in range(0,50):
        arrowRect = pygame.Rect(x+i, y+i, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)
    for i in range(0,50):
        arrowRect = pygame.Rect(x+i, y-i, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)
    for i in range(0,30):
        arrowRect = pygame.Rect(x+50, y-50+i, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)
    for i in range(0,50):
        arrowRect = pygame.Rect(x+50+i, y-20, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)
    for i in range(0,30):
        arrowRect = pygame.Rect(x+50, y+50-i, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)
    for i in range(0,50):
        arrowRect = pygame.Rect(x+50+i, y+20, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)
    for i in range(0,40):
        arrowRect = pygame.Rect(x+100, y+20-i, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)  


def ArrowFalling_UP(x, y):
    #set arrow variables
    BORDER = 4
    COLOR =  (255, 255, 255)
    
    for i in range(0,50):
        arrowRect = pygame.Rect(x+200-i, y-50+i, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)

    for i in range(0,50):
        arrowRect = pygame.Rect(x+200+i, y-50+i, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)
     
    for i in range(0,30):
        arrowRect = pygame.Rect(x+200-50+i, y, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)

    for i in range(0,30):
        arrowRect = pygame.Rect(x+200+50-i, y, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)

    for i in range(0,50):
        arrowRect = pygame.Rect(x+200+50-30, y+i, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)

    for i in range(0,50):
        arrowRect = pygame.Rect(x+200-50+30, y+i, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)

    for i in range(0,40):
        arrowRect = pygame.Rect(x+200-50+30+i, y+50, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)


def ArrowFalling_DOWN(x,y):
    #set arrow variables
    BORDER = 4
    COLOR =  (255, 255, 255)
      
    for i in range(0,40):
        arrowRect = pygame.Rect(x+200-50+200-20+i, y-50, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)

    for i in range(0,50):
        arrowRect = pygame.Rect(x+200-50+200-20, y-50+i, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)
     
    for i in range(0,50):
        arrowRect = pygame.Rect(x+200-50+200-20+40, y-50+i, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)

    for i in range(0,30):
        arrowRect = pygame.Rect(x+200-50+200-20+40+i, y-50+50, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)

    for i in range(0,30):
        arrowRect = pygame.Rect(x+200-50+200-20-i, y-50+50, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)

    for i in range(0,50):
        arrowRect = pygame.Rect(x+200-50+200-20-30+i, y-50+50+i, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)
        
    for i in range(0,50):
        arrowRect = pygame.Rect(x+200-50+200-20+40+30-i, y-50+50+i, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)

def ArrowFalling_RIGHT(x,y):
    #set arrow variables
    BORDER = 4
    COLOR =  (255, 255, 255)

    for i in range(0,40):
        arrowRect = pygame.Rect(x+200-50+200-20+40+30+50, y-50+30+i, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)
        
    for i in range(0,50):
        arrowRect = pygame.Rect(x+200-50+200-20+40+30+50+i, y-50+30, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)
        
    for i in range(0,50):
        arrowRect = pygame.Rect(x+200-50+200-20+40+30+50+i, y-50+30+40, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)  

    for i in range(0,30):
        arrowRect = pygame.Rect(x+200-50+200-20+40+30+60+40, y-50+30-i, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)  

    for i in range(0,30):
        arrowRect = pygame.Rect(x+200-50+200-20+40+30+60+40, y-50+30+40+i, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)  

    for i in range(0,50):
        arrowRect = pygame.Rect(x+200-50+200-20+40+30+60+40+i, y-50+30+40+30-i, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)

    for i in range(0,50):
        arrowRect = pygame.Rect(x+200-50+200-20+40+30+60+40+i, y-50+30-30+i, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)
        
def drawArrowEmpty():
    #set arrow variables
    x = 40
    y = 400
    BORDER = 4
    COLOR =  (122, 122, 122)
    
    #create arrow left   
    for i in range(0,50):
        arrowRect = pygame.Rect(x+i, y+i, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)
    for i in range(0,50):
        arrowRect = pygame.Rect(x+i, y-i, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)
    for i in range(0,30):
        arrowRect = pygame.Rect(x+50, y-50+i, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)
    for i in range(0,50):
        arrowRect = pygame.Rect(x+50+i, y-20, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)
    for i in range(0,30):
        arrowRect = pygame.Rect(x+50, y+50-i, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)
    for i in range(0,50):
        arrowRect = pygame.Rect(x+50+i, y+20, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)
    for i in range(0,40):
        arrowRect = pygame.Rect(x+100, y+20-i, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)

    #create arrow up
    for i in range(0,50):
        arrowRect = pygame.Rect(x+200-i, y-50+i, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)

    for i in range(0,50):
        arrowRect = pygame.Rect(x+200+i, y-50+i, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)
     
    for i in range(0,30):
        arrowRect = pygame.Rect(x+200-50+i, y, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)

    for i in range(0,30):
        arrowRect = pygame.Rect(x+200+50-i, y, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)

    for i in range(0,50):
        arrowRect = pygame.Rect(x+200+50-30, y+i, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)

    for i in range(0,50):
        arrowRect = pygame.Rect(x+200-50+30, y+i, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)

    for i in range(0,40):
        arrowRect = pygame.Rect(x+200-50+30+i, y+50, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)

    #create arrow down
    for i in range(0,40):
        arrowRect = pygame.Rect(x+200-50+200-20+i, y-50, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)

    for i in range(0,50):
        arrowRect = pygame.Rect(x+200-50+200-20, y-50+i, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)
     
    for i in range(0,50):
        arrowRect = pygame.Rect(x+200-50+200-20+40, y-50+i, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)

    for i in range(0,30):
        arrowRect = pygame.Rect(x+200-50+200-20+40+i, y-50+50, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)

    for i in range(0,30):
        arrowRect = pygame.Rect(x+200-50+200-20-i, y-50+50, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)

    for i in range(0,50):
        arrowRect = pygame.Rect(x+200-50+200-20-30+i, y-50+50+i, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)
        
    for i in range(0,50):
        arrowRect = pygame.Rect(x+200-50+200-20+40+30-i, y-50+50+i, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)

    #create arrow right
    for i in range(0,40):
        arrowRect = pygame.Rect(x+200-50+200-20+40+30+50, y-50+30+i, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)
        
    for i in range(0,50):
        arrowRect = pygame.Rect(x+200-50+200-20+40+30+50+i, y-50+30, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)
        
    for i in range(0,50):
        arrowRect = pygame.Rect(x+200-50+200-20+40+30+50+i, y-50+30+40, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)  

    for i in range(0,30):
        arrowRect = pygame.Rect(x+200-50+200-20+40+30+60+40, y-50+30-i, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)  

    for i in range(0,30):
        arrowRect = pygame.Rect(x+200-50+200-20+40+30+60+40, y-50+30+40+i, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)  

    for i in range(0,50):
        arrowRect = pygame.Rect(x+200-50+200-20+40+30+60+40+i, y-50+30+40+30-i, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)

    for i in range(0,50):
        arrowRect = pygame.Rect(x+200-50+200-20+40+30+60+40+i, y-50+30-30+i, BORDER, BORDER)
        pygame.draw.rect(screen, COLOR, arrowRect)  



def drawLifeBar(LIFE):   
    size = 45   #width
    if LIFE >= WINDOWWIDTH/2:
        COLOR =  (255,215,0)
    elif WINDOWWIDTH/4 <= LIFE < WINDOWWIDTH/2:     
        COLOR =  (255,127,0)
    elif LIFE< WINDOWWIDTH/4:
        COLOR =  RED

    lifeRect = pygame.Rect(0, 0, LIFE, size)
    pygame.draw.rect(screen, COLOR, lifeRect)

def drawScore(score):
    scoreSurf = basicFont.render('Score: %s' % (int(score)), True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (10, 10)
    screen.blit(scoreSurf, scoreRect)

def showGameOver(score):
    if score <3000:
        #comments
        gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
        gameSurf = gameOverFont.render('Sucks', True, WHITE)
        gameRect = gameSurf.get_rect()
        gameRect.midtop = (WINDOWWIDTH / 2, 180)             #position

        #background of comments
        bgRect = pygame.Rect(0, gameRect.height + 10 , WINDOWWIDTH, 180)
        pygame.draw.rect(screen, (178,34,34), bgRect)

        #background of score
        bg2Rect = pygame.Rect(0, 325, WINDOWWIDTH, 50)  #position
        pygame.draw.rect(screen, (139,35,35), bg2Rect)  #color

        #score
        scoreSurf = basicFont.render('You got %s points !' % (int(score)), True, WHITE)
        scoreRect = scoreSurf.get_rect()
        scoreRect.center = (WINDOWWIDTH / 2, 350)   #position

        screen.blit(scoreSurf, scoreRect)
        screen.blit(gameSurf, gameRect)



    if 3000<= score <8000:
        gameOverFont = pygame.font.Font('freesansbold.ttf', 100)
        gameSurf = gameOverFont.render('Not Bad.', True, WHITE)
        gameRect = gameSurf.get_rect()
        gameRect.midtop = (WINDOWWIDTH / 2, 200)

        bgRect = pygame.Rect(0, gameRect.height + 10 + 25, WINDOWWIDTH, 200)
        pygame.draw.rect(screen, (24,116,139), bgRect)

        bg2Rect = pygame.Rect(0, 325, WINDOWWIDTH, 50)
        pygame.draw.rect(screen, (16,78,139), bg2Rect)
        
        scoreSurf = basicFont.render('You got %s points !' % (int(score)), True, WHITE)
        scoreRect = scoreSurf.get_rect()
        scoreRect.center = (WINDOWWIDTH / 2, 350)

        screen.blit(scoreSurf, scoreRect)
        screen.blit(gameSurf, gameRect)


    if 8000 <= score < 10000:
        gameOverFont = pygame.font.Font('freesansbold.ttf', 100)
        gameSurf = gameOverFont.render('Applause!', True, (139,119,101))
        gameRect = gameSurf.get_rect()
        gameRect.midtop = (WINDOWWIDTH / 2, 200)

        bgRect = pygame.Rect(0, gameRect.height + 10 + 25, WINDOWWIDTH, 200)
        pygame.draw.rect(screen, (238,223,204), bgRect)

        bg2Rect = pygame.Rect(0, 325, WINDOWWIDTH, 50)
        pygame.draw.rect(screen, (205,192,176), bg2Rect)
        
        scoreSurf = basicFont.render('You got %s points !' % (int(score)), True, (139,119,101))
        scoreRect = scoreSurf.get_rect()
        scoreRect.center = (WINDOWWIDTH / 2, 350)

        screen.blit(scoreSurf, scoreRect)
        screen.blit(gameSurf, gameRect)


    if 10000 <= score :
        gameOverFont = pygame.font.Font('freesansbold.ttf', 100)
        gameSurf = gameOverFont.render('Awesome!', True, WHITE)
        gameRect = gameSurf.get_rect()
        gameRect.midtop = (WINDOWWIDTH / 2, 200)

        bgRect = pygame.Rect(0, gameRect.height + 10 + 25, WINDOWWIDTH, 200)
        pygame.draw.rect(screen, (191,62,255), bgRect)

        bg2Rect = pygame.Rect(0, 325, WINDOWWIDTH, 50)
        pygame.draw.rect(screen, (154,50,205), bg2Rect)
        
        scoreSurf = basicFont.render('You got %s points !' % (int(score)), True, WHITE)
        scoreRect = scoreSurf.get_rect()
        scoreRect.center = (WINDOWWIDTH / 2, 350)

        screen.blit(scoreSurf, scoreRect)
        screen.blit(gameSurf, gameRect)

if __name__ == '__main__':
    main()
