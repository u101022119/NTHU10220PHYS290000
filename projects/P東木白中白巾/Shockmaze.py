""" 
 Simple graphics demo
  
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
"""
 
import pygame, sys
from pygame.locals import *
import os

pygame.init()
pygame.mixer.init()
windowsurface=pygame.display.set_mode((1200,600),0,32)
pygame.display.set_caption('Shock Maze')

BLACK = (0,0,0)
WHITE = (255, 255, 255)
GREEN = (0,255,0)
BLUE = (0,0,255)  

def terminate():
    pygame.quit()
    sys.exit()

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, WHITE)
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

basicFont = pygame.font.SysFont(None, 48)




drawText('Shock Maze OH YA !', basicFont, windowsurface, (1200 / 3), (600 / 3))
drawText('Press a key to start.', basicFont, windowsurface, (1200 / 3) + 30, (600 / 3) + 50)
drawText('Do not cheat !', basicFont, windowsurface, (1200 / 3) + 60, (600 / 3) + 100)
drawText('By pochunghandsome~~~', basicFont, windowsurface, (1200 / 3) + 90, (600 / 3) + 150)

pygame.display.update()
waitForPlayerToPressKey()





def game():
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Dota.mp3")
    pygame.mixer.music.play(10)    
    pygame.mouse.set_pos([75,575])
    while True:
        windowsurface.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit() 
                sys.exit()
       
        c=pygame.mouse.get_pos()
        rect1=pygame.draw.rect(windowsurface ,WHITE ,pygame.Rect(c[0], c[1] ,5,5))
        rect2=pygame.draw.rect(windowsurface ,BLACK ,pygame.Rect(50,550,100,50))
        rect3=pygame.draw.rect(windowsurface ,BLACK ,pygame.Rect(75,50,15,550))
        rect4=pygame.draw.rect(windowsurface ,BLACK ,pygame.Rect(75,50,100,50))
        rect5=pygame.draw.rect(windowsurface ,BLACK ,pygame.Rect(175,50,100,20))
        rect6=pygame.draw.rect(windowsurface ,BLACK ,pygame.Rect(275,50,20,50))
        rect7=pygame.draw.rect(windowsurface ,BLACK ,pygame.Rect(275,100,50,20))
        rect8=pygame.draw.rect(windowsurface ,BLACK ,pygame.Rect(325,100,20,50))
        rect9=pygame.draw.rect(windowsurface ,BLACK ,pygame.Rect(325,150,50,20))
        rect10=pygame.draw.rect(windowsurface ,BLACK ,pygame.Rect(375,150,20,50))
        rect11=pygame.draw.rect(windowsurface ,BLACK ,pygame.Rect(375,200,50,20))
        rect12=pygame.draw.rect(windowsurface ,BLACK ,pygame.Rect(425,200,15,50))
        rect13=pygame.draw.rect(windowsurface ,BLACK ,pygame.Rect(390,250,50,15))
        rect14=pygame.draw.rect(windowsurface ,BLACK ,pygame.Rect(390,250,15,65))
        rect15=pygame.draw.rect(windowsurface ,BLACK ,pygame.Rect(340,300,50,15))
        rect16=pygame.draw.rect(windowsurface ,BLACK ,pygame.Rect(340,300,15,65))
        rect17=pygame.draw.rect(windowsurface ,BLACK ,pygame.Rect(290,350,50,15))
        rect18=pygame.draw.rect(windowsurface ,BLACK ,pygame.Rect(290,350,15,65))
        rect19=pygame.draw.rect(windowsurface ,BLACK ,pygame.Rect(240,400,50,15))
    
        rect20=pygame.draw.rect(windowsurface ,BLACK ,pygame.Rect(220,400,20,200))
        rect21=pygame.draw.rect(windowsurface ,BLACK ,pygame.Rect(240,580,250,20))
        rect22=pygame.draw.rect(windowsurface ,BLACK ,pygame.Rect(490,430,20,250))
        rect23=pygame.draw.rect(windowsurface ,BLACK ,pygame.Rect(490,330,100,100))

        rect24=pygame.draw.rect(windowsurface ,BLACK ,pygame.Rect(590,360,300,12))
        rect25=pygame.draw.rect(windowsurface ,BLACK ,pygame.Rect(880,360,12,150))
        rect26=pygame.draw.rect(windowsurface ,BLACK ,pygame.Rect(642,510,250,12))
        rect27=pygame.draw.rect(windowsurface ,BLACK ,pygame.Rect(642,410,12,100))

        rect28=pygame.draw.rect(windowsurface ,BLACK ,pygame.Rect(642,410,92,12))
        rect29=pygame.draw.rect(windowsurface ,BLACK ,pygame.Rect(723,410,12,70))
        rect30=pygame.draw.rect(windowsurface ,BLACK ,pygame.Rect(723,468,100,12))
        rect31=pygame.draw.rect(windowsurface ,BLACK ,pygame.Rect(811,388,12,80))

        rect32=pygame.draw.rect(windowsurface ,BLACK ,pygame.Rect(611,388,200,12))
        rect33=pygame.draw.rect(windowsurface ,BLACK ,pygame.Rect(611,388,12,200))
        rect34=pygame.draw.rect(windowsurface ,BLACK ,pygame.Rect(611,576,400,12))
        rect35=pygame.draw.rect(windowsurface ,BLACK ,pygame.Rect(1011,0,189,600))
        drawText('Goal~', basicFont, windowsurface,1070,290)
        pygame.display.update()


        def isPointInsideRect(x, y, rect):
            if (x > rect.left) and (x < rect.right) \
               and (y > rect.top) and (y < rect.bottom):
                return True
            else:
                return False

    
        def doRectsOverlap(rect1, rect2 ,rect3 ,rect4 ,rect5 ,rect6 ,rect7, rect8, rect9, rect10, rect11, rect12, rect13, rect14, rect15, rect16, rect17, rect18, rect19, rect20, rect21, rect22, rect23, rect24, rect25, rect26, rect27, rect28, rect29, rect30, rect31, rect32, rect33, rect34,rect35 ):
            for a, b ,c ,d ,e ,f ,g ,h ,i ,j ,k ,l ,m ,n ,o ,p ,q ,r ,s ,t ,u ,v ,w ,x ,y ,z ,aa ,ab ,ac ,ad ,ae ,af ,ag ,ah ,ai, in [(rect1, rect2 ,rect3 ,rect4 ,rect5 ,rect6 ,rect7, rect8, rect9, rect10, rect11, rect12, rect13, rect14, rect15, rect16, rect17, rect18, rect19, rect20, rect21, rect22, rect23, rect24, rect25, rect26, rect27, rect28, rect29, rect30, rect31, rect32, rect33, rect34,rect35 )]:
                if ((isPointInsideRect(a.left, a.top, b)) or
                    (isPointInsideRect(a.left, a.bottom, b)) or
                    (isPointInsideRect(a.right, a.top, b)) or
                    (isPointInsideRect(a.right, a.bottom, b))or
                    (isPointInsideRect(a.left, a.top, c)) or
                    (isPointInsideRect(a.left, a.bottom, c)) or
                    (isPointInsideRect(a.right, a.top, c)) or
                    (isPointInsideRect(a.right, a.bottom, c))or
                    (isPointInsideRect(a.left, a.top, d)) or
                    (isPointInsideRect(a.left, a.bottom, d)) or
                    (isPointInsideRect(a.right, a.top, d)) or
                    (isPointInsideRect(a.right, a.bottom, d))or
                    (isPointInsideRect(a.left, a.top, e)) or
                    (isPointInsideRect(a.left, a.bottom, e)) or
                    (isPointInsideRect(a.right, a.top, e)) or
                    (isPointInsideRect(a.right, a.bottom, e)) or
                    (isPointInsideRect(a.left, a.top, f)) or
                    (isPointInsideRect(a.left, a.bottom, f)) or
                    (isPointInsideRect(a.right, a.top, f)) or
                    (isPointInsideRect(a.right, a.bottom, f)) or
                    (isPointInsideRect(a.left, a.top, g)) or
                    (isPointInsideRect(a.left, a.bottom, g)) or
                    (isPointInsideRect(a.right, a.top, g)) or
                    (isPointInsideRect(a.right, a.bottom, g)) or
                    (isPointInsideRect(a.left, a.top, h)) or
                    (isPointInsideRect(a.left, a.bottom, h)) or
                    (isPointInsideRect(a.right, a.top, h)) or
                    (isPointInsideRect(a.right, a.bottom, h)) or
                    (isPointInsideRect(a.left, a.top, i)) or
                    (isPointInsideRect(a.left, a.bottom, i)) or
                    (isPointInsideRect(a.right, a.top, i)) or
                    (isPointInsideRect(a.right, a.bottom, i)) or
                    (isPointInsideRect(a.left, a.top, j)) or
                    (isPointInsideRect(a.left, a.bottom, j)) or
                    (isPointInsideRect(a.right, a.top, j)) or
                    (isPointInsideRect(a.right, a.bottom, j)) or
                    (isPointInsideRect(a.left, a.top, k)) or
                    (isPointInsideRect(a.left, a.bottom, k)) or
                    (isPointInsideRect(a.right, a.top, k)) or
                    (isPointInsideRect(a.right, a.bottom, k))or
                    (isPointInsideRect(a.left, a.top, l)) or
                    (isPointInsideRect(a.left, a.bottom, l)) or
                    (isPointInsideRect(a.right, a.top, l)) or
                    (isPointInsideRect(a.right, a.bottom, l))or
                    (isPointInsideRect(a.left, a.top, m)) or
                    (isPointInsideRect(a.left, a.bottom, m)) or
                    (isPointInsideRect(a.right, a.top, m)) or
                    (isPointInsideRect(a.right, a.bottom, m))or
                    (isPointInsideRect(a.left, a.top, n)) or
                    (isPointInsideRect(a.left, a.bottom, n)) or
                    (isPointInsideRect(a.right, a.top, n)) or
                    (isPointInsideRect(a.right, a.bottom, n))or
                    (isPointInsideRect(a.left, a.top, o)) or
                    (isPointInsideRect(a.left, a.bottom, o)) or
                    (isPointInsideRect(a.right, a.top, o)) or
                    (isPointInsideRect(a.right, a.bottom, o))or
                    (isPointInsideRect(a.left, a.top, p)) or
                    (isPointInsideRect(a.left, a.bottom, p)) or
                    (isPointInsideRect(a.right, a.top, p)) or
                    (isPointInsideRect(a.right, a.bottom, p))or
                    (isPointInsideRect(a.left, a.top, q)) or
                    (isPointInsideRect(a.left, a.bottom, q)) or
                    (isPointInsideRect(a.right, a.top, q)) or
                    (isPointInsideRect(a.right, a.bottom, q))or
                    (isPointInsideRect(a.left, a.top, r)) or
                    (isPointInsideRect(a.left, a.bottom, r)) or
                    (isPointInsideRect(a.right, a.top, r)) or
                    (isPointInsideRect(a.right, a.bottom, r))or
                    (isPointInsideRect(a.left, a.top, s)) or
                    (isPointInsideRect(a.left, a.bottom, s)) or
                    (isPointInsideRect(a.right, a.top, s)) or
                    (isPointInsideRect(a.right, a.bottom, s))or
                    (isPointInsideRect(a.left, a.top, t)) or
                    (isPointInsideRect(a.left, a.bottom, t)) or
                    (isPointInsideRect(a.right, a.top, t)) or
                    (isPointInsideRect(a.right, a.bottom, t))or
                    (isPointInsideRect(a.left, a.top, u)) or
                    (isPointInsideRect(a.left, a.bottom, u)) or
                    (isPointInsideRect(a.right, a.top, u)) or
                    (isPointInsideRect(a.right, a.bottom, u))or
                    (isPointInsideRect(a.left, a.top, v)) or
                    (isPointInsideRect(a.left, a.bottom, v)) or
                    (isPointInsideRect(a.right, a.top, v)) or
                    (isPointInsideRect(a.right, a.bottom, v))or
                    (isPointInsideRect(a.left, a.top, w)) or
                    (isPointInsideRect(a.left, a.bottom, w)) or
                    (isPointInsideRect(a.right, a.top, w)) or
                    (isPointInsideRect(a.right, a.bottom, w))or
                    (isPointInsideRect(a.left, a.top, x)) or
                    (isPointInsideRect(a.left, a.bottom, x)) or
                    (isPointInsideRect(a.right, a.top, x)) or
                    (isPointInsideRect(a.right, a.bottom, x))or
                    (isPointInsideRect(a.left, a.top, y)) or
                    (isPointInsideRect(a.left, a.bottom, y)) or
                    (isPointInsideRect(a.right, a.top, y)) or
                    (isPointInsideRect(a.right, a.bottom, y))or
                    (isPointInsideRect(a.left, a.top, z)) or
                    (isPointInsideRect(a.left, a.bottom, z)) or
                    (isPointInsideRect(a.right, a.top, z)) or
                    (isPointInsideRect(a.right, a.bottom, z))or
                    (isPointInsideRect(a.left, a.top, aa)) or
                    (isPointInsideRect(a.left, a.bottom, aa)) or
                    (isPointInsideRect(a.right, a.top, aa)) or
                    (isPointInsideRect(a.right, a.bottom, aa))or
                    (isPointInsideRect(a.left, a.top, ab)) or
                    (isPointInsideRect(a.left, a.bottom, ab)) or
                    (isPointInsideRect(a.right, a.top, ab)) or
                    (isPointInsideRect(a.right, a.bottom, ab))or
                    (isPointInsideRect(a.left, a.top, ac)) or
                    (isPointInsideRect(a.left, a.bottom, ac)) or
                    (isPointInsideRect(a.right, a.top, ac)) or
                    (isPointInsideRect(a.right, a.bottom, ac))or
                    (isPointInsideRect(a.left, a.top, ad)) or
                    (isPointInsideRect(a.left, a.bottom, ad)) or
                    (isPointInsideRect(a.right, a.top, ad)) or
                    (isPointInsideRect(a.right, a.bottom, ad))or
                    (isPointInsideRect(a.left, a.top, ae)) or
                    (isPointInsideRect(a.left, a.bottom, ae)) or
                    (isPointInsideRect(a.right, a.top, ae)) or
                    (isPointInsideRect(a.right, a.bottom, ae))or
                    (isPointInsideRect(a.left, a.top, af)) or
                    (isPointInsideRect(a.left, a.bottom, af)) or
                    (isPointInsideRect(a.right, a.top, af)) or
                    (isPointInsideRect(a.right, a.bottom, af))or
                    (isPointInsideRect(a.left, a.top, ag)) or
                    (isPointInsideRect(a.left, a.bottom, ag)) or
                    (isPointInsideRect(a.right, a.top, ag)) or
                    (isPointInsideRect(a.right, a.bottom, ag))or
                    (isPointInsideRect(a.left, a.top, ah)) or
                    (isPointInsideRect(a.left, a.bottom, ah)) or
                    (isPointInsideRect(a.right, a.top, ah)) or
                    (isPointInsideRect(a.right, a.bottom, ah))):
                    return True
                if ((isPointInsideRect(a.left, a.top, ai)) or
                    (isPointInsideRect(a.left, a.bottom, ai)) or
                    (isPointInsideRect(a.right, a.top, ai)) or
                    (isPointInsideRect(a.right, a.bottom, ai))):
                    windowsurface.fill((0, 0, 0))                
                    drawText('You win !! Congratulation d^_^b', basicFont, windowsurface, (1200 / 3), (600 / 3))
                    drawText('Press a key to play again !', basicFont, windowsurface, (1200 / 3) - 30, (600 / 3) + 50)
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("Pygame.mp3")
                    pygame.mixer.music.play()
                    pygame.display.update()
                    waitForPlayerToPressKey()
                    return False
                else:
                    windowsurface.fill((0, 0, 0))                
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("laugh.mp3")
                    pygame.mixer.music.play(10)
                    
                    drawText('Game over !! HA !', basicFont, windowsurface, (1200 / 3), (600 / 3))
                    drawText('Press a key to restart. Try harder !', basicFont, windowsurface, (1200 / 3) - 30, (600 / 3) + 50)
                     
                    pygame.display.update()
                    waitForPlayerToPressKey()
                    return False
        

                

        if doRectsOverlap(rect1, rect2 ,rect3 ,rect4 ,rect5 ,rect6 ,rect7, rect8, rect9, rect10, rect11, rect12, rect13, rect14, rect15, rect16, rect17, rect18, rect19, rect20, rect21, rect22, rect23, rect24, rect25, rect26, rect27, rect28, rect29, rect30, rect31, rect32, rect33, rect34,rect35) == False:
            return False
        
        
        
                           
         
while True:
    game()


        
        
        
        


        
        

    
