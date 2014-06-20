import pygame, sys, random
import sqlite3
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 1280
WINDOWHEIGHT = 700
BOXSIZE = 25
GAPSIZE = 7 
UNITSIZE = BOXSIZE + GAPSIZE
LINEWIDTH = 3
BLANKNUMBER = 80

BASICSIZE = 20
MENUSIZE = 40

MODEMENU = 'Menu'
MODEZEN = 'Zen'
MODERANK = 'Rank'
MODETIME10x10 = 'Time 10x10'
MODETIME15x15 = 'Time 15x15'
MODETIME18x18 = 'Time 18x18'
MODETIME25x18 = 'Time 25x18'
GAMEMODES = [MODEZEN, MODETIME10x10, MODETIME15x15, MODETIME18x18, MODETIME25x18]

SIZEOFGAMEMODE = {MODEZEN:(35,18),MODETIME10x10:(10,10),MODETIME15x15:(15,15),MODETIME18x18:(18,18),MODETIME25x18:(25,18)}
TOTALTIMEOFGAMEMODE = {MODEZEN:2000, MODETIME10x10:500, MODETIME15x15:1000, MODETIME18x18:1500, MODETIME25x18:2000}

GAMETOMENU = 'gametomenu'
MENUTOGAME = 'menutogame'
GAMETOGAME = 'gametogame'
MENUTORANK = 'menutorank'
RANKTOMENU = 'ranktomenu'
DELETEDATA = 'deletedata'

GRAY = (100,100,100)
BLUE = (0,0,255)
BLACK = (0,0,0)
CYAN = (0,255,255)
YELLOW = (255,255,0)
WHITE = (255,255,255)
DEEPBLUE = (130,75,255)
RED = (255,0,0)
GREEN = (0,255,0)
PURPLE = (255,0,255)

BGCOLOR = GRAY
HIGHLIGHTCOLOR = BLUE
LINECOLOR = (242,156,73)
TEXTCOLOR = (115,212,236)
TIMECOLOR = (141,106,243)

ALLCOLORS = (RED, GREEN, WHITE, YELLOW, DEEPBLUE, PURPLE, CYAN)

class Option(object):
	def __init__(self, surf, rect, typeofoption, mode = None):
		self.surf = surf
		self.rect = rect
		self.typeofoption = typeofoption
		self.mode = mode
	def action(self,board):
		if self.typeofoption == GAMETOMENU:
			RecordScore(board)
			board.mode = MODEMENU
		elif self.typeofoption == MENUTOGAME:
			width, height = SIZEOFGAMEMODE[self.mode]
			board.setsize(width,height) 
			board.totaltime = TOTALTIMEOFGAMEMODE[self.mode]
			board.initialize()
			board.mode = self.mode
		elif self.typeofoption == GAMETOGAME:
			RecordScore(board)
			board.initialize()
		elif self.typeofoption == MENUTORANK:
			board.mode = MODERANK
		elif self.typeofoption == RANKTOMENU:
			board.mode = MODEMENU
		elif self.typeofoption == DELETEDATA:
			DeleteScore()

class Box(object):
	def __init__(self, color=BGCOLOR, left=0, top=0, size=0):
		self.size = size
		self.color = color
		self.visible = True
		self.rect = pygame.Rect(left,top,size,size)

class Board(object):
	def __init__(self, width=10, height=10):
		self.width = width
		self.height = height
		self.score = 0
		self.totaltime = 0
		self.time = 0
		self.xmargin = int((WINDOWWIDTH - (width*UNITSIZE))/2)
		self.ymargin = int((WINDOWHEIGHT - (height*UNITSIZE))/2)
		self.mode = MODEMENU
	
	def setsize(self, width=10, height=10):
		self.width = width
		self. height = height
		self.xmargin = int((WINDOWWIDTH - (width*UNITSIZE))/2)
		self.ymargin = int((WINDOWHEIGHT - (height*UNITSIZE))/2)

	def decresetime(self, decrement=1):
		self.time -= decrement

	def initialize(self):
		self.board = []
		for i in range(self.width):
			tmp = []
			for j in range(self.height):
				color = randomcolor()
				left = self.xmargin + UNITSIZE * i
				top = self.ymargin + UNITSIZE * j
				tmp.append(Box(color,left,top,BOXSIZE))
			self.board.append(tmp)
		for i in range(BLANKNUMBER):
			x = random.randint(0,self.width-1)
			y = random.randint(0,self.height-1)
			self.board[x][y].visible = False
		self.combo = 0
		self.score = 0
		self.time = self.totaltime
	
	def IncreseOneBox(self):
		tmp = []
		for i in range(self.width):
			for j in range(self.height):
				if self.board[i][j].visible == False:
					tmp.append(self.board[i][j])
		index = random.randint(0,len(tmp)-1)
		tmp[index].visible = True
		tmp[index].color = randomcolor()

	def getCoordAtPixel(self,x,y):
		for i in range(self.width):
			for j in range(self.height):
				if self.board[i][j].rect.collidepoint(x,y):
					return (i,j)
		return (None,None)
	
	def ClickOnBox(self,x,y):
		if self.board[x][y].visible == True:
			return
		boxlist = []
		dx = (0,0,1,-1)
		dy = (1,-1,0,0)
		for i in range(4):
			nowx, nowy = x+dx[i], y+dy[i]
			while 0<=nowx<self.width and 0<=nowy<self.height:
				if self.board[nowx][nowy].visible:
					boxlist.append(self.board[nowx][nowy])
					break
				nowx, nowy = nowx+dx[i], nowy+dy[i]
		cancelbox = 0
		for i in range(len(boxlist)):
			for j in range(len(boxlist)):
				if i is not j :
					if boxlist[i].color == boxlist[j].color:
						boxlist[i].visible = False
						cancelbox += 1
						break
		self.score += cancelbox 
		self.time += cancelbox * 10
		if cancelbox == 0:
			self.time -= 100

def main():
	global DISPLAYSURF

	pygame.init()

	OpenDatabase()
	CreateAllOptions()

	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
	pygame.display.set_caption("Cross Boxes")

	DISPLAYSURF.fill(BGCOLOR)
	MainBoard = Board()
	
	while True:
		DISPLAYSURF.fill(BGCOLOR)
		if MainBoard.mode == MODEMENU:
			MenuInterface(MainBoard)
		elif MainBoard.mode == MODERANK:
			RankInterface(MainBoard)
		else:
			GameInterface(MainBoard)
		pygame.display.update()
		FPSCLOCK.tick(FPS)

def GameInterface(board):
	global GameOptions
	drawGame(board)
	drawScore(board.score)

	if board.mode is not MODEZEN:
		drawTime(board.time)
	for event in pygame.event.get():
		if IsTerminateAction(event):
			terminate()
		if event.type == MOUSEBUTTONUP:
			mouseX, mouseY = event.pos
			X, Y = board.getCoordAtPixel(mouseX, mouseY)
			if (X, Y) != (None, None):
				board.ClickOnBox(X,Y)
			else:
				for option in GameOptions:
					if option.rect.collidepoint(event.pos):
						option.action(board)
	if board.mode is not MODEZEN:
		board.decresetime(1)
		if board.time <= 0:
			RecordScore(board)
			board.mode = MODEMENU


def MenuInterface(board):
	global MenuOptions
	drawMenu(board)
	for event in pygame.event.get():
		if IsTerminateAction(event):
			terminate()
		if event.type == MOUSEBUTTONUP:
			for option in MenuOptions:
				if option.rect.collidepoint(event.pos):
					option.action(board)

def RankInterface(board):
	global RankOptions
	drawRank()
	for event in pygame.event.get():
		if IsTerminateAction(event):
			terminate()
		if event.type == MOUSEBUTTONUP:
			for option in RankOptions:
				if option.rect.collidepoint(event.pos):
					option.action(board)

def CreateAllOptions():
	global MenuOptions, RankOptions, GameOptions
	MenuOptions = []
	for i in range(len(GAMEMODES)):
		name = GAMEMODES[i]
		game_SURF, game_RECT = makeText(name,TEXTCOLOR,BGCOLOR,WINDOWWIDTH/2-80,WINDOWHEIGHT/2-210+70*i,MENUSIZE)
		gameoption = Option(game_SURF,game_RECT,MENUTOGAME,name)
		MenuOptions.append(gameoption)
	RANK_SURF, RANK_RECT = makeText('Rank',TEXTCOLOR,BGCOLOR,WINDOWWIDTH/2-80,WINDOWHEIGHT/2-210+70*len(GAMEMODES),MENUSIZE)
	rankoption = Option(RANK_SURF,RANK_RECT,MENUTORANK)
	MenuOptions.append(rankoption)

	RankOptions = []
	RMENU_SURF, RMENU_RECT = makeText('Menu',TEXTCOLOR,BGCOLOR,WINDOWWIDTH-100,WINDOWHEIGHT-30,BASICSIZE)
	rmenuoption = Option(RMENU_SURF,RMENU_RECT,RANKTOMENU)
	RankOptions.append(rmenuoption)
	DELETE_SURF, DELETE_RECT = makeText('Delete Data',TEXTCOLOR,BGCOLOR,WINDOWWIDTH-300,WINDOWHEIGHT-30,BASICSIZE)
	deleteoption = Option(DELETE_SURF,DELETE_RECT,DELETEDATA)
	RankOptions.append(deleteoption)

	MENU_SURF, MENU_RECT = makeText('Menu',TEXTCOLOR,BGCOLOR,WINDOWWIDTH-180,WINDOWHEIGHT-30,BASICSIZE)
	RESTART_SURF, RESTART_RECT = makeText('Restart',TEXTCOLOR,BGCOLOR,WINDOWWIDTH-100,WINDOWHEIGHT-30,BASICSIZE)

	GameOptions = []
	menuoption = Option(MENU_SURF,MENU_RECT,GAMETOMENU,MODEMENU)
	restartoption = Option(RESTART_SURF,RESTART_RECT,GAMETOGAME)
	GameOptions.append(menuoption)
	GameOptions.append(restartoption)

def randomcolor():
	colorindex = random.randint(0,len(ALLCOLORS)-1)
	return ALLCOLORS[colorindex]

def makeText(text, color, bgcolor, top, left, size):
	BASICFONT = pygame.font.Font('freesansbold.ttf', size)
	textSurf = BASICFONT.render(text, True, color, bgcolor)
	textRect = textSurf.get_rect()
	textRect.topleft = (top,left)
	return (textSurf, textRect)

def drawGame(board):
	drawBoard(board)
	drawLine(board)
	drawGameOptions()

def drawBoard(board):
	for x in range(board.width):
		for y in range(board.height):
			box = board.board[x][y]
			if box.visible:
				pygame.draw.rect(DISPLAYSURF,box.color,box.rect)

def drawLine(board):
	ystart = board.ymargin - GAPSIZE/2
	yend = WINDOWHEIGHT - board.ymargin - GAPSIZE/2
	for i in range(board.width+1):
		x = board.xmargin + UNITSIZE * i - GAPSIZE/2
		pygame.draw.line(DISPLAYSURF,LINECOLOR,(x,ystart),(x,yend),LINEWIDTH)
	xstart = board.xmargin - GAPSIZE/2
	xend = WINDOWWIDTH - board.xmargin - GAPSIZE/2
	for j in range(board.height+1):
		y = board.ymargin + UNITSIZE * j - GAPSIZE/2
		pygame.draw.line(DISPLAYSURF,LINECOLOR,(xstart,y),(xend,y),LINEWIDTH)

def drawGameOptions():
	global GameOptions
	for option in GameOptions:
		DISPLAYSURF.blit(option.surf,option.rect)

def drawMenuOptions():
	global MenuOptions
	for option in MenuOptions:
		DISPLAYSURF.blit(option.surf,option.rect)


def drawRankOptions():
	global RankOptions
	for option in RankOptions:
		DISPLAYSURF.blit(option.surf,option.rect)

def drawMenu(board):
	drawMenuOptions()
	drawScore(board.score)

def drawScore(score):
	SCORE_SURF, SCORE_RECT = makeText('score = '+str(score),TEXTCOLOR, BGCOLOR,30,WINDOWHEIGHT-30,BASICSIZE)
	DISPLAYSURF.blit(SCORE_SURF,SCORE_RECT)

def drawTime(time):
	pygame.draw.rect(DISPLAYSURF,TIMECOLOR,(50,15,time/2,20))

def drawStatus(board):
	text = "time = "+str(board.time)+" score = "+str(board.score)+" mode = "+board.mode+" width = "+str(board.width)+" height = "+str(board.height)
	STATUS_SURF, STATUS_RECT = makeText(text,TEXTCOLOR,BGCOLOR,0,0,BASICSIZE)
	DISPLAYSURF.blit(STATUS_SURF,STATUS_RECT)

def drawRank():
	drawRankOptions()
	global cur
	for i in range(len(GAMEMODES)):
		name = GAMEMODES[i]
		if name[0:5] == 'Time ':
			name = name[5:]
		NAME_SURF, NAME_RECT = makeText(name,TEXTCOLOR,BGCOLOR,175+200*i,200,MENUSIZE-5)
		DISPLAYSURF.blit(NAME_SURF,NAME_RECT)
		cur.execute("select * from rank where mode='"+GAMEMODES[i]+"' order by score desc limit 5")
		for j in [1,2,3,4,5]:
			score = 0
			item = cur.fetchone()
			if item is not None:
				score = item[0]
			HIGH_SURF, HIGH_RECT = makeText(str(j)+":   "+str(score),TEXTCOLOR,BGCOLOR,175+200*i,200+50*j,MENUSIZE-5)
			DISPLAYSURF.blit(HIGH_SURF,HIGH_RECT)


def IsTerminateAction(event):
	return event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE)

def terminate():
	pygame.quit()
	sys.exit()

def OpenDatabase():
	global con, cur
	con = sqlite3.connect('crossbox.db3')
	cur = con.cursor()
	cur.execute("select count(*) from sqlite_master where type='table' and name='rank'")
	if cur.fetchone()[0] == 0:
		cur.execute("create table rank(score,mode)")

def RecordScore(MainBoard):
	global con, cur
	cur.execute("insert into rank values("+str(MainBoard.score)+",'"+MainBoard.mode+"')")
	con.commit()

def DeleteScore():
	global con, cur
	cur.execute("delete from rank where score>=0")
	con.commit()

if __name__ == "__main__":
	main()
