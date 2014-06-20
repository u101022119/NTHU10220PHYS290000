# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 20:12:21 2014

@author: user
"""

import pygame, sys, random
from pygame.locals import *
screen_width=700
screen_height=400
screen=pygame.display.set_mode([screen_width,screen_height])
background = (255, 255, 255)
BLACK = (255, 255, 255)
BLUE = (0, 0, 255)
CELLWIDTH = 58
CELLHEIGHT = 58
PIECEWIDTH = 25
PIECEHEIGHT = 25
BOARDX = 12
BOARDY = 8
FPS = 50

# 退出遊戲
def terminate():
    pygame.quit()
    sys.exit()

# 重置棋盤
def ResetBoard(board):
    for x in range(8):
        for y in range(8):
            board[x][y] = 'none'
            # 黑白棋是使用8*8的棋盤，所以 x 和 y 是從 1~8，也就是 in range(8)。
    
    board[3][3] = 'black'
    board[3][4] = 'white'
    board[4][3] = 'white'
    board[4][4] = 'black'
    # 黑白棋的遊戲規則之一：在雙方開始之前會先在棋盤正中央放置黑白棋各兩顆(對角線位置)


# 每一步建立新棋盤
def NewBoard():
    board = []
    for i in range(8):
        board.append(['none'] * 8)
    return board
    

# 檢驗是否在界內
def OnBoard(x, y):
    return x >= 0 and x <=7 and y >= 0 and y <=7
    # 這個定義是用在下方的合法走法，若下棋的位置不在界內(not OnBoard)，就不能下(return false)

# 檢驗是否是合法走法
def Validmove(board, tile, xstart, ystart): # xstart 和 ystart 就是你下棋的位置，tile就是棋子
    
    # 如果該位置出界或者已經有棋子，就不能下
    if not OnBoard(xstart, ystart) or board[xstart][ystart] != 'none':
        return False

    # 臨時將 tile 放到指定的位置
    board[xstart][ystart] = tile

    if tile == 'black':
        othertile = 'white'
    else:
        othertile = 'black'
    # 如果你下的棋子(tile)是黑色(白色)的話，電腦下的(othertile)就是白色(黑色)

    # 要被翻的棋子
    # 這邊要講解一下遊戲規則。當一方下了一個棋子後，從那個棋子的位置開始，往上下左右以及四個45度方向走，一直走到出界或是碰到同色的棋子為止，路上經過的每一個棋子都要翻色。
    flip = []

    for xdirection, ydirection in [ [0, 1], [0, -1], [-1, 0], [1, 0], [1, 1], [1, -1],  [-1, -1],  [-1, 1] ]:# 上下左右和四個45度方向
        x, y = xstart, ystart
        x += xdirection
        y += ydirection  # 從任一方下的棋子的位置開始往特定方向走
        if OnBoard(x, y) and board[x][y] == othertile:
            x += xdirection
            y += ydirection
            if not OnBoard(x, y):
                continue
            # 一直走到出界或不是对子的位置
            while board[x][y] == othertile:
                x += xdirection
                y += ydirection
                if not OnBoard(x, y):
                    break
            # 出界了，則棋子要翻轉XXXX
            if not OnBoard(x, y):
                continue
            # 是自己的棋子OXXXXXXO
            if board[x][y] == tile:
                while True:
                    x -= xdirection
                    y -= ydirection
                    # 回到了起點則结束
                    if x == xstart and y == ystart:
                        break
                    # 需要翻轉的棋子
                    flip.append([x, y])


    # 將前面臨時放上的棋子去掉，即還原棋盤
    board[xstart][ystart] = 'none' 
    # 這個tile的功能其實只是為了翻棋，你真正下的棋會在下方的makemove裡面出現

    # 如果你將棋子下在某個位置後沒有任何棋子可翻，就不能下
    if len(flip) == 0:   
        return False
    return flip

# 將一個tile棋子放到(xstart, ystart)
def MakeMove(board, tile, xstart, ystart):
    flip = Validmove(board, tile, xstart, ystart)

    if flip == False:
        return False

    board[xstart][ystart] = tile
    for x, y in flip:
        board[x][y] = tile
    return True


# 選取可下的位置
def getValidmove(board, tile):
    validMoves = []

    for x in range(8):
        for y in range(8):
            if Validmove(board, tile, x, y) != False:
                validMoves.append([x, y])
    return validMoves



# 選取棋盤上黑白雙方的棋子数
def GetScore(board): 
    xscore = 0
    oscore = 0
    for x in range(8):
        for y in range(8):
            if board[x][y] == 'black':
                xscore += 1
            if board[x][y] == 'white':
                oscore += 1
    return {'black':xscore, 'white':oscore}


# 決定順序，遊戲開始時為隨機決定先手
def GoFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


# 複製棋盤，給AI用
def CopyBoard(board):
    dupBoard = NewBoard()

    for x in range(8):
        for y in range(8):
            dupBoard[x][y] = board[x][y]

    return dupBoard


# 檢驗是否在角上
def Corner(x, y):
    return (x == 0 and y == 0) or (x == 8 and y == 0) or (x == 0 and y == 8) or (x == 8 and y == 8)


# 電脑走法，AI
def AI(board, computerTile):
    # 找出所有合法走法
    possible = getValidmove(board, computerTile)

    # 打亂所有合法走法
    random.shuffle(possible)

    # [x, y]在角上，則優先走，因為角上的不會被再次翻轉
    for x, y in possible:
        if Corner(x, y):
            return [x, y]

    bestScore = -1
    for x, y in possible:
        dupBoard = CopyBoard(board)
        MakeMove(dupBoard, computerTile, x, y)
        # 按照分数選擇走法，優先選擇翻轉後分数最多的走法
        score = GetScore(dupBoard)[computerTile]
        if score > bestScore:
            bestMove = [x, y]
            bestScore = score
            return bestMove
        else:
            pass

# 游戲结束指令
def GameOver(board):
    for x in range(8):
        for y in range(8):
            if board[x][y] == 'none':
                return False
    return True


# 初始化
pygame.init()
mainClock = pygame.time.Clock()

# 加载圖片和音樂
boardImage = pygame.image.load('board.gif')
boardRect = boardImage.get_rect()
blackImage = pygame.image.load('black.gif')
blackRect = blackImage.get_rect()
whiteImage = pygame.image.load('white.gif')
whiteRect = whiteImage.get_rect()
pygame.mixer.music.load("GAME START.mp3")
pygame.mixer.music.play(-1,0)


basicFont = pygame.font.SysFont("arial", 25)
gameoverStr = 'Game Over Score '


mainBoard = NewBoard()
ResetBoard(mainBoard)

turn = GoFirst()
if turn == 'player':
    playerTile = 'black'
    computerTile = 'white'
else:
    playerTile = 'white'
    computerTile = 'black'

print(turn) 

# 設置窗口
windowSurface = pygame.display.set_mode((boardRect.width, boardRect.height))
pygame.display.set_caption('黑白棋')

gameOver = False


# 游戲主循環

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()
        if gameOver == False and turn == 'player' and event.type == MOUSEBUTTONDOWN and event.button == 1:
            x, y = pygame.mouse.get_pos()
            col = int((x-BOARDX)/CELLWIDTH)
            row = int((y-BOARDY)/CELLHEIGHT)
            if MakeMove(mainBoard, playerTile, col, row) == True:
                if getValidmove(mainBoard, computerTile) != []:
                    turn = 'computer'

    windowSurface.fill(background)
    windowSurface.blit(boardImage, boardRect, boardRect)

    if (gameOver == False and turn == 'computer'):
        x, y = AI(mainBoard, computerTile)
        MakeMove(mainBoard, computerTile, x, y)
        savex, savey = x, y

        if getValidmove(mainBoard, playerTile) != []:
            turn = 'player'

    windowSurface.fill(background)
    windowSurface.blit(boardImage, boardRect, boardRect)
    
    for x in range(8):
        for y in range(8):
            rectDst = pygame.Rect(BOARDX+x*CELLWIDTH+1, BOARDY+y*CELLHEIGHT+1, PIECEWIDTH, PIECEHEIGHT)
            if mainBoard[x][y] == 'black':
                windowSurface.blit(blackImage, rectDst, blackRect)
            elif mainBoard[x][y] == 'white':
                windowSurface.blit(whiteImage, rectDst, whiteRect)

    if GameOver(mainBoard):
        pygame.mixer.music.stop()
        pygame.mixer.music.load("clap.mp3")
        pygame.mixer.music.play(-1,0)
        scorePlayer = GetScore(mainBoard)[playerTile]
        scoreComputer = GetScore(mainBoard)[computerTile]
        outputStr = gameoverStr +"  "+ "player  "+str(scorePlayer) + "  :  " +"computer  "+ str(scoreComputer)
        text = basicFont.render(outputStr, True, BLACK, BLUE)
        textRect = text.get_rect()
        textRect.centerx = windowSurface.get_rect().centerx
        textRect.centery = windowSurface.get_rect().centery
        windowSurface.blit(text, textRect)
    
    pygame.display.update()
    mainClock.tick(FPS)

