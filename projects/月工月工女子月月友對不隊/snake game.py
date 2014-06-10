import pygame, sys, random,time
from pygame.locals import *


pygame.init()
mainClock = pygame.time.Clock()

def title():
    pygame.mixer.music.load("begin music.mp3")
    pygame.mixer.music.play(-1, 0.0)
    pygame.init()
    
    color_list =[WHITE,BLUE,RED,YELLOW]
    x = WHITE
    #font1 = pygame.font.Font(None, 108)
    #font2 = pygame.font.Font(None, 36)

    background_image = pygame.image.load("snake picture.jpg")
    windowSurface.blit(background_image, [350,300])

   
        
    z = 0

    while True:        
        for event in pygame.event.get():                                  
            if event.type == QUIT:
                terminate()        

              
        text = font1.render("SNAKE GAME", True, x,ORANGE)
        windowSurface.blit(text, [240, 50])
        start_game = font2.render("PRESS A KEY TO START GAME", True, WHITE)
        windowSurface.blit(start_game, [300, 250])    
  
    
        TEMP_title_color = x
        while  random.choice(color_list) != TEMP_title_color:
            x=random.choice(color_list)   
        time.sleep(0.3)
               

        pygame.display.flip()
        mainClock.tick(20)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
                
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: 
                    terminate()   
                else:
                    z = z+1
        
        if z == 1:
            break

def final():
    pygame.init()
    windowSurface.fill(BLACK)

    DISPLAYSURF = windowSurface 


    pygame.draw.circle(DISPLAYSURF, BLUE, (210, 250), 40, 0)
    pygame.draw.circle(DISPLAYSURF, BLUE, (900, 500), 35, 0)
    pygame.draw.circle(DISPLAYSURF, BLUE, (400, 50), 30, 0)
    pygame.draw.circle(DISPLAYSURF, BLUE, (100, 220), 27, 0)
    pygame.draw.circle(DISPLAYSURF, BLUE, (800, 450), 33, 0)
    pygame.draw.circle(DISPLAYSURF, BLUE, (600, 130), 20, 0)
    pygame.draw.circle(DISPLAYSURF, BLUE, (700, 180), 26, 0)
    pygame.draw.circle(DISPLAYSURF, BLUE, (130, 480), 43, 0)

    pixObj = pygame.PixelArray(windowSurface)
    pixObj[380][280] = BLACK
    pixObj[382][282] = BLACK
    pixObj[384][284] = BLACK
    pixObj[386][286] = BLACK
    pixObj[388][288] = BLACK
    del pixObj

    drawText('HA HA', font3, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT*3 / 10))
    
    drawText('LOSER!', font3, windowSurface, (WINDOWWIDTH*1 / 2), (WINDOWHEIGHT*2 / 5))
                
    drawText('Continue??(Y/N)', font3, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT*2 / 3))
                          
                

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
                if event.key == K_ESCAPE:
                    terminate()
                return

def boundary():
    boundary = []
    boundary1 = []
    boundary2 = []
    pygame.init()
    

    d = 0

    for i in range(WINDOWWIDTH/20):
        boundary1.append(i*20)
        boundary2.append(0)
        d = d+1

    for i in range(WINDOWWIDTH/20):
        boundary1.append(i*20)
        boundary2.append(580)
        d = d+1

    for i in range(WINDOWHEIGHT/20-1):
        boundary1.append(0)
        boundary2.append((i+1)*20)
        d = d+1

    for i in range(WINDOWHEIGHT/20-1):
        boundary1.append(980)
        boundary2.append((i+1)*20)
        d = d+1

    for i in range(d):
        boundary.append(pygame.Rect(boundary1[i], boundary2[i], SNAKESIZE, SNAKESIZE))

    for i in range(d):
        pygame.draw.rect(windowSurface, RED, boundary[i]) 
 
font = pygame.font.SysFont(None, 48)
font1 = pygame.font.SysFont(None, 108)
font2 = pygame.font.SysFont(None, 36)
font3 = pygame.font.SysFont(None, 90)
WINDOWWIDTH = 1000
WINDOWHEIGHT = 600
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Snake')
font = pygame.font.SysFont(None, 48)
TEXTCOLOR = (255, 255, 255)

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
BLUE     = (   0,   0, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
YELLOW   = ( 255, 255,   0)
PURPLE   = ( 185,  70, 255)
ORANGE   = ( 255, 125,   0)

win = 35

title()
pygame.mixer.music.stop()

while True:
    
    pygame.mixer.music.load("snake music.mp3")
    pygame.mixer.music.play(-1, 10.0)
    snake = []
    snake1 = []
    snake2 = []
    SNAKESIZE = 20
    LENGTH = 5
    food = 0


    moveLeft = False
    moveRight = True
    moveUp = False
    moveDown = False

    for i in range(LENGTH):
        snake1.append(500-SNAKESIZE*i)
        snake2.append(300)

    for i in range(LENGTH):
        snake.append(pygame.Rect(snake1[i], snake2[i], SNAKESIZE, SNAKESIZE))

    a = 0

    while True:       
        windowSurface.fill(BLACK)
        boundary()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_LEFT or event.key == ord('a'):
                    if moveRight:
                        moveRight = True
                        moveLeft = False
                        moveUp = False
                        moveDown = False
                    else:
                        moveLeft = True
                        moveRight = False
                        moveUp = False
                        moveDown = False    
                if event.key == K_RIGHT or event.key == ord('d'):
                    if moveLeft:
                        moveRight = False
                        moveLeft = True
                        moveUp = False
                        moveDown = False
                    else:
                        moveLeft = False
                        moveRight = True
                        moveUp = False
                        moveDown = False                                      
                   
                if event.key == K_UP or event.key == ord('w'):
                    if moveDown:
                         moveDown = True
                         moveUp = False
                         moveLeft = False
                         moveRight = False
                    else:
                        moveUp = True
                        moveDown = False
                        moveLeft = False
                        moveRight = False       
                if event.key == K_DOWN or event.key == ord('s'):
                    if moveUp:
                         moveDown = False
                         moveUp = True
                         moveLeft = False
                         moveRight = False
                    else:
                        moveUp = False
                        moveDown = True
                        moveLeft = False
                        moveRight = False                                          
                    
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    terminate()
        if moveDown:
                for i in range(LENGTH):
                    snake[LENGTH-1-i] = snake[LENGTH-2-i]
                snake[0] = pygame.Rect(snake1[0], snake2[0]+SNAKESIZE, SNAKESIZE, SNAKESIZE)
                snake2[0] += SNAKESIZE
        if moveUp:
                for i in range(LENGTH):
                    snake[LENGTH-1-i] = snake[LENGTH-2-i]
                snake[0] = pygame.Rect(snake1[0], snake2[0]-SNAKESIZE, SNAKESIZE, SNAKESIZE)
                snake2[0] -= SNAKESIZE
        
        if moveLeft:
                for i in range(LENGTH):
                    snake[LENGTH-1-i] = snake[LENGTH-2-i]
                snake[0] = pygame.Rect(snake1[0]-SNAKESIZE, snake2[0], SNAKESIZE, SNAKESIZE)
                snake1[0] -= SNAKESIZE
                
        if moveRight:
                for i in range(LENGTH):
                    snake[LENGTH-1-i] = snake[LENGTH-2-i]
                snake[0] = pygame.Rect(snake1[0]+SNAKESIZE, snake2[0], SNAKESIZE, SNAKESIZE)
                snake1[0] += SNAKESIZE                     
                
          
        for i in range(LENGTH):
            pygame.draw.rect(windowSurface, WHITE, snake[i])

        if a == 0:
            c = 1
            while c >= 1:           
                b1 = random.randint(1,WINDOWWIDTH/20-2)*20
                b2 = random.randint(1,WINDOWHEIGHT/20-2)*20
                block = pygame.Rect(b1,b2,SNAKESIZE,SNAKESIZE)
                for i in range(LENGTH):
                    if snake[i].colliderect(block):
                        c = c + 1
                if c > 1:
                    c = 1
                elif c == 1:
                    c = 0
                
            pygame.draw.rect(windowSurface, GREEN, block)
            a = 1
        elif a == 1:
            pygame.draw.rect(windowSurface, GREEN, block)

        if snake[0].colliderect(block):
            food += 1
            LENGTH += 1
            if moveDown == True:
                snake.append(pygame.Rect(snake1[0], snake2[0]-LENGTH*SNAKESIZE, SNAKESIZE, SNAKESIZE))
            elif moveUp == True:
                snake.append(pygame.Rect(snake1[0], snake2[0]+LENGTH*SNAKESIZE, SNAKESIZE, SNAKESIZE))
            elif moveLeft == True:
                snake.append(pygame.Rect(snake1[0]+LENGTH*SNAKESIZE, snake2[0], SNAKESIZE, SNAKESIZE))
            elif moveRight == True:
                snake.append(pygame.Rect(snake1[0]-LENGTH*SNAKESIZE, snake2[0], SNAKESIZE, SNAKESIZE))
            a = 0
        b = 0
        for i in range(LENGTH-1):        
            if snake[0].colliderect(snake[i+1]):
                b += 1
        

        if b > 0:
            break
        
        if snake1[0] < 20 or snake1[0] >= WINDOWWIDTH-20:
            break
        elif snake2[0] < 20 or snake2[0] >= WINDOWHEIGHT-20:
            break     
           
        pygame.display.update()
        mainClock.tick(5+food)
        if food == win:
            break

    pygame.mixer.music.stop()
    if food != win:
        while True:           
            y = 0
            b = 0
            pygame.display.update()
            windowSurface.fill(BLACK)
            final()
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                if event.type == KEYDOWN:
                    if event.key == ord('y'):
                        y = y+1
                        break
                    if event.key == ord('n'):
                        terminate()
            if y == 1:
                pygame.display.update()
                mainClock.tick(20)
                break
       

    elif food == win :
        x = 0
        pygame.mixer.music.load("We Are The Champions.mp3")
        pygame.mixer.music.play(-1, 39.0)
        while True:            
            pygame.display.update()
            windowSurface.fill(BLACK)
            background_image1 = pygame.image.load("winner.jpg")
            drawText('You Win!!!!', font1, windowSurface, (WINDOWWIDTH*2 / 5)-90, (WINDOWHEIGHT*1 / 8))
            windowSurface.blit(background_image1, [350,150])
            drawText('Continue??(Y/N)', font, windowSurface, (WINDOWWIDTH*2 / 5)-50, (WINDOWHEIGHT*4 / 5))
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                if event.type == KEYDOWN:
                    if event.key == ord('y'):
                        pygame.mixer.music.stop()
                        x = x+1
                        break
                    if event.key == ord('n'):
                        terminate()

            if x == 1:
                break
                     

            
                

        

    
         
     
    
    


    


    


     
