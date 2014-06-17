import math , pygame , sys , numpy 
from pygame.locals import *
from random import *
from copy import *


#set up the colors
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)



WINDOWWIDTH =880       #size of window's width in pixels
WINDOWHEIGHT = 440     #size of window's height in pixels
BOXSIZE = 40           #size of the box height & width in pixels
GAPSIZE = 0            #size of the gap between boxes in pixels
BLOCKSIZE =40          #number of the columns of icons
mousex=0
mousey=0

class Rectangle(object):
    """block"""
    def __init__(self,x,y):
        self.x=20+x*40
        self.y=20+y*40
    def color(self,t):
        self.red=choice(t)
        self.green=choice(t)
class Block(object):
    """block"""
class BlockColor(object):
    """the block's color"""

def ConstructBlockArray(s):
    t=[]
    for i in range(10):
        r=s[10*i:10*i+10]
        t.append(r)
    return t

def BLOCKARRAYDETAIL(s,t):
    u=[]
    x=0
    y=0
    while x <10:
        while y <10:
            BLOCK=Rectangle(x,y)
            BLOCK.color(t)
            r=[BLOCK.x,BLOCK.y,BLOCK.red,BLOCK.green]
            v=[BLOCK.red,BLOCK.green]
            if v in u:
                y+=0
            else:
                u.append(v)
                s.append(r)
                y+=1
        y=0
        x+=1
    return s

def ANSWER(t):
    s=[]
    for i in range(10):
        for j in range(10):
            box=Block()
            box.x=900+i*40
            box.y=20+j*40
            box.color=BlockColor()
            box.color.red=t[i]
            box.color.green=t[j]
            r=[box.x,box.y,box.color.red,box.color.green]
            s.append(r)
    return s
            
def DRAWBLOCKARRAY(s):
    for i in range(10):
        for j in range(10):
            pygame.draw.rect(windowSurface,(s[i][j][2],s[i][j][3],0),(s[i][j][0],s[i][j][1],BLOCKSIZE,BLOCKSIZE)) 


def GenerateSelectedBoxData(val):
    SelectedBox=[]
    for i in range(10):
        SelectedBox.append([val]*10)
    return SelectedBox

def leftTopCoordsOfBox(boxx, boxy):
    # Convert board coordinates to pixel coordinates
    left = boxx * BLOCKSIZE + 20
    top = boxy * BLOCKSIZE + 20
    return (left, top)


def getBoxAtPixel(x, y):
    for boxx in range(10):
        for boxy in range(10):
            left, top = leftTopCoordsOfBox(boxx, boxy)
            boxRect = pygame.Rect(left, top, BOXSIZE, BOXSIZE)
            if boxRect.collidepoint(x, y):
                return (boxx, boxy)
    return (None, None)

        
def INTO2DLIST(s):
    h=[]
    for i in range(10):
        for j in range(10):
            h.append([s[i][j][2],s[i][j][3]])
    return h

def countscore(s,s2):
    score=0
    t=INTO2DLIST(s)
    t2=INTO2DLIST(s2)
    for i in range(100):
        for j in range(100):
            if (t[i][0],t[i][1])==(t2[j][0],t2[j][1])  and i==j:
                score+=0
            elif (t[i][0],t[i][1])==(t2[j][0],t2[j][1]) and i!=j:
                score+=math.fabs(i-j)
    return score
                        
def drawblock(blocks):
    for block in blocks:
        left, top = leftTopCoordsOfBox(block[0], block[1])
        pygame.draw.rect(windowSurface,(block[2],block[3],0), (left, top, BLOCKSIZE, BLOCKSIZE))

def PRINTRETRYFONT():
    basicFont = pygame.font.SysFont(None,48)
    retrytext=basicFont.render('press r if you want to retry',True,RED,BLUE)
    retrytextRect = retrytext.get_rect()
    retrytextRect.centerx = windowSurface.get_rect().centerx
    retrytextRect.centery = windowSurface.get_rect().centery+160
    windowSurface.blit(retrytext,retrytextRect)    
    
#set pygame
pygame.init()

#set up the window pygame.display.set_mode((width,height)

windowSurface=pygame.display.set_mode((1320,440))

pygame.display.set_caption('Game_of_ColorSorting')

SelectedBox=GenerateSelectedBoxData(False)

#gamemode
easy=range(0,250,25)
normal=range(100,200,10)
hard=range(150,200,5)
crazy=range(150,180,3)
WTH=range(150,160,1)

#globalstate set
menu=True
retry=False
play=False
mode1=False
mode2=False
mode3=False
mode4=False
mode5=False
mousex=0
mousey=0
k=0
(x1,y1) = (None,None)
(x2,y2) = (None,None)
#easystate set
s1=[]
s1=BLOCKARRAYDETAIL(s1,easy)
s1=ConstructBlockArray(s1)
s12=ANSWER(easy)
s12=ConstructBlockArray(s12)
score1=0
#normalstate set
s2=[]
s2=BLOCKARRAYDETAIL(s2,normal)
s2=ConstructBlockArray(s2)
s22=ANSWER(normal)
s22=ConstructBlockArray(s22)
score2=0
#hardstate set
s3=[]
s3=BLOCKARRAYDETAIL(s3,hard)
s3=ConstructBlockArray(s3)
s32=ANSWER(hard)
s32=ConstructBlockArray(s32)
score3=0
#crazystate set
s4=[]
s4=BLOCKARRAYDETAIL(s4,crazy)
s4=ConstructBlockArray(s4)
s42=ANSWER(crazy)
s42=ConstructBlockArray(s42)
score4=0
#WTHstate set
s5=[]
s5=BLOCKARRAYDETAIL(s5,WTH)
s5=ConstructBlockArray(s5)
s52=ANSWER(WTH)
s52=ConstructBlockArray(s52)
score5=0



#set up gamemode fonts
while True:
    
    windowSurface=pygame.display.set_mode((1320,440))
    windowSurface.fill((180,45,100))
    pygame.display.update()


    basicFont = pygame.font.SysFont(None,72)


    for i in range(25):
        pygame.draw.rect(windowSurface,(10*i,255,0),(160+40*i,120,40,200)) 

        

    easytext=basicFont.render('-easy-',True,WHITE,BLUE)
    easytextRect = easytext.get_rect()
    easytextRect.centerx = windowSurface.get_rect().centerx-360
    easytextRect.centery = windowSurface.get_rect().centery-160

    normaltext=basicFont.render('-normal-',True,WHITE,BLUE)
    normaltextRect = normaltext.get_rect()
    normaltextRect.centerx = windowSurface.get_rect().centerx-180
    normaltextRect.centery = windowSurface.get_rect().centery-160

    hardtext=basicFont.render('-hard-',True,WHITE,BLUE)
    hardtextRect = hardtext.get_rect()
    hardtextRect.centerx = windowSurface.get_rect().centerx
    hardtextRect.centery = windowSurface.get_rect().centery-160

    crazytext=basicFont.render('-crazy-',True,WHITE,BLUE)
    crazytextRect = crazytext.get_rect()
    crazytextRect.centerx = windowSurface.get_rect().centerx+180
    crazytextRect.centery = windowSurface.get_rect().centery-160

    WTHtext=basicFont.render('-WTH-',True,WHITE,BLUE)
    WTHtextRect = WTHtext.get_rect()
    WTHtextRect.centerx = windowSurface.get_rect().centerx+360
    WTHtextRect.centery = windowSurface.get_rect().centery-160

    windowSurface.blit(easytext,easytextRect)
    windowSurface.blit(normaltext,normaltextRect)
    windowSurface.blit(hardtext,hardtextRect)
    windowSurface.blit(crazytext,crazytextRect)
    windowSurface.blit(WTHtext,WTHtextRect)
    pygame.display.update()
    menu=True
    retry=False
    play=False
    mode1=False
    mode2=False
    mode3=False
    mode4=False
    mode5=False
    retry=False

    while not retry:   #main game loop 
        for event in pygame.event.get():
            mouseClicked = False
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex,mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex,mousey = event.pos
                mouseClicked = True
            elif event.type == KEYUP and event.key == K_r:
                retry=True
        #easymode
        boxx,boxy = getBoxAtPixel(mousex,mousey)
        if easytextRect.collidepoint((mousex,mousey))==True and menu ==True and mouseClicked:
            menu=False
            mode1=True
            play=True

        elif  mode1 == True and menu==False:
            windowSurface.fill(WHITE)
            DRAWBLOCKARRAY(s1)
            DRAWBLOCKARRAY(s12)
            #finish button
            PRINTRETRYFONT()
            finishtext=basicFont.render('-finish-',True,WHITE,BLUE)
            finishtextRect = finishtext.get_rect()
            finishtextRect.centerx = 660
            finishtextRect.centery = windowSurface.get_rect().centery
            windowSurface.blit(finishtext,finishtextRect)
            if boxx!=None and boxy!=None and play==True:
                if not SelectedBox[boxx][boxy] and mouseClicked:
                    SelectedBox[boxx][boxy]=True
                    if (x1,y1) == (None,None) and (x2,y2) == (None,None) and finishtextRect.collidepoint(mousex,mousey)==False:
                        (x1,y1)=(boxx,boxy)
                        mouseClicked=False
                    elif (x1,y1) != (None,None) and (x2,y2) == (None,None) and finishtextRect.collidepoint(mousex,mousey)==False:
                        (x2,y2)=(boxx,boxy)
                        (X1,Y1)=(s1[x1][y1][2],s1[x1][y1][3])    #(x1,y1)is pixel while (X1,Y1)is not 
                        (X2,Y2)=(s1[x2][y2][2],s1[x2][y2][3])    #(x2,y2)is pixel while (X2,Y2)is not
                        (s1[x1][y1][2],s1[x1][y1][3])=(X2,Y2)
                        (s1[x2][y2][2],s1[x2][y2][3])=(X1,Y1)
                        drawblock([s1[x1][y1],s1[x2][y2]])
                        pygame.display.update()
                        SelectedBox[x1][y1]=False
                        SelectedBox[x2][y2]=False
                        mouseClicked=False
                        (x1,y1) = (None,None)
                        (x2,y2) = (None,None)
            elif  finishtextRect.collidepoint(mousex,mousey)==True and mouseClicked and play==True:
                play=False
                score1=countscore(s1,s12)
            elif play==False:
                scoreFont=pygame.font.SysFont(None,220)
                scoretext=scoreFont.render(str(score1),True,BLUE,WHITE)
                scoretextRect=scoretext.get_rect()
                scoretextRect.centerx = windowSurface.get_rect().centerx
                scoretextRect.centery = windowSurface.get_rect().centery
                windowSurface.blit(scoretext,scoretextRect)
                    
                                       


        #normalmode
        boxx,boxy = getBoxAtPixel(mousex,mousey)
        if normaltextRect.collidepoint((mousex,mousey))==True and menu ==True and mouseClicked:
            menu=False
            mode2=True
            play=True

        elif  mode2 == True and menu==False:
            windowSurface.fill(WHITE)
            DRAWBLOCKARRAY(s2)
            DRAWBLOCKARRAY(s22)
            #finish button
            PRINTRETRYFONT()
            finishtext=basicFont.render('-finish-',True,WHITE,BLUE)
            finishtextRect = finishtext.get_rect()
            finishtextRect.centerx = 660
            finishtextRect.centery = windowSurface.get_rect().centery
            windowSurface.blit(finishtext,finishtextRect)
            if boxx!=None and boxy!=None and play==True:
                if not SelectedBox[boxx][boxy] and mouseClicked:
                    SelectedBox[boxx][boxy]=True
                    if (x1,y1) == (None,None) and (x2,y2) == (None,None) and finishtextRect.collidepoint(mousex,mousey)==False:
                        (x1,y1)=(boxx,boxy)
                        mouseClicked=False
                    elif (x1,y1) != (None,None) and (x2,y2) == (None,None) and finishtextRect.collidepoint(mousex,mousey)==False:
                        (x2,y2)=(boxx,boxy)
                        (X1,Y1)=(s2[x1][y1][2],s2[x1][y1][3])    #(x1,y1)is pixel while (X1,Y1)is not 
                        (X2,Y2)=(s2[x2][y2][2],s2[x2][y2][3])    #(x2,y2)is pixel while (X2,Y2)is not
                        (s2[x1][y1][2],s2[x1][y1][3])=(X2,Y2)
                        (s2[x2][y2][2],s2[x2][y2][3])=(X1,Y1)
                        drawblock([s2[x1][y1],s2[x2][y2]])
                        pygame.display.update()
                        SelectedBox[x1][y1]=False
                        SelectedBox[x2][y2]=False
                        mouseClicked=False
                        (x1,y1) = (None,None)
                        (x2,y2) = (None,None)
            elif  finishtextRect.collidepoint(mousex,mousey)==True and mouseClicked and play==True:
                play=False
                score2=countscore(s2,s22)
            elif play==False:
                scoreFont=pygame.font.SysFont(None,220)
                scoretext=scoreFont.render(str(score2),True,BLUE,WHITE)
                scoretextRect=scoretext.get_rect()
                scoretextRect.centerx = windowSurface.get_rect().centerx
                scoretextRect.centery = windowSurface.get_rect().centery
                windowSurface.blit(scoretext,scoretextRect)
        
        #hardmode
        boxx,boxy = getBoxAtPixel(mousex,mousey)
        if hardtextRect.collidepoint((mousex,mousey))==True and menu ==True and mouseClicked:
            menu=False
            mode3=True
            play=True

        elif  mode3 == True and menu==False:
            windowSurface.fill(WHITE)
            DRAWBLOCKARRAY(s3)
            DRAWBLOCKARRAY(s32)
            #finish button
            PRINTRETRYFONT()
            finishtext=basicFont.render('-finish-',True,WHITE,BLUE)
            finishtextRect = finishtext.get_rect()
            finishtextRect.centerx = 660
            finishtextRect.centery = windowSurface.get_rect().centery
            windowSurface.blit(finishtext,finishtextRect)
            if boxx!=None and boxy!=None and play==True:
                if not SelectedBox[boxx][boxy] and mouseClicked:
                    SelectedBox[boxx][boxy]=True
                    if (x1,y1) == (None,None) and (x2,y2) == (None,None) and finishtextRect.collidepoint(mousex,mousey)==False:
                        (x1,y1)=(boxx,boxy)
                        mouseClicked=False
                    elif (x1,y1) != (None,None) and (x2,y2) == (None,None) and finishtextRect.collidepoint(mousex,mousey)==False:
                        (x2,y2)=(boxx,boxy)
                        (X1,Y1)=(s3[x1][y1][2],s3[x1][y1][3])    #(x1,y1)is pixel while (X1,Y1)is not 
                        (X2,Y2)=(s3[x2][y2][2],s3[x2][y2][3])    #(x2,y2)is pixel while (X2,Y2)is not
                        (s3[x1][y1][2],s3[x1][y1][3])=(X2,Y2)
                        (s3[x2][y2][2],s3[x2][y2][3])=(X1,Y1)
                        drawblock([s3[x1][y1],s3[x2][y2]])
                        pygame.display.update()
                        SelectedBox[x1][y1]=False
                        SelectedBox[x2][y2]=False
                        mouseClicked=False
                        (x1,y1) = (None,None)
                        (x2,y2) = (None,None)
            elif  finishtextRect.collidepoint(mousex,mousey)==True and mouseClicked and play==True:
                play=False
                score3=countscore(s3,s32)
            elif play==False:
                scoreFont=pygame.font.SysFont(None,220)
                scoretext=scoreFont.render(str(score3),True,BLUE,WHITE)
                scoretextRect=scoretext.get_rect()
                scoretextRect.centerx = windowSurface.get_rect().centerx
                scoretextRect.centery = windowSurface.get_rect().centery
                windowSurface.blit(scoretext,scoretextRect)
        
        #crazymod
        boxx,boxy = getBoxAtPixel(mousex,mousey)
        if crazytextRect.collidepoint((mousex,mousey))==True and menu ==True and mouseClicked:
            menu=False
            mode4=True
            play=True

        elif  mode4 == True and menu==False:
            windowSurface.fill(WHITE)
            DRAWBLOCKARRAY(s4)
            DRAWBLOCKARRAY(s42)
            #finish button
            PRINTRETRYFONT()
            finishtext=basicFont.render('-finish-',True,WHITE,BLUE)
            finishtextRect = finishtext.get_rect()
            finishtextRect.centerx = 660
            finishtextRect.centery = windowSurface.get_rect().centery
            windowSurface.blit(finishtext,finishtextRect)
            if boxx!=None and boxy!=None and play==True:
                if not SelectedBox[boxx][boxy] and mouseClicked:
                    SelectedBox[boxx][boxy]=True
                    if (x1,y1) == (None,None) and (x2,y2) == (None,None) and finishtextRect.collidepoint(mousex,mousey)==False:
                        (x1,y1)=(boxx,boxy)
                        mouseClicked=False
                    elif (x1,y1) != (None,None) and (x2,y2) == (None,None) and finishtextRect.collidepoint(mousex,mousey)==False:
                        (x2,y2)=(boxx,boxy)
                        (X1,Y1)=(s4[x1][y1][2],s4[x1][y1][3])    #(x1,y1)is pixel while (X1,Y1)is not 
                        (X2,Y2)=(s4[x2][y2][2],s4[x2][y2][3])    #(x2,y2)is pixel while (X2,Y2)is not
                        (s4[x1][y1][2],s4[x1][y1][3])=(X2,Y2)
                        (s4[x2][y2][2],s4[x2][y2][3])=(X1,Y1)
                        drawblock([s4[x1][y1],s4[x2][y2]])
                        pygame.display.update()
                        SelectedBox[x1][y1]=False
                        SelectedBox[x2][y2]=False
                        mouseClicked=False
                        (x1,y1) = (None,None)
                        (x2,y2) = (None,None)
            elif  finishtextRect.collidepoint(mousex,mousey)==True and mouseClicked and play==True:
                play=False
                score4=countscore(s4,s42)
            elif play==False:
                scoreFont=pygame.font.SysFont(None,220)
                scoretext=scoreFont.render(str(score4),True,BLUE,WHITE)
                scoretextRect=scoretext.get_rect()
                scoretextRect.centerx = windowSurface.get_rect().centerx
                scoretextRect.centery = windowSurface.get_rect().centery
                windowSurface.blit(scoretext,scoretextRect)
        #WTHmode
        boxx,boxy = getBoxAtPixel(mousex,mousey)
        if WTHtextRect.collidepoint((mousex,mousey))==True and menu ==True and mouseClicked:
            menu=False
            mode5=True
            play=True

        elif  mode5 == True and menu==False:
            windowSurface.fill(WHITE)
            DRAWBLOCKARRAY(s5)
            DRAWBLOCKARRAY(s52)
            #finish button
            PRINTRETRYFONT()
            finishtext=basicFont.render('-finish-',True,WHITE,BLUE)
            finishtextRect = finishtext.get_rect()
            finishtextRect.centerx = 660
            finishtextRect.centery = windowSurface.get_rect().centery
            windowSurface.blit(finishtext,finishtextRect)
            if boxx!=None and boxy!=None and play==True:
                if not SelectedBox[boxx][boxy] and mouseClicked:
                    SelectedBox[boxx][boxy]=True
                    if (x1,y1) == (None,None) and (x2,y2) == (None,None) and finishtextRect.collidepoint(mousex,mousey)==False:
                        (x1,y1)=(boxx,boxy)
                        mouseClicked=False
                    elif (x1,y1) != (None,None) and (x2,y2) == (None,None) and finishtextRect.collidepoint(mousex,mousey)==False:
                        (x2,y2)=(boxx,boxy)
                        (X1,Y1)=(s5[x1][y1][2],s5[x1][y1][3])    #(x1,y1)is pixel while (X1,Y1)is not 
                        (X2,Y2)=(s5[x2][y2][2],s5[x2][y2][3])    #(x2,y2)is pixel while (X2,Y2)is not
                        (s5[x1][y1][2],s5[x1][y1][3])=(X2,Y2)
                        (s5[x2][y2][2],s5[x2][y2][3])=(X1,Y1)
                        drawblock([s5[x1][y1],s5[x2][y2]])
                        pygame.display.update()
                        SelectedBox[x1][y1]=False
                        SelectedBox[x2][y2]=False
                        mouseClicked=False
                        (x1,y1) = (None,None)
                        (x2,y2) = (None,None)
            elif  finishtextRect.collidepoint(mousex,mousey)==True and mouseClicked and play==True:
                play=False
                score5=countscore(s5,s52)
            elif play==False:
                scoreFont=pygame.font.SysFont(None,220)
                scoretext=scoreFont.render(str(score5),True,BLUE,WHITE)
                scoretextRect=scoretext.get_rect()
                scoretextRect.centerx = windowSurface.get_rect().centerx
                scoretextRect.centery = windowSurface.get_rect().centery
                windowSurface.blit(scoretext,scoretextRect)                        
        pygame.display.update()

