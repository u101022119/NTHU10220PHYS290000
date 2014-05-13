# -*- coding: utf-8 -*-
"""
Created on Tue May 13 16:37:20 2014

@author: user
"""

import pygame, sys, random
from pygame.locals import *


pygame.init()
mainClock = pygame.time.Clock()

WINDOWWIDTH = 1000
WINDOWHEIGHT = 600
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Snake')

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

snake = []
snake1 = []
snake2 = []
SNAKESIZE = 20
LENGTH = 5

moveLeft = False
moveRight = True
moveUp = False
moveDown = False

for i in range(LENGTH):
    snake1.append(500-SNAKESIZE*i)
    snake2.append(300)

for i in range(LENGTH):
    snake.append(pygame.Rect(snake1[i], snake2[i], SNAKESIZE, SNAKESIZE))





while True:
    windowSurface.fill(BLACK)  
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit() 
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == ord('a'):
                if moveRight:
                    moveRight = True
                    moveLeft = False
                    moveUp = False
                    moveDown = False
                else:
                    moveLeft = True
                    moveRight = False
                    moveUp = False
                    moveDown = False    
            if event.key == K_RIGHT or event.key == ord('d'):
                if moveLeft:
                    moveRight = False
                    moveLeft = True
                    moveUp = False
                    moveDown = False
                else:
                    moveLeft = False
                    moveRight = True
                    moveUp = False
                    moveDown = False                                      
               
            if event.key == K_UP or event.key == ord('w'):
                if moveDown:
                     moveDown = True
                     moveUp = False
                     moveLeft = False
                     moveRight = False
                else:
                    moveUp = True
                    moveDown = False
                    moveLeft = False
                    moveRight = False       
            if event.key == K_DOWN or event.key == ord('s'):
                if moveUp:
                     moveDown = False
                     moveUp = True
                     moveLeft = False
                     moveRight = False
                else:
                    moveUp = False
                    moveDown = True
                    moveLeft = False
                    moveRight = False                                          
                
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
    if moveDown:
            for i in range(LENGTH):
                snake[LENGTH-1-i] = snake[LENGTH-2-i]
            snake[0] = pygame.Rect(snake1[0], snake2[0]+SNAKESIZE, SNAKESIZE, SNAKESIZE)
            snake2[0] += SNAKESIZE
    if moveUp:
            for i in range(LENGTH):
                snake[LENGTH-1-i] = snake[LENGTH-2-i]
            snake[0] = pygame.Rect(snake1[0], snake2[0]-SNAKESIZE, SNAKESIZE, SNAKESIZE)
            snake2[0] -= SNAKESIZE
    
    if moveLeft:
            for i in range(LENGTH):
                snake[LENGTH-1-i] = snake[LENGTH-2-i]
            snake[0] = pygame.Rect(snake1[0]-SNAKESIZE, snake2[0], SNAKESIZE, SNAKESIZE)
            snake1[0] -= SNAKESIZE
            
    if moveRight:
            for i in range(LENGTH):
                snake[LENGTH-1-i] = snake[LENGTH-2-i]
            snake[0] = pygame.Rect(snake1[0]+SNAKESIZE, snake2[0], SNAKESIZE, SNAKESIZE)
            snake1[0] += SNAKESIZE
            
        
        
            
            
            
            
      
    for i in range(LENGTH):
        pygame.draw.rect(windowSurface, WHITE, snake[i])
    
    
    
    
    
    pygame.display.update()
    mainClock.tick(20)

    


     
