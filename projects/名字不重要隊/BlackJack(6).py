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
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)


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
        basicFont = pygame.font.SysFont(None, 48)
        text1 = basicFont.render(' Welcome to BlackJack ', True, BLACK, YELLOW)
        text1Rect = text1.get_rect()
        text1Rect.centerx = 500
        text1Rect.centery = 200
        windowSurface.blit(text1, text1Rect)
        
        basicFont = pygame.font.SysFont(None, 30)           
        text2 = basicFont.render(' Press "SPACE" to continue... ', True, BLACK, WHITE)
        text2Rect = text2.get_rect()
        text2Rect.centerx = 500
        text2Rect.centery = 490
        
        windowSurface.blit(text2, text2Rect)
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    T=False

      
    windowSurface.fill(BLACK)
    pygame.display.update()
    T=True
    while T:
        
        basicFont = pygame.font.SysFont(None, 30)
        text1 = basicFont.render(' This is a game to see who can get the point that is more close to 21. ', True, BLACK, WHITE)
        text1Rect = text1.get_rect()
        text1Rect.centerx = 400
        text1Rect.centery = 50
        text2 = basicFont.render(' The following is the rule: ', True, BLACK, WHITE)
        text2Rect = text1.get_rect()
        text2Rect.centerx = 400
        text2Rect.centery = 80
        text3 = basicFont.render(' You and Computer will get a pair of cards. ', True, BLACK, WHITE)
        text3Rect = text1.get_rect()
        text3Rect.centerx = 400
        text3Rect.centery = 110
        text4 = basicFont.render(' One of the cards is open, and the other one is hiden.' , True, BLACK, WHITE)
        text4Rect = text1.get_rect()
        text4Rect.centerx = 400
        text4Rect.centery = 140
        text5 = basicFont.render(' And you can choose to get more cards or to stop. ', True, BLACK, WHITE)
        text5Rect = text1.get_rect()
        text5Rect.centerx = 400
        text5Rect.centery = 170
        text6 = basicFont.render(' After you and Computer both finish adding cards, it will be the time to see who is the winner. ', True, BLACK, WHITE)
        text6Rect = text1.get_rect()
        text6Rect.centerx = 400
        text6Rect.centery = 200
        text7 = basicFont.render(' Who gets the point more close to 21, he/she will be the winner. ', True, BLACK, WHITE)
        text7Rect = text1.get_rect()
        text7Rect.centerx = 400
        text7Rect.centery = 230
        text8 = basicFont.render(' Be careful, when your point is bigger than 21, then you will lose. ', True, BLACK, WHITE)
        text8Rect = text1.get_rect()
        text8Rect.centerx = 400
        text8Rect.centery = 260
        text9 = basicFont.render(' And, if you and the computer get the same point, the computer will win the game. ', True, BLACK, WHITE)
        text9Rect = text1.get_rect()
        text9Rect.centerx = 400
        text9Rect.centery = 290
        text10 = basicFont.render(' Last, 1~10 express the same point, 11 expresses 10 point, 12 and 13 express 0.5 point. ', True, BLACK, WHITE)
        text10Rect = text1.get_rect()
        text10Rect.centerx = 400
        text10Rect.centery = 320
        text11 = basicFont.render(' Now, press "SPACE" to start the game! ', True, BLACK, YELLOW)
        text11Rect = text1.get_rect()
        text11Rect.centerx = 400
        text11Rect.centery = 400
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

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    T=False


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

    def comparison(sumP2):
        if sum(sumP2) > 21:
            print 'You lose!!!'
            pygame.quit()
            sys.exit()
        else:
            pass    
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
                p.append(a)
                if i == 2:
                    number2= a
                else:
                    number4=a
            else:
                pc.append(a)
                if i == 1:
                    number1=a
                else:
                    number3=a

        sumP = [numerical(select[1]),numerical(select[3])]

        

            
        while T:
            
            windowSurface.blit(poker[number2], (400,50))
            windowSurface.blit(poker[number1],(500,400))
            windowSurface.blit(poker[number3],(400,400))
            text1 = basicFont.render('computer', True, BLACK, WHITE)
            text1Rect = text1.get_rect()
            text1Rect.centerx = 250
            text1Rect.centery = 50
            text2 = basicFont.render('player', True, BLACK, WHITE)
            text2Rect = text1.get_rect()
            text2Rect.centerx = 710
            text2Rect.centery = 400
            windowSurface.blit(text1, text1Rect)
            windowSurface.blit(text2, text2Rect)
            text1 = basicFont.render('Do you want to add one more card?', True, RED, BLACK)
            text1Rect = text1.get_rect()
            text1Rect.centerx = 450
            text1Rect.centery = 240
            text2 = basicFont.render('If you do, press y key.', True, RED, BLACK)
            text2Rect = text2.get_rect()
            text2Rect.centerx = 450
            text2Rect.centery = 280
            text3 = basicFont.render('If that is enough already, press n key.', True, RED, BLACK)
            text3Rect = text3.get_rect()
            text3Rect.centerx = 450
            text3Rect.centery = 320
            text4 = basicFont.render('Now, what is your decision?', True, RED, BLACK)
            text4Rect = text4.get_rect()
            text4Rect.centerx = 450
            text4Rect.centery = 360
            windowSurface.blit(text1, text1Rect)
            windowSurface.blit(text2, text2Rect)
            windowSurface.blit(text3, text3Rect)
            windowSurface.blit(text4, text4Rect)

            
    #Add the cards    
            T=True
            i=600
            sumP=[numerical(select[1]),numerical(select[3])]  
            sumP2=[numerical(select[2]),numerical(select[0])]
            
            while T:
                pygame.display.update()
                for event in pygame.event.get():
                   if event.type == KEYDOWN:
                       if event.key == ord('y'):
                           
                           if sum(sumP)<21:
                               i+=50
                               length += 1
                               a= add(random.randint(1,52))
                               select.append(a)
                               sumP.append(numerical(a))
                               p.append(a)
                               number5=a
                               windowSurface.blit(poker[number5], (i,400))
                           else:
                               text8 = basicFont.render('The point is more than 21', True, RED, BLACK)
                               text8Rect = text1.get_rect()
                               text8Rect.centerx = 200
                               text8Rect.centery = 50
                               text9 = basicFont.render('Please press "n"', True, RED, BLACK)
                               text9Rect = text1.get_rect()
                               text9Rect.centerx = 200
                               text9Rect.centery = 100
                               windowSurface.blit(text8, text8Rect)
                               windowSurface.blit(text9, text9Rect)
                               pygame.display.update()
                               

                       elif event.key==K_n:
                           T=True
                           print sumP2
                           print number4
                           while T:
                               windowSurface.blit(poker[number4], (500,50))
                               
                               if sum(sumP2)<16:
                                   i+=50
                                   length += 1
                                   a= add(random.randint(1,52))
                                   select.append(a)
                                   sumP2.append(numerical(a))
                                   p.append(a)
                                   number6=a
                                   windowSurface.blit(poker[number6], (i,50))
                               else:
                                   
                                   text9 = basicFont.render('Please press "space"', True, RED, BLACK)
                                   text9Rect = text1.get_rect()
                                   text9Rect.centerx = 200
                                   text9Rect.centery = 100

                                   windowSurface.blit(text9, text9Rect)
        
                                   pygame.display.update()
                                   for event in pygame.event.get():
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

    p=sumP
    c=sumP2

    def add_allp(p):
        player_point = 0
        for x in p:
            player_point += x
        return player_point


    def add_allc(c):
        computer_point = 0
        for x in c:
            computer_point += x
        return computer_point

    T=True
    while T:

        basicFont = pygame.font.SysFont(None, 30)
        text1 = basicFont.render(" Your point is ", True, BLACK, WHITE)
        text1Rect = text1.get_rect()
        text1Rect.centerx = 450
        text1Rect.centery = 200
        windowSurface.blit(text1, text1Rect)
        pygame.display.update()


        basicFont = pygame.font.SysFont(None, 30)
        text2 = basicFont.render( str(add_allp(p))  , True, BLACK, WHITE)
        text2Rect = text2.get_rect()
        text2Rect.centerx = 550
        text2Rect.centery = 200
        windowSurface.blit(text2, text2Rect)
        pygame.display.update()


        basicFont = pygame.font.SysFont(None, 30)
        text3 = basicFont.render(" Computer's point is ", True, BLACK, WHITE)
        text3Rect = text3.get_rect()
        text3Rect.centerx = 450
        text3Rect.centery = 300
        windowSurface.blit(text3, text3Rect)
        pygame.display.update()


        basicFont = pygame.font.SysFont(None, 30)
        text4 = basicFont.render( str(add_allc(c))  , True, BLACK, WHITE)
        text4Rect = text4.get_rect()
        text4Rect.centerx = 590
        text4Rect.centery = 300
        windowSurface.blit(text4, text4Rect)
        pygame.display.update()
        

        basicFont = pygame.font.SysFont(None, 60)
        text5 = basicFont.render(' Sorry, you lose! ', True, BLACK, RED)
        text5Rect = text5.get_rect()
        text5Rect.centerx = 450
        text5Rect.centery = 500
        text6 = basicFont.render(' Congratulations, you win! ', True, BLACK, RED)
        text6Rect = text6.get_rect()
        text6Rect.centerx = 450
        text6Rect.centery = 500
        
        if add_allp(p) >21:
            windowSurface.blit(text5, text5Rect)
            pygame.display.update()
        elif add_allc(c) > 21:
            windowSurface.blit(text6, text6Rect)
            pygame.display.update()
        elif add_allc(c) >= add_allp(p):
            windowSurface.blit(text5, text5Rect)
            pygame.display.update()
        else:
            windowSurface.blit(text6, text6Rect)
            pygame.display.update()

        for event in pygame.event.get():
            
            basicFont = pygame.font.SysFont(None, 30)
            text7 = basicFont.render(' Press "SPACE" to continue... ', True, BLACK, YELLOW)
            text7Rect = text7.get_rect()
            text7Rect.centerx = 450
            text7Rect.centery = 550
            windowSurface.blit(text7, text7Rect)
            pygame.display.update()
            
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    T=False


    T=True
    while T:
        
        windowSurface.fill(BLACK)
        
        basicFont = pygame.font.SysFont(None, 50)
        text1= basicFont.render(' Do you want to play again? Y/N ', True, BLACK, YELLOW)
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
                
