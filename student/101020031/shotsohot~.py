# -*- coding: utf-8 -*-
"""
Created on Tue May 27 16:23:29 2014

@author: user
"""

import sys

import pygame

from pygame.locals import *

pygame.init()

windowSurface = pygame.display.set_mode((500, 400), 0, 32)

pygame.display.set_caption("Zombie shotshot~")


BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DOWNLEFT = 1
DOWNRIGHT = 3
UPLEFT = 7
UPRIGHT = 9
MOVESPEED = 4

b1 = {'rect':pygame.Rect(300, 80, 50, 100),
'color':RED, 'dir':UPRIGHT}
b2 = {'rect':pygame.Rect(200, 200, 20, 20),
'color':GREEN, 'dir':UPLEFT}
b3 = {'rect':pygame.Rect(100, 150, 60, 60),
'color':BLUE, 'dir':DOWNLEFT}
blocks = [b1, b2, b3]

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

windowSurface.fill(BLACK)

for b in blocks:
    if b['dir'] == DOWNLEFT:
        b['rect'].left -= MOVESPEED
        b['rect'].top += MOVESPEED
    if b['dir'] == DOWNRIGHT:
        b['rect'].left += MOVESPEED
        b['rect'].top += MOVESPEED
        
    if b['dir'] == UPLEFT:
        b['rect'].left -= MOVESPEED
        b['rect'].top -= MOVESPEED
    if b['dir'] == UPRIGHT:
        b['rect'].left += MOVESPEED
        b['rect'].top -= MOVESPEED

if b['rect'].top < 0:
    if b['dir'] == UPLEFT:
        b['dir'] = DOWNLEFT
    if b['dir'] == UPRIGHT:
        b['dir'] = DOWNRIGHT

pygame.draw.rect(windowSurface,
b['color'], b['rect'])

pygame.display.update()

time.sleep(0.02)
