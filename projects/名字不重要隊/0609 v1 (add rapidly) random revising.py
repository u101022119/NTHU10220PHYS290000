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



R=True
while R:

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
        pygame.display.update()
        
        basicFont = pygame.font.SysFont(None, 30)
        text2 = basicFont.render(' Press "SPACE" to continue... ', True, BLACK, WHITE)
        text2Rect = text2.get_rect()
        text2Rect.centerx = 500
        text2Rect.centery = 400
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
    
    def choose1(x):
        if x == a:
            return choose1(random.randint(1, 52))
        else:
            return x

    def choose2(x):
        if x == a:
            return choose2(random.randint(1,52))
        elif x == b:
            return choose2(random.randint(1,52))
        else:
            return x

    def choose3(x):
        if x == a:
            return choose3(random.randint(1,52))
        elif x == b:
            return choose3(random.randint(1,52))
        elif x == c:
            return choose3(random.randint(1,52))
        else:
            return x
    
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
                
    def add_allp(P):
        player_point = 0
        for x in P:
            player_point += point[x]
        return player_point


    def add_allc(C):
        computer_point = 0
        for x in C:
            computer_point += point[x]
        return computer_point
        
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
    T=True
    while T:
        windowSurface.blit(background, (0,0))
        windowSurface.blit(pokerback, (500,50))

        select = []        
        length = -1
        mydict= {1:"spade1", 2:"spade2", 3:"spade3", 4:"spade4", 5:"spade5", 6:"spade6", 7:"spade7", 8:"spade8", 9:"spade9", 10:"spade10",
                 11:"spade11", 12:"spade12", 13:"spade13", 14:"heart1", 15:"heart2", 16:"heart3", 17:"heart4", 18:"heart5", 19:" heart6", 20:"heart7",
                 21:"heart8", 22:"heart9", 23:"heart10", 24:"heart11", 25:"heart12", 26:"heart13", 27:"diamond1", 28:"diamond2", 29:" diamond3", 30:"diamond4",
                 31:"diamond5", 32:"diamond6", 33:"diamond7", 34:"diamond8", 35:"diamond9", 36:"diamond10", 37:"diamond11", 38:"diamond12", 39:" diamond13", 40:"club1",
                 41:"club2", 42:"club3", 43:"club4", 44:" club5", 45:"club6", 46:"club7", 47:"club8", 48:"club9", 49:"club10", 50:"club11", 51:"club12", 52:"club13"}

        a=random.randint(1,52)
        b=choose1(random.randint(1, 52))
        c=choose2(random.randint(1,52))
        d=choose3(random.randint(1, 52))
        P = [mydict[a],mydict[c]]
        C = [mydict[b],mydict[d]]


        while T:            
            windowSurface.blit(poker[b], (400,50))
            windowSurface.blit(poker[a],(500,400))
            windowSurface.blit(poker[c],(400,400))
            text1 = basicFont.render('computer', True, BLACK, WHITE)
            text1Rect = text1.get_rect()
            text1Rect.centerx = 250
            text1Rect.centery = 50
            text2 = basicFont.render('player', True, BLACK, WHITE)
            text2Rect = text2.get_rect()
            text2Rect.centerx = 710
            text2Rect.centery = 400
            windowSurface.blit(text1, text1Rect)
            windowSurface.blit(text2, text2Rect)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        T=False
        
    #Add the cards(player)
        T=True
        nicht_add = False
        while T:
            basicFont = pygame.font.SysFont(None, 48)
            text1 = basicFont.render('Do you want to add one more card?', True, RED, BLACK)
            text1Rect = text1.get_rect()
            text1Rect.centerx = 400
            text1Rect.centery = 180
            text2 = basicFont.render('If you do, press Y key.', True, RED, BLACK)
            text2Rect = text2.get_rect()
            text2Rect.centerx = 400
            text2Rect.centery = 220
            text3 = basicFont.render('If that is enough already, press N key.', True, RED, BLACK)
            text3Rect = text3.get_rect()
            text3Rect.centerx = 400
            text3Rect.centery = 260
            text4 = basicFont.render('Now, what is your decision?', True, RED, BLACK)
            text4Rect = text4.get_rect()
            text4Rect.centerx = 400
            text4Rect.centery = 300
            windowSurface.blit(text1, text1Rect)
            windowSurface.blit(text2, text2Rect)
            windowSurface.blit(text3, text3Rect)
            windowSurface.blit(text4, text4Rect)
            pygame.display.update()    
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_y:
                        T = False
                        nicht_add = True
                    if event.key == K_n:
                        T = False
                        nicht_add = False
        
        e = random.randint(1,52)        
        while nicht_add:
            select.append(e)
            P.append(mydict[e])
            windowSurface.blit(poker[e], (600,400))
            text1 = basicFont.render('One more?', True, RED, BLACK)
            text1Rect = text1.get_rect()
            text1Rect.centerx = 250
            text1Rect.centery = 380
            windowSurface.blit(text1, text1Rect)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_y:
                        T = True
                        nicht_add = False
                        computer = True
                    if event.key == K_n:
                        T = False
                        nicht_add = False
                        computer = True

        f = random.randint(1,52)
        while T:                
            select.append(f)
            P.append(mydict[f])
            windowSurface.blit(poker[f], (700,400))
            text1 = basicFont.render('One more?', True, RED, BLACK)
            text1Rect = text1.get_rect()
            text1Rect.centerx = 250
            text1Rect.centery = 420
            windowSurface.blit(text1, text1Rect)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_y:
                        T = False
                        nicht_add = True
                        computer = True
                    if event.key == K_n:
                        T = False
                        nicht_add = False
                        computer = True
                
        g = random.randint(1,52)
        while nicht_add:       
            select.append(g)
            P.append(mydict[g])
            windowSurface.blit(poker[g], (800,400))
            text1 = basicFont.render('One more?', True, RED, BLACK)
            text1Rect = text1.get_rect()
            text1Rect.centerx = 250
            text1Rect.centery = 460
            windowSurface.blit(text1, text1Rect)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_y:
                        T = True
                        nicht_add = False
                        computer = True
                    if event.key == K_n:
                        T = False
                        nicht_add = False
                        computer = True
                        
        
    #while addcard:
     #   
      #  b = add(random.randint(1,52))
       # select.append(b)
        #p.append(mydict[b])
        #n = 0 
        #windowSurface.blit(poker[b], (700,400))
        #pygame.display.update()
        #for event in pygame.event.get():
        #    if event.type == KEYDOWN:
        #        if event.key == K_SPACE:
        #            addcard = False
                    
       

                
        h = random.randint(1,52)
        while computer:
            if add_allc(C) > 15:
                select.append(h)
                C.append(mydict[h])
                windowSurface.blit(poker[h], (600,50))
                pygame.display.update()    
                text1 = basicFont.render('Computer\'s turn...', True, RED, BLACK)
                text1Rect = text1.get_rect()
                text1Rect.centerx = 300
                text1Rect.centery = 50
                windowSurface.blit(text1, text1Rect)
                pygame.display.update()

                

    #add the cards(computer)
   # T = True
  #  while T:
    #    computer_add()
                    
                    
    #see who is winner

    
    point = {'spade1' : 1, 'spade2' : 2, 'spade3' : 3, 'spade4' : 4, 'spade5' : 5, 'spade6' : 6, 'spade7' : 7, 'spade8' : 8, 'spade9' : 9, 'spade10' : 10, 'spade11' : 10, 'spade12' : 10, 'spade13' : 10, 'heart1' : 1, 'heart2' : 2, 'heart3' : 3, 'heart4' : 4, 'heart5' : 5, 'heart6' : 6, 'heart7' : 7, 'heart8' : 8, 'heart9' : 9, 'heart10' : 10, 'heart11' : 10, 'heart12' : 10, 'heart13' : 10, 'diamond1' : 1, 'diamond2' : 2, 'diamond3' : 3, 'diamond4' : 4, 'diamond5' : 5, 'diamond6' : 6, 'diamond' : 7, 'diamond8' : 8, 'diamond9' : 9, 'diamond10' : 10, 'diamond11' : 10, 'diamond12' : 10 , 'diamond13' : 10, 'club1' : 1, 'club2' : 2, 'club3' : 3, 'club4' : 4, 'club5' : 5, 'club6' : 6, 'club7' : 7, 'club8' : 8, 'club9' : 9, 'club10' : 10, 'club11' : 10, 'club12' : 10, 'club13' : 10}
    
    T=True
    while T:
        P=['spade2','club3','diamond11','club3']
        C=['heart1','spade1','heart2','club11']
            
    
    #point = {'spade1' : 1, 'spade2' : 2, 'spade3' : 3, 'spade4' : 4, 'spade5' : 5, 'spade6' : 6, 'spade7' : 7, 'spade8' : 8, 'spade9' : 9, 'spade10' : 10, 'spade11' : 10, 'spade12' : 10, 'spade13' : 10, 'heart1' : 1, 'heart2' : 2, 'heart3' : 3, 'heart4' : 4, 'heart5' : 5, 'heart6' : 6, 'heart7' : 7, 'heart8' : 8, 'heart9' : 9, 'heart10' : 10, 'heart11' : 10, 'heart12' : 10, 'heart13' : 10, 'diamond1' : 1, 'diamond2' : 2, 'diamond3' : 3, 'diamond4' : 4, 'diamond5' : 5, 'diamond6' : 6, 'diamond' : 7, 'diamond8' : 8, 'diamond9' : 9, 'diamond10' : 10, 'diamond11' : 10, 'diamond12' : 10 , 'diamond13' : 10, 'club1' : 1, 'club2' : 2, 'club3' : 3, 'club4' : 4, 'club5' : 5, 'club6' : 6, 'club7' : 7, 'club8' : 8, 'club9' : 9, 'club10' : 10, 'club11' : 10, 'club12' : 10, 'club13' : 10}
    
        basicFont = pygame.font.SysFont(None, 30)
        text1 = basicFont.render(" Your point is ", True, BLACK, WHITE)
        text1Rect = text1.get_rect()
        text1Rect.centerx = 450
        text1Rect.centery = 200
        windowSurface.blit(text1, text1Rect)
        pygame.display.update()
        
    
        basicFont = pygame.font.SysFont(None, 30)
        text2 = basicFont.render( str(add_allp(P))  , True, BLACK, WHITE)   
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
        text4 = basicFont.render( str(add_allc(C))  , True, BLACK, WHITE)
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
        text6 = basicFont.render(' Congratulations, you win! ' , True, BLACK, RED)
        text6Rect = text6.get_rect()
        text6Rect.centerx = 450
        text6Rect.centery = 500
            
        if add_allp(P) >21:
            windowSurface.blit(text5, text5Rect)
            pygame.display.update()
        elif add_allc(C) >= add_allp(P):
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
    
        windowSurface.fill(BLACK)
        pygame.display.update()
        
        back_ground_image= r'D:\PySDL2-0.9.2\images.jpg'
        background=pygame.image.load(back_ground_image).convert()
        windowSurface.blit(background, (0,0))
        pygame.display.update()
        

    #basicFont = pygame.font.SysFont(None, 50)
    #text1= basicFont.render('Do you want to play again? Y/N', True, BLACK, YELLOW)
    #text1Rect = text1.get_rect()
    #text1Rect.centerx = 500
    #text1Rect.centery = 300
    #windowSurface.blit(text1, text1Rect)
    #pygame.display.update()

        for event in pygame.event.get():
            basicFont = pygame.font.SysFont(None, 50)
            text1= basicFont.render(' Do you want to play again? Y/N ', True, BLACK, YELLOW)
            text1Rect = text1.get_rect()
            text1Rect.centerx = 500
            text1Rect.centery = 300
            windowSurface.blit(text1, text1Rect)
            pygame.display.update()
    
            if event.type == KEYDOWN:
                if event.key == ord('N'):
                    R=False

                

#basicFont = pygame.font.SysFont(None, 30)
#text2 = basicFont.render( , True, BLACK, WHITE)
#text2Rect = text2.get_rect()
#text2Rect.centerx = 590
#text2Rect.centery = 300
#windowSurface.blit(text2, text2Rect)
#pygame.display.update()

    

#run the game loop
back_ground_image= r'D:\PySDL2-0.9.2\images.jpg'
background=pygame.image.load(back_ground_image).convert()
windowSurface.blit(background, (0,0))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

