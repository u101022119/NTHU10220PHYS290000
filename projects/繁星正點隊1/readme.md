Color Sorting Game
============

這是一個遊戲讓玩家根據程式所給的參考圖畫，去嘗試排列相近的顏色

>遊戲說明:
>先在遊戲選單裡面選擇難度
>進到遊戲畫面後，右邊會呈現遊戲希望玩家完成的答案
>玩家根據右邊的答案，用滑鼠點擊任兩個方格讓它交換
>當玩家認為完成之後點擊finish鍵後系統會計算玩家的完成程度
>給予相對應的分數，分數越低代表完成度越高

遊戲畫面分成兩個部分

  * 遊戲選單
  * 遊戲畫面

遊戲選單內包含五種難度給玩家選擇,難度的不同因方格色碼的變化量而不同
 1. easy, 以25為單位做變化
 2. normal, 以10為單位做變化
 3. hard, 以5為單位做變化
 4. crazy, 以3為單位做變化
 5. WTH, 以1為單位做變化

難度的不同以list的形式把100個方格應該擁有的顏色存在程式碼裡面的這個部分

~~~

#gamemode
easy=range(0,250,25)
normal=range(100,200,10)
hard=range(150,200,5)
crazy=range(150,180,3)
WTH=range(150,160,1)

~~~

函數定義
-----
這邊稍微介紹一下程式中所定義的函數

####1.這是產生100個方格的函數##

~~~
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

~~~

####2.產生對應答案的函數###

~~~
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
~~~

####3.把方格畫到畫面上的函數###

~~~
def DRAWBLOCKARRAY(s):
    for i in range(10):
        for j in range(10):
            pygame.draw.rect(windowSurface,(s[i][j][2],s[i][j][3],0),(s[i][j][0],s[i][j][1],BLOCKSIZE,BLOCKSIZE)) 
~~~

####4.決定方格是否被點擊過的判斷函數##

~~~
def GenerateSelectedBoxData(val):
    SelectedBox=[]
    for i in range(10):
        SelectedBox.append([val]*10)
    return SelectedBox
~~~

####5.把遊戲的方格座標像素化，讓方格之間的運算簡化的函數

~~~

def getBoxAtPixel(x, y):
    for boxx in range(10):
        for boxy in range(10):
            left, top = leftTopCoordsOfBox(boxx, boxy)
            boxRect = pygame.Rect(left, top, BOXSIZE, BOXSIZE)
            if boxRect.collidepoint(x, y):
                return (boxx, boxy)
    return (None, None)

~~~

####6.像素化的方格運算過後轉換回視窗座標的函數

~~~
def leftTopCoordsOfBox(boxx, boxy):
    # Convert board coordinates to pixel coordinates
    left = boxx * BLOCKSIZE + 20
    top = boxy * BLOCKSIZE + 20
    return (left, top)
~~~

####7.計算遊戲分數的函數，以方格的正確位置和玩家放置位置的座標差來做計算

~~~
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
~~~

遊戲迴圈
--------


在遊戲的第一層迴圈繪製遊戲選單，利用一開始設定的變數來跟遊戲畫面做切換

~~~

    windowSurface=pygame.display.set_mode((1320,440))
    windowSurface.fill((180,45,100))
    pygame.display.update()
    .
    .
    .
    menu=True
    retry=False
    play=False
    mode1=False
    mode2=False
    mode3=False
    mode4=False
    mode5=False
    retry=False
~~~
選擇遊戲模式後相對應的mode變數會轉為True，menu變數會變為False
以防止在遊戲模式誤觸menu上的按鈕

在遊戲迴圈建立在:
~~~
    while not retry:
~~~
來讓遊戲具有重置功能

接下來在:
~~~
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
~~~
設定遊戲的input，在滑鼠指標的移動跟點擊時都擷取座標，並以mouseClicked變數來做區分

進入不同難度的遊戲時使用的迴圈大致相同，在迴圈外設定的變數不同，以繪出不同的難度

其中第三層迴圈內的:

~~~
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
~~~
是用來交換兩次點擊的方塊的顏色資訊，並重新繪製兩個方塊
原本是打算把整個遊戲盤面重新繪製，後來才想出只畫兩個方塊的函數

project製作過程
--------
一開始是打算製作棋盤類的遊戲，但是發現光是要搞定儲存所有方塊內資訊（座標、顏色etc.）
就已經遇到許多困難，只好把遊戲簡化到只儲存方塊內的少數資訊
所以產生了這個遊戲

遇到的困難有:

    * 一開始沒有想到把方塊像素化，所以位置資訊十分混亂
    * 遊戲模式之間的切換沒有想到控制方法，所以即使畫面變了，滑鼠動到原本的按鈕還是會有效果
    * 最後是利用list的模式改變來控制顏色資訊的交換也遇到了問題，最後產生了兩層list與三層list的轉換函數

