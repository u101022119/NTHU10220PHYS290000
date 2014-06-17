import pygame, sys
import sqlite3
import random
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 1280
WINDOWHEIGHT = 700
BOXSIZE = 20
GAPSIZE = 10
BOARDWIDTH = 40
BOARDHEIGHT = 20
BLANKNUMBER = 20
LINEWIDTH = 3
TOTALTIME = 2300
BASICSIZE = 20
MENUSIZE = 40

MODEMENU = 'menu'
MODESTART = 'start'
MODEZEN = 'zen'
MODETIME = 'time'

XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE)))/2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE)))/2)

GRAY = (100,100,100)
BLUE = (0,0,255)
BLACK = (0,0,0)
CYAN = (0,255,255)
YELLOW = (255,255,0)
WHITE = (255,255,255)
ORANGE = (255,100,0)
RED = (255,0,0)
GREEN = (0,255,0)
PURPLE = (255,0,255)

BACKGROUNDCOLOR = GRAY
HIGHLIGHTCOLOR = BLUE
BOXCOLOR = BLACK
LINECOLOR = (242,156,73)
TEXTCOLOR = (115,212,236)
TIMECOLOR = (141,106,243)

ALLCOLORS = (RED, GREEN, WHITE, YELLOW, ORANGE, PURPLE, CYAN)

con = sqlite3.connect('crossbox.db3')
cur = con.cursor()
cur.execute("select count(*) from sqlite_master where type='table' and name='ranking'")
if cur.fetchone()[0] == 0:
	cur.execute("create table ranking(score,name)")


def main():#game loop
	global FPSCLOCK, DISPLAYSURF, mainBoard, remainedBoxes, time, score, RESTART_SURF, RESTART_RECT, TIME_SURF, TIME_RECT, MENU_SURF, MENU_RECT, ZEN_SURF, ZEN_RECT

	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
	pygame.display.set_caption('Cross Boxes')
	
	RESTART_SURF, RESTART_RECT = makeText('Restart', TEXTCOLOR, BACKGROUNDCOLOR, WINDOWWIDTH-100, WINDOWHEIGHT-30,BASICSIZE)
	TIME_SURF, TIME_RECT = makeText('Time', TEXTCOLOR, BACKGROUNDCOLOR, WINDOWWIDTH/2-50, WINDOWHEIGHT/2-70,MENUSIZE)
	ZEN_SURF, ZEN_RECT = makeText('Zen', TEXTCOLOR, BACKGROUNDCOLOR, WINDOWWIDTH/2-50, WINDOWHEIGHT/2,MENUSIZE)
	MENU_SURF, MENU_RECT = makeText('Menu', TEXTCOLOR, BACKGROUNDCOLOR, WINDOWWIDTH-180, WINDOWHEIGHT-30,BASICSIZE)


	mouseX = 0
	mouseY = 0

	mode = MODEMENU
	DISPLAYSURF.fill(BACKGROUNDCOLOR)
	
	InitializeGmae()

	while True:
		mouseClicked = False

		DISPLAYSURF.fill(BACKGROUNDCOLOR)
		if mode == MODEMENU:
			drawScore(score)
			drawMenu()
			drawHighestScore()
			for event in pygame.event.get():
				CheckForTerminate(event)
				if event.type == MOUSEBUTTONDOWN:
					if TIME_RECT.collidepoint(event.pos):
						InitializeGmae()
						mode = MODETIME
					elif ZEN_RECT.collidepoint(event.pos):
						InitializeGmae()
						mode = MODEZEN
		elif mode == MODETIME:
			drawBoard(mainBoard, remainedBoxes)
			drawOptions()
			drawScore(score)
			drawTime(time)
			for event in pygame.event.get():
				CheckForTerminate(event)
				if event.type == MOUSEMOTION:
					mouseX, mouseY = event.pos
				elif event.type == MOUSEBUTTONDOWN:
					mouseX, mouseY = event.pos
					mouseClicked = True

			boxX, boxY = getBoxAtPixel(mouseX,mouseY)
			
			if boxX == None and boxY == None:
				if mouseClicked:
					if RESTART_RECT.collidepoint(event.pos):
						cur.execute("insert into ranking values("+str(score)+",'unknown')")
						con.commit()
						InitializeGmae()
					elif MENU_RECT.collidepoint(event.pos):
						mode = MODEMENU
						cur.execute("insert into ranking values("+str(score)+",'unknown')")
						con.commit()
			elif boxX != None and boxY != None:
				drawHighlightBox(boxX,boxY)
				if mouseClicked:
					clickOnBox(boxX,boxY)	
			time -= 1
			if time <= 0:
				mode = MODEMENU
				cur.execute("insert into ranking values("+str(score)+",'unknown')")
				con.commit()
		elif mode == MODEZEN:
			drawBoard(mainBoard, remainedBoxes)
			drawOptions()
			drawScore(score)
			for event in pygame.event.get():
				CheckForTerminate(event)
				if event.type == MOUSEMOTION:
					mouseX, mouseY = event.pos
				elif event.type == MOUSEBUTTONDOWN:
					mouseX, mouseY = event.pos
					mouseClicked = True

			boxX, boxY = getBoxAtPixel(mouseX,mouseY)
			
			if boxX == None and boxY == None:
				if mouseClicked:
					if RESTART_RECT.collidepoint(event.pos):
						cur.execute("insert into ranking values("+str(score)+",'unknown')")
						con.commit()
						InitializeGmae()
					elif MENU_RECT.collidepoint(event.pos):
						cur.execute("insert into ranking values("+str(score)+",'unknown')")
						con.commit()
						mode = MODEMENU
			elif boxX != None and boxY != None:
				drawHighlightBox(boxX,boxY)
				if mouseClicked:
					clickOnBox(boxX,boxY)	
		pygame.display.update()
		FPSCLOCK.tick(FPS)
				

def InitializeGmae():
	global mainBoard, remainedBoxes, score, time
	mainBoard = getInitialBoard()
	remainedBoxes = getInitialRemainedBoxes()
	score = 0
	time = TOTALTIME

def clickOnBox(boxX,boxY):
	global score, time
	canceledbox = 0
	if not remainedBoxes[boxX][boxY]:
		UP = [boxX, boxY]
		DOWN = [boxX, boxY]
		LEFT = [boxX, boxY]
		RIGHT = [boxX, boxY] 

		position = []
		dx = [0,0,1,-1]
		dy = [-1,1,0,0]
		for i in range(4):
			nowX, nowY = boxX+dx[i], boxY+dy[i]
			while nowX>=0 and nowX<BOARDWIDTH and nowY>=0 and nowY<BOARDHEIGHT:
				if remainedBoxes[nowX][nowY]:
					position.append([nowX,nowY])
					break
				else:
					nowX += dx[i]
					nowY += dy[i]
		boxcolors = []
		for i in range(len(position)):
			boxcolors.append(mainBoard[position[i][0]][position[i][1]])

		for i in range(len(position)):
			for j in range(len(position)):
				if i is not j:
					if boxcolors[i] == boxcolors[j]:
						X = position[i][0]
						Y = position[i][1]
						remainedBoxes[X][Y] = False
						score += 1
						canceledbox += 1
						time += 10
						break
		if canceledbox == 0:
			time -= 100 

def getBoxAtPixel(x,y):
	for boxX in range(BOARDWIDTH):
		for boxY in range(BOARDHEIGHT):
			left, top = leftTopCoordsOfbox(boxX,boxY)
			boxRect = pygame.Rect(left,top,BOXSIZE,BOXSIZE)
			if boxRect.collidepoint(x,y):
				return (boxX,boxY)
	return (None,None)


def getInitialRemainedBoxes():
	remained = []
	for i in range(BOARDWIDTH):
		remained.append([True] * BOARDHEIGHT)
	for i in range(BLANKNUMBER):
		X = random.randint(0,BOARDWIDTH-1)
		Y = random.randint(0,BOARDHEIGHT-1)
		remained[X][Y] = False
	return remained

def leftTopCoordsOfbox(boxX,boxY):
	left = boxX * (BOXSIZE + GAPSIZE) + XMARGIN
	top = boxY * (BOXSIZE + GAPSIZE) + YMARGIN
	return (left,top)

def getInitialBoard():
	colors = []
	for i in range(BOARDWIDTH * BOARDHEIGHT):
		colorindex = random.randint(0,len(ALLCOLORS)-1)
		selectedcolor = ALLCOLORS[colorindex]
		colors.append(selectedcolor)
	board = []
	for x in range(BOARDWIDTH):
		column = []
		for y in range(BOARDHEIGHT):
			column.append(colors[0])
			del colors[0]
		board.append(column)
	return board

def drawBoard(board, remained):
	for boxX in range(BOARDWIDTH):
		for boxY in range(BOARDHEIGHT):
			left, top = leftTopCoordsOfbox(boxX, boxY)
			if remained[boxX][boxY]:
				color = board[boxX][boxY] 
			else:
				color = BACKGROUNDCOLOR
			pygame.draw.rect(DISPLAYSURF,color,(left,top,BOXSIZE,BOXSIZE))
	for boxX in range(1,BOARDWIDTH):
		left, top = leftTopCoordsOfbox(boxX, boxY)
		pygame.draw.line(DISPLAYSURF, LINECOLOR, (left-GAPSIZE/2,YMARGIN-GAPSIZE/2), (left-GAPSIZE/2,WINDOWHEIGHT-YMARGIN-GAPSIZE/2), LINEWIDTH)
	for boxY in range(1,BOARDHEIGHT):
		left, top = leftTopCoordsOfbox(boxX, boxY)
		pygame.draw.line(DISPLAYSURF, LINECOLOR, (XMARGIN-GAPSIZE/2,top-GAPSIZE/2), (WINDOWWIDTH-XMARGIN-GAPSIZE/2,top-GAPSIZE/2), LINEWIDTH)

def drawOptions():
	DISPLAYSURF.blit(RESTART_SURF, RESTART_RECT)
	DISPLAYSURF.blit(MENU_SURF, MENU_RECT)

def drawMenu():
	DISPLAYSURF.blit(TIME_SURF, TIME_RECT)
	DISPLAYSURF.blit(ZEN_SURF, ZEN_RECT)

def drawTime(time):
	pygame.draw.rect(DISPLAYSURF,TIMECOLOR,(50,15,time/2,20))

def drawScore(score):
	SCORE_SURF, SCORE_RECT = makeText('score = '+str(score),TEXTCOLOR,BACKGROUNDCOLOR,30,WINDOWHEIGHT-30,BASICSIZE)
	DISPLAYSURF.blit(SCORE_SURF, SCORE_RECT)

def drawHighlightBox(boxX,boxY):
	left, top = leftTopCoordsOfbox(boxX,boxY)
	pygame.draw.rect(DISPLAYSURF, HIGHLIGHTCOLOR, (left-5,top-5,BOXSIZE+10,BOXSIZE+10),4)

def makeText(text, color, bgcolor, top, left, size):
	BASICFONT = pygame.font.Font('freesansbold.ttf', size)
	textSurf = BASICFONT.render(text, True, color, bgcolor)
	textRect = textSurf.get_rect()
	textRect.topleft = (top, left)
	return (textSurf, textRect)

def drawHighestScore():
	cur.execute("select * from ranking order by score desc limit 1")
	highest = cur.fetchone()[0]
	HIGH_SURF, HIGH_RECT = makeText('highest score = '+str(highest), TEXTCOLOR, BACKGROUNDCOLOR,0,0,BASICSIZE)
	DISPLAYSURF.blit(HIGH_SURF, HIGH_RECT)

def CheckForTerminate(event):
	if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
		pygame.quit()
		sys.exit()

if __name__ == '__main__':
	main()
