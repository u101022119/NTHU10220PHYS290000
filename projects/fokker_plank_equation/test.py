"""
 Show how to use a sprite backed by a graphic.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame,time,random
from pygame.locals import *
import sys, time
 

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (0 ,0,255)
 
pygame.init()
 

size = (1250, 621)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Turtle Game")
all_sprites_list = pygame.sprite.Group()
 

block_list = pygame.sprite.Group()
block1_list = pygame.sprite.Group()


 

bullet_list = pygame.sprite.Group()
bullet1_list= pygame.sprite.Group()

aplus_list = pygame.sprite.Group()

 

done = False
display_instructions = True
font = pygame.font.Font(None, 86)
instruction_page=1

clock = pygame.time.Clock()
background_image = pygame.image.load("background.png").convert()



momo_image=pygame.image.load("momo.png").convert()
lin_image=pygame.image.load("lin.png").convert()
bullet_image=pygame.image.load("bullet.png").convert()
momo_image.set_colorkey(WHITE)
lin_image.set_colorkey(WHITE)
bullet_image.set_colorkey(WHITE)
zombie_image=pygame.image.load("zombie.png").convert()
zombie_image.set_colorkey(WHITE)
zombie1_image=pygame.image.load("zombie1.png").convert()
zombie1_image.set_colorkey(WHITE)
aplus_image=pygame.image.load("aplus.png").convert()
aplus_image.set_colorkey(WHITE)
hsu_image=pygame.image.load("hsu.png").convert()
hsu_image.set_colorkey(WHITE)
hsu1_image=pygame.image.load("hsu1.png").convert()
hsu1_image.set_colorkey(WHITE)
star_image=pygame.image.load("star.png").convert()
instruction_image=pygame.image.load("instruction.png").convert()
gameover_image=pygame.image.load("gameover.png").convert()
victory_image=pygame.image.load("victory.png").convert()
class Zombie(pygame.sprite.Sprite):
    """ This class represents the block. """
    def __init__(self, color):
        
        pygame.sprite.Sprite.__init__(self)
        self.image = zombie_image
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.x -= 0.8
class Zombie1(pygame.sprite.Sprite):
    """ This class represents the block. """
    def __init__(self, color):
        
        pygame.sprite.Sprite.__init__(self)
        self.image = zombie1_image
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.x -= 0.8
class Aplus(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = aplus_image
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.x -=0
                                        
        
        
 

class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
 
        self.image = bullet_image
        
 
        self.rect = self.image.get_rect()
 
    def update(self):
        """ Move the bullet. """
        self.rect.x += 3
class Bullet1(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
 
        self.image = pygame.Surface([10, 10])
        self.image.fill(RED)
 
        self.rect = self.image.get_rect()
 
    def update(self):
        """ Move the bullet. """
        self.rect.x += 3
    
all_image = [ [ ( 0, 0 ), momo_image ],
              [ ( 200, 0 ), lin_image ],
              [ ( 400, 0 ), hsu_image ],
              [ ( 570, 0 ), hsu1_image ],
              [ ( 800, 0 ), None ],
              [ ( 1000, 0 ), None ] ]

blocks = [ [ ( 0, 209 ), None ], [ ( 188, 209 ), None ],  [ ( 386, 209 ), None ],[ ( 584, 209 ), None ], [ ( 0, 418 ), None ],[ ( 188, 418 ), None ],[ ( 386, 418 ), None ],[ ( 584, 418 ), None ] ]
momo=[[ ( 0, 209 ), None ], [ ( 188, 209 ), None ], [ ( 386, 209 ), None ],[ ( 564, 209 ), None ], [ ( 0, 418 ), None ],[ ( 188, 418 ), None ],[ ( 376, 418 ), None ],[ ( 564, 418 ), None ]]
#lins=[[(0,209),None],[ ( 188, 209 ), None ], [ ( 376, 209 ), None ],[ ( 564, 209 ), None ], [ ( 0, 418 ), None ],[ ( 188, 418 ), None ],[ ( 376, 418 ), None ],[ ( 564, 418 ), None ]]
aplus=[[(10,269),None],[(198,269),None],[(386,269),None],[(574,269),None],[(10,478),None],[(198,478),None],[(396,478),None],[(594,478),None]]

mouseHasImage = None
k=0
q=125
for i in range(10):
    if i<=10:
        asd=random.randrange(0,10000)
        if asd%2==0:
            block = Zombie(BLACK)
            block.life = 5
        else:
            block=Zombie1(BLACK)
            block.life=5
        block.rect.x = 2250+i*400
        
        tmp = random.randrange(0,10000)
        if tmp%2==0:
            block.rect.y=210
            
        else:
            block.rect.y=400
            
 
    
        block_list.add(block)
        
        
        all_sprites_list.add(block)
for j in range (10):
    asd=random.randrange(0,10000)
    if asd%2==0:
            
        
            
    
            block = Zombie(BLACK)
        
            block.life = 10
    else:
            block=Zombie1(BLACK)
            block.life=10
    
 
    block.rect.x = 2250+(j+14)*300
    
    tmp = random.randrange(0,10000)
    if tmp%2==0:
        block.rect.y=210
        
    else:
        block.rect.y=400
        
 
    
    block_list.add(block)
    
    all_sprites_list.add(block)
for m in range (10):
    asd=random.randrange(0,10000)
    if asd%2==0:
            
        
            
    
            block = Zombie(BLACK)
        
            block.life = 20
    else:
            block=Zombie1(BLACK)
            block.life=20
    
 
    block.rect.x = 2250+(m+36)*200
    
    tmp = random.randrange(0,10000)
    if tmp%2==0:
        block.rect.y=210
        
    else:
        block.rect.y=400
        
 
    
    block_list.add(block)
    
    all_sprites_list.add(block)
for r in range (20):
    asd=random.randrange(0,10000)
    if asd%2==0:
            
        
            
    
        block = Zombie(BLACK)
        
        block.life = 30
    else:
        block=Zombie1(BLACK)
        block.life=30
    
 
    block.rect.x = 2250+(r+92)*100
    
    tmp = random.randrange(0,10000)
    if tmp%2==0:
        block.rect.y=210
        
    else:
        block.rect.y=400
        
 
    
    block_list.add(block)
    
    all_sprites_list.add(block)
for t in range (50):
    asd=random.randrange(0,10000)
    if asd%2==0:
            
        
            
    
            block = Zombie(BLACK)
        
            block.life = 40
    else:
            block=Zombie1(BLACK)
            block.life=40
    
 
    block.rect.x = 2250+(t+224)*50
    
    tmp = random.randrange(0,10000)
    if tmp%2==0:
        block.rect.y=210
        
    else:
        block.rect.y=400
        
 
    
    block_list.add(block)
    
    all_sprites_list.add(block)
for y in range (400):
    asd=random.randrange(0,10000)
    if asd%2==0:
            
        
            
    
        block = Zombie(BLACK)
        
        block.life = 60
    else:
        block=Zombie1(BLACK)
        block.life=60
    block.rect.x=2250+(y+548)*25
    tmp=random.randrange(0,10000)
    if tmp%2==0:
        block.rect.y=210
    else:
        block.rect.y=400
    


while done==False  and display_instructions:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            done=True 
        if event.type == pygame.MOUSEBUTTONDOWN:
            instruction_page += 1
            if instruction_page == 3:
                display_instructions = False
    screen.fill(BLACK)

    if instruction_page==1:
        
        screen.blit(star_image,[0,0])
    
    if instruction_page==2:
        
        screen.blit(instruction_image,[0,0])



    pygame.display.flip()

pygame.mixer.music.load('1.mp3')
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
pygame.mixer.music.play()
game_over = False


    
        
        

    

        

while not done:
    
    
    

    
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
        if event.type == pygame.MOUSEBUTTONDOWN:
           
            mousepos = pygame.mouse.get_pos()
            if mouseHasImage:
                if mouseHasImage==momo_image:
                    for i in range(4):
                        j=i+4
                        if ( mousepos[0] in range( blocks[ i ][ 0 ][ 0 ], blocks[ i ][ 0 ][ 0 ] + 200 ) ) and ( mousepos[1] in range( blocks[ 0 ][ 0 ][ 1 ], blocks[ 0 ][ 0 ][ 1 ] + 200 ) ):
                            print 1
                            blocks[ i ][ 1 ] = mouseHasImage
                            momo[i][1]=1
                            mouseHasImage = None
                        elif ( mousepos[0] in range( blocks[ i ][ 0 ][ 0 ], blocks[ i ][ 0 ][ 0 ] + 200 ) ) and ( mousepos[1] in range( 418,627 ) ):
                            blocks[  j][ 1 ] = mouseHasImage
                            momo[j][1]=1
                            mouseHasImage = None

                
                if mouseHasImage==lin_image:
                    for i in range (4):
                        
                         if ( mousepos[0] in range( blocks[ i ][ 0 ][ 0 ], blocks[ i ][ 0 ][ 0 ] + 200 ) ) and ( mousepos[1] in range( blocks[ 0 ][ 0 ][ 1 ], blocks[ 0 ][ 0 ][ 1 ] + 200 ) ):
                             blocks[ i ][ 1 ] = mouseHasImage
                             momo[i][1]=2
                             mouseHasImage = None
                         elif ( mousepos[0] in range( blocks[ i ][ 0 ][ 0 ], blocks[ i ][ 0 ][ 0 ] + 200 ) ) and ( mousepos[1] in range( 481,627 ) ):
                             j=i+4
                             blocks[ j ][ 1 ] = mouseHasImage
                             momo[j][1]=2
                             mouseHasImage = None
                if mouseHasImage==hsu_image:
                    for i in range (4):
                        
                         if ( mousepos[0] in range( blocks[ i ][ 0 ][ 0 ], blocks[ i ][ 0 ][ 0 ] + 200 ) ) and ( mousepos[1] in range( blocks[ 0 ][ 0 ][ 1 ], blocks[ 0 ][ 0 ][ 1 ] + 200 ) ):
                             blocks[ i ][ 1 ] = mouseHasImage
                             momo[i][1]=3
                             mouseHasImage = None
                         elif ( mousepos[0] in range( blocks[ i ][ 0 ][ 0 ], blocks[ i ][ 0 ][ 0 ] + 200 ) ) and ( mousepos[1] in range( 481,627 ) ):
                             j=i+4
                             blocks[ j ][ 1 ] = mouseHasImage
                             momo[j][1]=3
                             mouseHasImage = None
                if mouseHasImage==hsu1_image:
                    for i in range (4):
                        
                         if ( mousepos[0] in range( blocks[ i ][ 0 ][ 0 ], blocks[ i ][ 0 ][ 0 ] + 200 ) ) and ( mousepos[1] in range( blocks[ 0 ][ 0 ][ 1 ], blocks[ 0 ][ 0 ][ 1 ] + 200 ) ):
                             blocks[ i ][ 1 ] = mouseHasImage
                             momo[i][1]=4
                             mouseHasImage = None
                         elif ( mousepos[0] in range( blocks[ i ][ 0 ][ 0 ], blocks[ i ][ 0 ][ 0 ] + 200 ) ) and ( mousepos[1] in range( 481,627 ) ):
                             j=i+4
                             blocks[ j ][ 1 ] = mouseHasImage
                             momo[j][1]=4
                             mouseHasImage = None
                         
            else:
                
                if ( mousepos[0] in range( all_image[ 0 ][ 0 ][ 0 ], all_image[ 0 ][ 0 ][ 0 ] + 200 ) ) and ( mousepos[1] in range( all_image[ 0 ][ 0 ][ 1 ], all_image[ 0 ][ 0 ][ 1 ] + 200 ) )and q>=6:
                    mouseHasImage=momo_image
                    q-=6
                    
                    
                if ( mousepos[0] in range( all_image[ 1 ][ 0 ][ 0 ], all_image[ 1 ][ 0 ][ 0 ] + 200 ) ) and ( mousepos[1] in range( all_image[ 1][ 0 ][ 1 ], all_image[ 1][ 0 ][ 1 ] + 200 ) )and q>=3:
                    mouseHasImage=lin_image
                    q-=3

                if ( mousepos[0] in range( all_image[ 2 ][ 0 ][ 0 ], all_image[ 2 ][ 0 ][ 0 ] + 200 ) ) and ( mousepos[1] in range( all_image[ 2][ 0 ][ 1 ], all_image[ 2][ 0 ][ 1 ] + 200 ) )and q>=12:
                    print 1
                    mouseHasImage=hsu_image
                    q-=12
                if ( mousepos[0] in range( all_image[ 3 ][ 0 ][ 0 ], all_image[ 3 ][ 0 ][ 0 ] + 200 ) ) and ( mousepos[1] in range( all_image[ 3][ 0 ][ 1 ], all_image[ 3][ 0 ][ 1 ] + 200 ) )and q>=25:
                    mouseHasImage=hsu1_image
                    q-=25
        if event.type==KEYUP:
                
              if event.key==ord('f'):
                  
                  for i in range(8):
                      if aplus[i][1]:
                          q+=3
                          aplus[i][1]=None
                          print q
              if event.key==ord('s'):
                  print q
              
            
                             
                
    
    screen.blit(background_image, [0, 0])
    for i in range(4):
        screen.blit( all_image[ i ][ 1 ], all_image[ i ][ 0 ] )
    mousepos=pygame.mouse.get_pos()
    
    if mouseHasImage:
        screen.blit( mouseHasImage, mousepos )
    
    for block in blocks:
        if block[ 1 ]:
            screen.blit( block[ 1 ], block[ 0 ] )
    for aplu in aplus:
        if aplu[1]:
            screen.blit( aplu[ 1 ], aplu[ 0 ] )
            
            
    
            
        
    
    k += 1
    for i in range(8):
        
        if k % 100 == 0 and momo[i][1]==1:
        
            bullet = Bullet()
        
            bullet.rect.x =momo[i][0][0]+188
            bullet.rect.y = momo[i][0][1]+30
        
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)
   

        if momo[i][1]==2 and k % 550 == 0:
            aplus[i][1]=aplus_image
        if momo[i][1]==3 and k%50==0:
            bullet = Bullet()
        
            bullet.rect.x =momo[i][0][0]+188
            bullet.rect.y = momo[i][0][1]+30
        
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)
        if momo[i][1]==4 and k%15==0:
            bullet = Bullet()
        
            bullet.rect.x =momo[i][0][0]+188
            bullet.rect.y = momo[i][0][1]+30
        
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)
            
            
            
            
            
            
            
        
            

    
   
    for bullet in bullet_list:
        
        block_hit_list= pygame.sprite.spritecollide(bullet, block_list, None)
        
    
        
        
        
        
        
        for block in block_hit_list:
            block.life = block.life - 1
            
            
            
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            if block.life <= 0:
              
                q+=0
                
                block_list.remove(block)
                all_sprites_list.remove(block)
        
                
              
        if bullet_list:
            if bullet.rect.x > 1250:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
    
            
    all_sprites_list.update()
    all_sprites_list.draw(screen)
    money=q
    text=font.render(str(q),True,WHITE)
    screen.blit(text,[865,60])
    if q>=128:
        screen.blit(victory_image,[0,0])
        
        
        
    for block in block_list:
        if block.rect.x==0:
            game_over=True
    if game_over and q<128:
        
        
        screen.blit(gameover_image, [0, 0])
        
            
    
                     
                     
        
    
    
 
    
    pygame.display.flip()
 
    
    clock.tick(60)
 

pygame.quit()
