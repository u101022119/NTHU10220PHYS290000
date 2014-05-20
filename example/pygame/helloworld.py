import sys
import pygame
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300),0,32)
pygame.display.set_caption('Hello World!')

WHITE = (255, 255, 255)
RED = (255, 0, 0)
DISPLAYSURF.fill(WHITE)
pygame.draw.polygon(DISPLAYSURF, RED, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
