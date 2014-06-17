
import pygame
from pygame.locals import *
from sys import exit
import random
from time import *



def backgroundmusic():
    pygame.mixer.music.load('bee.mp3')
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(0.25)
    
def music(music_type):
    fart = pygame.mixer.Sound("fart.wav")
    duck = pygame.mixer.Sound("duck.wav")
    thwap = pygame.mixer.Sound("thwap.wav")
    botton = pygame.mixer.Sound("botton.wav")
    total_type=[fart,duck,thwap,botton]
    total_type[music_type].set_volume(0.25)
    total_type[music_type].play()


def selection1():
    
    q=150
    w=q+325
    e=q+650
    r=450
    t=570

    screen=pygame.display.set_mode((1200,720),0,32)
    pygame.display.set_caption("Teacher shot")
    
    background_image="play_0.jpg"
    background=pygame.image.load(background_image).convert_alpha()
    
    a=["1_1_1.png","1_2.png","1_3.png","1_4.png"]
    b=["2_1_1.png","2_2.png","2_3.png","2_4.png"]

    
    teacher_image=["pcchen_1.png","kuoan_1.png","mou_1.png"]

    picture=range(4)
    picture2=range(4)
    teacher=range(3)
    
    for j in range(4):
        picture[j]=pygame.image.load(a[j]).convert_alpha()
        picture2[j]=pygame.image.load(b[j]).convert_alpha()
    for j in range(3):
        teacher[j]=pygame.image.load(teacher_image[j]).convert_alpha()
    

    i=0
    screen.blit(background, (0,0))
    screen.blit(picture2[0], (q,r))
    screen.blit(picture2[1], (w,r))
    screen.blit(picture2[2], (e,r))
    screen.blit(picture2[3], (w,t))
    for j in range(3):
        screen.blit(teacher[j], (q+325*j,175))
        
    while True:               
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_LEFT and i !=1 and i!=0 :
                    music(3)
                    i=i-1
                elif event.key == K_RIGHT and i !=4:
                    music(3)
                    i=i+1                
                elif event.key == K_ESCAPE:
                    music(3)
                    pygame.quit()
                    exit()
                elif event.key == K_SPACE and (i==1 or i==2 or i==3 or i==4 ):
                    music(3)
                    if i!=4:
                        game_start(i) 
                    else:
                        pygame.quit()
                        exit()
                else:
                    music(0)
                while i==1:
                    screen.blit(picture[0], (q,r))
                    screen.blit(picture2[1], (w,r))
                    screen.blit(picture2[2], (e,r))
                    screen.blit(picture2[3], (w,t))
                    break
                while i ==2:
                    screen.blit(picture2[0], (q,r))
                    screen.blit(picture[1], (w,r))
                    screen.blit(picture2[2], (e,r))
                    screen.blit(picture2[3], (w,t))
                    break
                while i ==3:
                    screen.blit(picture2[0], (q,r))
                    screen.blit(picture2[1], (w,r))
                    screen.blit(picture[2], (e,r))
                    screen.blit(picture2[3], (w,t))
                    break
                while i ==4:
                    screen.blit(picture2[0], (q,r))
                    screen.blit(picture2[1], (w,r))
                    screen.blit(picture2[2], (e,r))
                    screen.blit(picture[3], (w,t))
                    break      
        pygame.display.update()


def count(screen):
    cnt=range(3)
    cnt_image=['cnt_1.jpg','cnt_2.jpg','cnt_3.jpg']
    for i in range(3):
        cnt[i]=pygame.image.load(cnt_image[i]).convert_alpha()
    for i in range(3):
        screen.blit(cnt[-i-1],(450,210))
        pygame.display.update()
        sleep(1)

def game_start(level):
    background_image="play_1.jpg"
    if level==1:
        teacher_image="pcchen.png"
    elif level==2:
        teacher_image="kuoan.png"
    elif  level==3:
        teacher_image="mou.png"
    else:
        teacher_image=""
    
    screen=pygame.display.set_mode((1200,720),0,32)
    pygame.display.set_caption("Teacher shot")
    
    target=range(9)
    time=range(10)
    
    name_0=['1.png','2.png','3.png','4.png','5.png','6.png','7.png','8.png','9.png']
    name_1=['0_1.png','1_1.png','2_1.png','3_1.png','4_1.png','5_1.png','6_1.png','7_1.png','8_1.png','9_1.png']

    background=pygame.image.load(background_image).convert_alpha()
    teacher=pygame.image.load(teacher_image).convert_alpha()
    
    for i in range(9):
        target[i]=pygame.image.load(name_0[i]).convert_alpha()
    for i in range(10):
        time[i]=pygame.image.load(name_1[i]).convert_alpha()
    
    key_0={ 1:K_1 , 2:K_2 , 3:K_3 , 4:K_4 , 5:K_5 , 6:K_6 , 7:K_7 , 8:K_8 , 9:K_9 }
    key_1={ 1:257 , 2:258 , 3:259 , 4:260 , 5:261 , 6:262 , 7:263 , 8:264 , 9:265 }

    num=7
    x=range(num)
    
    dx=120
    dy=85
    local=[600-85/2-120,600-103-120*2,600-85/2-120*4]

    score=0
    
    count(screen)

    time_init=pygame.time.get_ticks()
    
    for i in range(num):
        x[i]=random.randint(1,3*level)
        
    while True:
        screen.blit(background,(0,0))
        
        for i in range(num):
            screen.blit(teacher,(local[level-1]+dx*(x[i]-1),dy*i))
        for i in range(3*level):
            screen.blit(target[i],(local[level-1]+dx*i,dy*7))

        time_remain=pygame.time.get_ticks()-time_init
        
        ten=time_remain/10000
        one=time_remain/1000-10*ten
        
        screen.blit(time[ten],(1130,0))
        screen.blit(time[one],(1165,0))
        
        pygame.display.update()
        
        if time_remain>30000:
            sleep(3)
            evaluation(level,score)
        
        for event in pygame.event.get():
            if event.type==KEYDOWN:
                if event.key==key_0[x[num-1]] or event.key==key_1[x[num-1]]:
                    music(2)
                    for i in range(1,num):
                        x[-i]=x[-i-1]
                    x[0]=random.randint(1,3*level)
                    score+=1
                else:
                    music(1)
            if event.type==QUIT or (event.type==KEYDOWN and event.key==27):
                pygame.quit()
                exit()

def evaluation(level,score):
    screen_size = (1200, 720)
    background_image = "play_1.jpg"
    table_image="table.png"
    teacher_image=["pcchen_2.png","kuoan_2.png","mou_2.png"]
    ev=["e0.png","e1.png","e2.png","e3.png","e4.png","e5.png","e6.png","e7.png","e8.png","e9.png","e10.png"]

    ti=range(10)
    name=['0_1.png','1_1.png','2_1.png','3_1.png','4_1.png','5_1.png','6_1.png','7_1.png','8_1.png','9_1.png']

    for i in range(10):
        ti[i]=pygame.image.load(name[i]).convert_alpha()

    if score<60:
        k=0
    elif score<120:
        k=1
    else:
        k=2

    screen = pygame.display.set_mode(screen_size, 0, 32)
    background = pygame.image.load(background_image).convert_alpha()
    table=pygame.image.load(table_image).convert_alpha()
    
    ev_state=pygame.image.load(ev[0]).convert_alpha()
    ev_i = pygame.image.load(ev[(level+3*k)]).convert_alpha()
    ev_final=pygame.image.load(ev[10]).convert_alpha()
        
    teacher=pygame.image.load(teacher_image[level-1]).convert_alpha()

    screen.blit(background, (0, 0))
                             
    
    screen.blit(teacher, (150, 250))
    screen.blit(table, (20, 520))
    screen.blit(ev_state, (500, 150))
    pygame.display.update()
    sleep(3)

    hun=score/100 
    ten=(score-hun*100)/10 
    one=score-100*hun-10*ten
    
    screen.blit(ti[hun],(720,240))                       
    screen.blit(ti[ten],(755,240))
    screen.blit(ti[one],(790,240))
    pygame.display.update()

    sleep(1)
    
    screen.blit(ev_i, (500, 150))
    pygame.display.update()
    
    sleep(1)
    
    screen.blit(ev_final, (500, 150))    
    pygame.display.update()
    
    sleep(1)

    selection2(level)




def selection2(level):

    w=475

    screen=pygame.display.set_mode((1200,720),0,32)
    pygame.display.set_caption("Teacher shot")
    
    background_image = "play_0.jpg"
    background = pygame.image.load(background_image).convert_alpha()
    
    a=["1_5.png","1_6.png","1_7.png"]
    b=["2_5.png","2_6.png","2_7.png"]

    picture=range(3)
    picture2=range(3)

    for j in range(3):
        picture[j]=pygame.image.load(a[j]).convert_alpha()
        picture2[j]=pygame.image.load(b[j]).convert_alpha()
        
    w=450  
    i=0
    screen.blit(background, (0,0))
    screen.blit(picture2[0], (w,150))
    screen.blit(picture2[1], (w,300))
    screen.blit(picture2[2], (w,450))
    
    while True:        
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_UP and i !=1 and i!=0 :
                    music(3)
                    i=i-1                    
                elif event.key == K_DOWN and i !=3:
                    music(3)
                    i=i+1
                elif event.key == K_ESCAPE:
                    music(3)
                    pygame.quit()
                    exit()
                elif event.key == K_SPACE and (i==1 or i==2 or i==3):
                    music(3)
                    if i==1:
                        selection1()
                    elif i==2:
                        game_start(level)
                    elif i==3:
                        pygame.quit()
                        exit()
                else:
                    music(0)
                
                while i==1:
                    screen.blit(picture[0], (w,150))
                    screen.blit(picture2[1], (w,300))
                    screen.blit(picture2[2], (w,450))
                    break
                while i ==2:
                    screen.blit(picture2[0], (w,150))
                    screen.blit(picture[1], (w,300))
                    screen.blit(picture2[2], (w,450))
                    break
                while i ==3:
                    screen.blit(picture2[0], (w,150))
                    screen.blit(picture2[1], (w,300))
                    screen.blit(picture[2], (w,450))
                    break        
        pygame.display.update()



    
if __name__=="__main__":
    pygame.init()
    pygame.mixer.init()
    backgroundmusic()
    selection1()
