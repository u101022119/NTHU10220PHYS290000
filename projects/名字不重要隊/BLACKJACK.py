import pygame, sys, random
from pygame.locals import *

#set up pygame
pygame.init()


#set up the window
windowSurface = pygame.display.set_mode((1000,600), 0, 32)
pygame.display.set_caption('BlackJack')



#set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (229, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
STEELBLUE = (99, 184, 255)

for event in pygame.event.get():
    if event.type == QUIT:
        pygame.quit()
        sys.exit()
    if event.type == KEYUP:
        if event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()





#Turn on
back_ground_image= r'D:\PySDL2-0.9.2\2.jpg'
background=pygame.image.load(back_ground_image).convert()
pygame.display.update()

pygame.mixer.music.load(r'D:\PySDL2-0.9.2\3.mp3')
pygame.mixer.music.play(-1, 0.0)
musicPlaying = True
    


T=True
while T:
                
    windowSurface.blit(background, (0,0))
    basicFont = pygame.font.SysFont(None, 54)
    text1 = basicFont.render(' Welcome to BlackJack ', True, YELLOW, BLACK)
    text1Rect = text1.get_rect()
    text1Rect.centerx = 230
    text1Rect.centery = 35
    windowSurface.blit(text1, text1Rect)
        
    basicFont = pygame.font.SysFont(None, 28)           
    text2 = basicFont.render(' Press "SPACE" to continue... ', True, WHITE, BLACK)
    text2Rect = text2.get_rect()
    text2Rect.centerx = 840
    text2Rect.centery = 570
        
    windowSurface.blit(text2, text2Rect)
    pygame.display.update()
        
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                T=False
      
windowSurface.fill(BLACK)
pygame.display.update()

T=True
while T:
        
    basicFont = pygame.font.SysFont(None, 28)
    text1 = basicFont.render('This is a game to see who can get the point that is more close to 21. ', True, WHITE, BLACK)
    text1Rect = text1.get_rect()
    text1Rect.centerx = 400
    text1Rect.centery = 55
    text2 = basicFont.render('The following is the rule: ', True, WHITE, BLACK)
    text2Rect = text1.get_rect()
    text2Rect.centerx = 400
    text2Rect.centery = 85
    text3 = basicFont.render('You and Computer will get a pair of cards. ', True, WHITE, BLACK)
    text3Rect = text1.get_rect()
    text3Rect.centerx = 400
    text3Rect.centery = 115
    text4 = basicFont.render('One of the cards is open, and the other one is hiden.' , True, WHITE, BLACK)
    text4Rect = text1.get_rect()
    text4Rect.centerx = 400
    text4Rect.centery = 145
    text5 = basicFont.render('And you can choose to get more cards or to stop. ', True, WHITE, BLACK)
    text5Rect = text1.get_rect()
    text5Rect.centerx = 400
    text5Rect.centery = 175
    text6 = basicFont.render('After you and Computer both finish adding cards, that\'s see who is the winner. ', True, WHITE, BLACK)
    text6Rect = text1.get_rect()
    text6Rect.centerx = 400
    text6Rect.centery = 205
    text7 = basicFont.render('Who gets the point not above but more close to 21 will be the winner. ', True, WHITE, BLACK)
    text7Rect = text1.get_rect()
    text7Rect.centerx = 400
    text7Rect.centery = 235
    text8 = basicFont.render('Besides, if someone gets the point less than 16, he/she will be loser. ', True, WHITE, BLACK)
    text8Rect = text1.get_rect()
    text8Rect.centerx = 400
    text8Rect.centery = 265
    text9 = basicFont.render('And, it will be deuce when you and the computer both lose the game. ', True, WHITE, BLACK)
    text9Rect = text1.get_rect()
    text9Rect.centerx = 400
    text9Rect.centery = 295
    text10 = basicFont.render('Be careful, if you and the computer get the same point, the computer will win the game. ', True, WHITE, BLACK)
    text10Rect = text1.get_rect()
    text10Rect.centerx = 400
    text10Rect.centery = 325
    text11 = basicFont.render('Last, 2~10 express the same point as itself. J, Q and K express 10 point. Ace can be 11 or 1. ', True, WHITE, BLACK)
    text11Rect = text1.get_rect()
    text11Rect.centerx = 400
    text11Rect.centery = 360
    windowSurface.blit(text1, text1Rect)
    windowSurface.blit(text2, text2Rect)
    windowSurface.blit(text3, text3Rect)
    windowSurface.blit(text4, text4Rect)
    windowSurface.blit(text5, text5Rect)
    windowSurface.blit(text6, text6Rect)
    windowSurface.blit(text7, text7Rect)
    windowSurface.blit(text8, text8Rect)
    windowSurface.blit(text9, text9Rect)
    windowSurface.blit(text10, text10Rect)
    windowSurface.blit(text11, text11Rect)
    pygame.display.update()
    
    basicFont = pygame.font.SysFont(None, 55)
    text12 = basicFont.render(' Now, press "SPACE" to start the game! ', True, YELLOW, BLACK)
    text12Rect = text1.get_rect()
    text12Rect.centerx = 400
    text12Rect.centery = 450
    windowSurface.blit(text12, text12Rect)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                T=False
                
T=True
while T:


    #Start the game (get the cards)
    back_ground_image= r'D:\PySDL2-0.9.2\images.jpg'
    background=pygame.image.load(back_ground_image).convert()
    pokerback_image= r'D:\PySDL2-0.9.2\pokerback.jpg'
    pokerback=pygame.image.load(pokerback_image).convert()
    poker=[0]
    for i in range(1,53):
        poker.append(pygame.image.load('D:\\PySDL2-0.9.2\\poker\\'+str(i)+'.gif').convert())
        
    pygame.display.update()
    def add(y):
        while True:
            same = 0
            for i in range(length):
                if y == select[i]:
                    same += 1
            if same > 0 :
                y = random.randint(1,52)
            else:
                return y
    def numerical(n):
        remainder = n%13
        if remainder == 11:
            return 10
        elif remainder == 12:
            return 10 
        elif remainder == 0:
            return 10
        else:
            return remainder

    def comparison(sumP):
        if sum(sumP) > 21:
            print 'You lose!!!'
            pygame.quit()
            sys.exit()
        else:
            pass

    def comparison(sumPC):
        if sum(sumPC) > 21:
            print 'You lose!!!'
            pygame.quit()
            sys.exit()
        else:
            pass

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
    
    T=True
    while T:
                
        windowSurface.blit(background, (0,0))
        windowSurface.blit(pokerback, (500,50))
        
        import random

        select = []
        p = []
        pc = []
        length = -1
        mydict= {1:"spade1", 2:"spade2", 3:"spade3", 4:"spade4", 5:"spade5", 6:"spade6", 7:"spade7", 8:"spade8", 9:"spade9", 10:"spade10",
                 11:"spade11", 12:"spade12", 13:"spade13", 14:"heart1", 15:"heart2", 16:"heart3", 17:"heart4", 18:"heart5", 19:" heart6", 20:"heart7",
                 21:"heart8", 22:"heart9", 23:"heart10", 24:"heart11", 25:"heart12", 26:"heart13", 27:"diamond1", 28:"diamond2", 29:" diamond3", 30:"diamond4",
                 31:"diamond5", 32:"diamond6", 33:"diamond7", 34:"diamond8", 35:"diamond9", 36:"diamond10", 37:"diamond11", 38:"diamond12", 39:" diamond13", 40:"club1",
                 41:"club2", 42:"club3", 43:"club4", 44:" club5", 45:"club6", 46:"club7", 47:"club8", 48:"club9", 49:"club10", 50:"club11", 51:"club12", 52:"club13"}
        for i in range(4):
            length += 1
            a = add(random.randint(1,52))
            select.append(a)
            if i%2 == 0:
                pc.append(a)
                if i == 2:
                    number2= a
                else:
                    number4=a
            else:
                p.append(a)
                if i == 1:
                    number1=a
                else:
                    number3=a

        sumP = [numerical(select[1]),numerical(select[3])]

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()       

        while T:
                        
            basicFont = pygame.font.SysFont(None, 30)
            windowSurface.blit(poker[number2], (400,50))
            windowSurface.blit(poker[number1],(500,400))
            windowSurface.blit(poker[number3],(400,400))
            text1 = basicFont.render('computer', True, BLACK, WHITE)
            text1Rect = text1.get_rect()
            text1Rect.centerx = 250
            text1Rect.centery = 50
            text2 = basicFont.render('player', True, BLACK, WHITE)
            text2Rect = text1.get_rect()
            text2Rect.centerx = 650
            text2Rect.centery = 360
            windowSurface.blit(text1, text1Rect)
            windowSurface.blit(text2, text2Rect)
            text1 = basicFont.render('Do you want to add one more card?', True, RED, STEELBLUE)
            text1Rect = text1.get_rect()
            text1Rect.centerx = 250
            text1Rect.centery = 240
            text2 = basicFont.render('If you do, press Y key.', True, RED, STEELBLUE)
            text2Rect = text2.get_rect()
            text2Rect.centerx = 185
            text2Rect.centery = 280
            text3 = basicFont.render('If that is enough already, press N key.', True, RED, STEELBLUE)
            text3Rect = text3.get_rect()
            text3Rect.centerx = 260
            text3Rect.centery = 320
            text4 = basicFont.render('Now, what is your decision?', True, RED, STEELBLUE)
            text4Rect = text4.get_rect()
            text4Rect.centerx = 215
            text4Rect.centery = 360
            windowSurface.blit(text1, text1Rect)
            windowSurface.blit(text2, text2Rect)
            windowSurface.blit(text3, text3Rect)
            windowSurface.blit(text4, text4Rect)
               
            
    #Add the cards    
            
            i=600
            sumP=[numerical(select[1]),numerical(select[3])]  
            sumPC=[numerical(select[2]),numerical(select[0])]
            T=True
            U=True
            while T :
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYUP:
                        if event.key == K_ESCAPE:
                            pygame.quit()
                            sys.exit()                              
                    if event.type == KEYDOWN:
                        if event.key == ord('y'):                        
                            if sum(sumP)<=21:
                                i+=50
                                length += 1
                                a= add(random.randint(1,52))
                                select.append(a)
                                sumP.append(numerical(a))
                                p.append(a)
                                number5=a
                                windowSurface.blit(poker[number5], (i,400))
                                if event.key==K_n:
                                    U = False
                                if sum(sumP)>21:
                                    U = False
                                    
                            if sum(sumP) > 21:
                                basicFont = pygame.font.SysFont(None, 30)
                                text8 = basicFont.render('The point is more than 21', True, BLACK, STEELBLUE)
                                text8Rect = text1.get_rect()
                                text8Rect.centerx = 780
                                text8Rect.centery = 50
                                text9 = basicFont.render("Press 'N' to continue", True, BLACK, STEELBLUE)
                                text9Rect = text1.get_rect()
                                text9Rect.centerx = 780
                                text9Rect.centery = 100
                                windowSurface.blit(text8, text8Rect)
                                windowSurface.blit(text9, text9Rect)
                                pygame.display.update()
                                U = False
                                
                        if event.key==K_n:
                            T=True
                            c=sumPC
                            if int(1) in sumPC:
                                if sum(c)<12:
                                    sumPC.append(10)
                                    pc.append(10) 
                            while T:
                                windowSurface.blit(poker[number4], (500,50))
                               
                                if sum(sumPC)<16:
                                    i+=50
                                    length += 1
                                    a= add(random.randint(1,52))
                                    select.append(a)
                                    sumPC.append(numerical(a))
                                    pc.append(a)
                                    number6=a
                                    windowSurface.blit(poker[number6], (i,50))
                                else:
                                   
                                    text9 = basicFont.render("Press 'SPACE' to continue", True, BLACK, STEELBLUE)
                                    text9Rect = text1.get_rect()
                                    text9Rect.centerx = 780
                                    text9Rect.centery = 150

                                    windowSurface.blit(text9, text9Rect)
        
                                    pygame.display.update()
                                    for event in pygame.event.get():
                                        if event.type == QUIT:
                                            pygame.quit()
                                            sys.exit()
                                        if event.type == KEYUP:
                                            if event.key == K_ESCAPE:
                                                pygame.quit()
                                                sys.exit()
                                        if event.type == KEYDOWN:
                                            if event.key == K_SPACE:
                                                T=False 
  
                
    #see who is winner

    windowSurface.fill(BLACK)
    pygame.display.update()                
    back_ground_image= r'D:\PySDL2-0.9.2\images.jpg'
    background=pygame.image.load(back_ground_image).convert()
    windowSurface.blit(background, (0,0))
    pygame.display.update()

    sumP
    sumPC

    def add_allp(sumP):
        player_point = 0
        for x in sumP:
            player_point += x
        return player_point


    def add_allc(sumPC):
        computer_point = 0
        for x in sumPC:
            computer_point += x
        return computer_point

    T=True
    while T:

        basicFont = pygame.font.SysFont(None, 40)
        text1 = basicFont.render(" Your point is ", True, BLACK, STEELBLUE)
        text1Rect = text1.get_rect()
        text1Rect.centerx = 480
        text1Rect.centery = 200
        windowSurface.blit(text1, text1Rect)
        pygame.display.update()


        basicFont = pygame.font.SysFont(None, 50)
        text2 = basicFont.render( str(add_allp(sumP))  , True, RED, STEELBLUE)
        text2Rect = text2.get_rect()
        text2Rect.centerx = 660
        text2Rect.centery = 200
        windowSurface.blit(text2, text2Rect)
        pygame.display.update()


        basicFont = pygame.font.SysFont(None, 40)
        text3 = basicFont.render(" Computer's point is ", True, BLACK, STEELBLUE)
        text3Rect = text3.get_rect()
        text3Rect.centerx = 480
        text3Rect.centery = 300
        windowSurface.blit(text3, text3Rect)
        pygame.display.update()


        basicFont = pygame.font.SysFont(None, 50)
        text4 = basicFont.render( str(add_allc(sumPC))  , True, RED, STEELBLUE)
        text4Rect = text4.get_rect()
        text4Rect.centerx = 660
        text4Rect.centery = 300
        windowSurface.blit(text4, text4Rect)
        pygame.display.update()
        

        basicFont = pygame.font.SysFont(None, 60)
        text5 = basicFont.render(' Sorry, you lose! ', True, RED, STEELBLUE)
        text5Rect = text5.get_rect()
        text5Rect.centerx = 500
        text5Rect.centery = 500
        text6 = basicFont.render(' Congratulations, you win! ', True, RED, STEELBLUE)
        text6Rect = text6.get_rect()
        text6Rect.centerx = 500
        text6Rect.centery = 500
        text7 = basicFont.render(' Deuce. ', True, BLACK, STEELBLUE)
        text7Rect = text7.get_rect()
        text7Rect.centerx = 500
        text7Rect.centery = 500
        
        if int(1) in sumP:
            if add_allp(sumP)<12:
                sumP.append(10)
        if int(1) in sumPC:
            if add_allc(sumPC)<12:
                sumPC.append(10)
        if add_allp(sumP) > 21 and add_allc(sumPC) > 21:
            windowSurface.blit(text7, text7Rect)
            pygame.display.update()
        elif add_allp(sumP) < 16 and add_allc(sumPC) > 21:
            windowSurface.blit(text7, text7Rect)
            pygame.display.update()
        elif add_allp(sumP) > 21:
            windowSurface.blit(text5, text5Rect)
            pygame.display.update()            
        elif add_allc(sumPC) > 21:
            windowSurface.blit(text6, text6Rect)
            pygame.display.update()
        elif add_allc(sumPC) >= add_allp(sumP):
            windowSurface.blit(text5, text5Rect)
            pygame.display.update()
        else:
            windowSurface.blit(text6, text6Rect)
            pygame.display.update()

        for event in pygame.event.get():
            
            basicFont = pygame.font.SysFont(None, 30)
            text7 = basicFont.render("Press 'SPACE' to continue...", True, BLACK, STEELBLUE)
            text7Rect = text7.get_rect()
            text7Rect.centerx = 500
            text7Rect.centery = 550
            windowSurface.blit(text7, text7Rect)
            pygame.display.update()

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    T=False


    T=True
    while T:
                    
        windowSurface.fill(BLACK)
        
        basicFont = pygame.font.SysFont(None, 50)
        text1= basicFont.render(' Do you want to play again? Y/N ', True, YELLOW, BLACK)
        text1Rect = text1.get_rect()
        text1Rect.centerx = 500
        text1Rect.centery = 300
        windowSurface.blit(text1, text1Rect)
        pygame.display.update()

     
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame. quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == ord('n') :
                    pygame.quit()
                    sys.exit()
                if event.key == ord('y'):
                    T=False
            
    T=True
                
