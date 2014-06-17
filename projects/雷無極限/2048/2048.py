# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 15:23:03 2014

@author: Harry
"""

import pygame, random, math, sys, copy, time
from pygame.locals import *
from operator import itemgetter




game=0
screen=0
 
BLACK = (0,0,0)
WHITE = (255,255,255)
 
class Board:
    pygame.mixer.init()
    pygame.init()
    def __init__(self, game, copied = False):
        self.board = [['.','.','.','.'],
                      ['.','.','.','.'],
                      ['.','.','.','.'],
                      ['.','.','.','.']]
        self.board[random.randint(0,3)][random.randint(0,3)] = 2
        self.game = game
        self.copied = copied
 
    def get_empty(self):
        empty = []
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == '.':
                    empty.append((i,j))
        return empty
 
    def create_random(self):
        empty = self.get_empty()
        if empty:
            i, j = random.choice(empty)
            value = random.choice([2]*9 + [4])
            self.board[i][j] = value
 
    def is_full(self):
        for row in self.board:
            for cell in row:
                if cell == '.':
                    return False
        return True
 
    def no_moves(self):
        for move in range(4):
            new_board = Board(game, True)
            new_board.board = copy.deepcopy(self.board)
            move_list = [new_board.up,new_board.down,new_board.left,new_board.right]
            move_list[move]()
            if new_board.board != self.board:
                return False
        return True
           
 
    def up(self):
        score = 0
        can_combine = [True,True,True,True]
        move_count = -1
        a=[1] 
        for j in range(4):
            if '.' not in [self.board[i][j] for i in range(4)] and \
               self.board[0][j] == self.board[1][j] and \
               self.board[2][j] == self.board[3][j]:
                self.board[0][j] *= 2
                self.board[1][j] = self.board[2][j] *2
                self.board[2][j] = '.'
                self.board[3][j] = '.'
                can_combine[j] = False
                score += self.board[0][j] + self.board[1][j]
                if not self.copied:
                    self.game.draw()
       
        while move_count != 0:
            move_count = 0
            a=[1]
            for i in range(1,4):
                for j in range(4):
                    if self.board[i][j] != '.':
                        if self.board[i-1][j] == '.':
                            self.board[i][j], self.board[i-1][j] = self.board[i-1][j],self.board[i][j]
                            move_count += 1
                        elif self.board[i-1][j] == self.board[i][j] and can_combine[j]:
                            if self.board[i][j]==512:
                                a.append(9)
                            elif self.board[i][j]==256:
                                a.append(8)
                            elif self.board[i][j]==128:
                                a.append(7)
                            elif self.board[i][j]==64:
                                a.append(6)
                            elif self.board[i][j]==32:
                                a.append(5)    
                            elif self.board[i][j]==16:
                                a.append(4)    
                            elif self.board[i][j]==8:
                                a.append(3)
                            elif self.board[i][j] == 4:
                                a.append(2)    
                            self.board[i-1][j] *= 2
                            self.board[i][j] = '.'
                            can_combine[j] = False
                            score += self.board[i-1][j]
                            move_count += 1
                if not self.copied:
                    self.game.draw()
            a.sort()
            if a[len(a)-1] == 9:
                pygame.mixer.music.load("he.mp3")
                pygame.mixer.music.play(1,0.0)
                 
            elif a[len(a)-1] == 8:
                pygame.mixer.music.load("expect.mp3")
                pygame.mixer.music.play(1,0.0)
                
            elif a[len(a)-1] == 7:
                pygame.mixer.music.load("learn.mp3")
                pygame.mixer.music.play(1,0.0)
                
            elif a[len(a)-1] == 6:
                pygame.mixer.music.load("problem.mp3")
                pygame.mixer.music.play(1,0.0)
               
            elif a[len(a)-1] == 5:
                pygame.mixer.music.load("alright.mp3")
                pygame.mixer.music.play(1,0.0)
                
            elif a[len(a)-1] == 4:
                pygame.mixer.music.load("coo.mp3")
                pygame.mixer.music.play(1,0.0)
                
            elif a[len(a)-1] == 3:
                pygame.mixer.music.load("pig.mp3")
                pygame.mixer.music.play(1,0.0)
                
            elif a[len(a)-1] == 2:
                pygame.mixer.music.load('anyway.mp3')
                pygame.mixer.music.play(1,0.0)
        return score
 
    def left(self):
        score = 0
        can_combine = [True,True,True,True]
        move_count = -1
        a=[1]       
        for i in range(4):
            if '.' not in [self.board[i][j] for j in range(4)] and \
               self.board[i][0] == self.board[i][1] and \
               self.board[i][2] == self.board[i][3]:
                self.board[i][0] *= 2
                self.board[i][1] = self.board[i][2] *2
                self.board[i][2] = '.'
                self.board[i][3] = '.'
                can_combine[i] = False
                score += self.board[i][0] + self.board[i][1]
                if not self.copied:
                    self.game.draw()                  
        while move_count != 0:
            move_count = 0
            a=[1]
            for j in range(1,4):
                for i in range(4):
                    if self.board[i][j] != '.':
                        if self.board[i][j-1] == '.':
                            self.board[i][j], self.board[i][j-1] = self.board[i][j-1],self.board[i][j]
                            move_count += 1
                        elif self.board[i][j-1] == self.board[i][j] and can_combine[i]:
                            if self.board[i][j]==512:
                                a.append(9)
                            elif self.board[i][j]==256:
                                a.append(8)
                            elif self.board[i][j]==128:
                                a.append(7)
                            elif self.board[i][j]==64:
                                a.append(6)
                            elif self.board[i][j]==32:
                                a.append(5)    
                            elif self.board[i][j]==16:
                                a.append(4)    
                            elif self.board[i][j]==8:
                                a.append(3)
                            elif self.board[i][j] == 4:
                                a.append(2)
                            self.board[i][j-1] *= 2
                            self.board[i][j] = '.'
                            can_combine[i] = False
                            score += self.board[i][j-1]
                            move_count += 1
                if not self.copied:
                    self.game.draw()
            a.sort()
            if a[len(a)-1] == 9:
                pygame.mixer.music.load("he.mp3")
                pygame.mixer.music.play(1,0.0)
                 
            elif a[len(a)-1] == 8:
                pygame.mixer.music.load("expect.mp3")
                pygame.mixer.music.play(1,0.0)
                
            elif a[len(a)-1] == 7:
                pygame.mixer.music.load("learn.mp3")
                pygame.mixer.music.play(1,0.0)
                
            elif a[len(a)-1] == 6:
                pygame.mixer.music.load("problem.mp3")
                pygame.mixer.music.play(1,0.0)
               
            elif a[len(a)-1] == 5:
                pygame.mixer.music.load("alright.mp3")
                pygame.mixer.music.play(1,0.0)
                
            elif a[len(a)-1] == 4:
                pygame.mixer.music.load("coo.mp3")
                pygame.mixer.music.play(1,0.0)
                
            elif a[len(a)-1] == 3:
                pygame.mixer.music.load("pig.mp3")
                pygame.mixer.music.play(1,0.0)
                
            elif a[len(a)-1] == 2:
                pygame.mixer.music.load('anyway.mp3')
                pygame.mixer.music.play(1,0.0)
        return score
                            
    def down(self):
        can_combine = [True,True,True,True]
        score = 0
        move_count = -1
        a=[1]
        for j in range(4):
            if '.' not in [self.board[i][j] for i in range(4)] and \
               self.board[0][j] == self.board[1][j] and \
               self.board[2][j] == self.board[3][j]:
                self.board[3][j] *= 2
                self.board[2][j] = self.board[1][j] *2
                self.board[1][j] = '.'
                self.board[0][j] = '.'
                can_combine[j] = False
                score += self.board[3][j] + self.board[2][j]
                if not self.copied:
                    self.game.draw()
       
        while move_count != 0:
            move_count = 0
            a=[1]
            for i in [2,1,0]:
                for j in range(4):
                    if self.board[i][j] != '.':
                        if self.board[i+1][j] == '.':
                            self.board[i][j], self.board[i+1][j] = self.board[i+1][j],self.board[i][j]
                            move_count += 1
                        elif self.board[i+1][j] == self.board[i][j] and can_combine[j]:
                            if self.board[i][j]==512:
                                a.append(9)
                            elif self.board[i][j]==256:
                                a.append(8)
                            elif self.board[i][j]==128:
                                a.append(7)
                            elif self.board[i][j]==64:
                                a.append(6)
                            elif self.board[i][j]==32:
                                a.append(5)    
                            elif self.board[i][j]==16:
                                a.append(4)    
                            elif self.board[i][j]==8:
                                a.append(3)
                            elif self.board[i][j] == 4:
                                a.append(2)
                            self.board[i+1][j] *= 2
                            self.board[i][j] = '.'
                            can_combine[j] = False
                            score += self.board[i+1][j]
                            move_count += 1
                if not self.copied:
                    self.game.draw()
            a.sort()
            if a[len(a)-1] == 9:
                pygame.mixer.music.load("he.mp3")
                pygame.mixer.music.play(1,0.0)
                 
            elif a[len(a)-1] == 8:
                pygame.mixer.music.load("expect.mp3")
                pygame.mixer.music.play(1,0.0)
                
            elif a[len(a)-1] == 7:
                pygame.mixer.music.load("learn.mp3")
                pygame.mixer.music.play(1,0.0)
                
            elif a[len(a)-1] == 6:
                pygame.mixer.music.load("problem.mp3")
                pygame.mixer.music.play(1,0.0)
               
            elif a[len(a)-1] == 5:
                pygame.mixer.music.load("alright.mp3")
                pygame.mixer.music.play(1,0.0)
                
            elif a[len(a)-1] == 4:
                pygame.mixer.music.load("coo.mp3")
                pygame.mixer.music.play(1,0.0)
                
            elif a[len(a)-1] == 3:
                pygame.mixer.music.load("pig.mp3")
                pygame.mixer.music.play(1,0.0)
                
            elif a[len(a)-1] == 2:
                pygame.mixer.music.load('anyway.mp3')
                pygame.mixer.music.play(1,0.0)
        return score
 
    def right(self):
        can_combine = [True,True,True,True]
        score = 0
        move_count = -1
        a=[1]
        for i in range(4):
            if '.' not in [self.board[i][j] for j in range(4)] and \
               self.board[i][0] == self.board[i][1] and \
               self.board[i][2] == self.board[i][3]:
                self.board[i][3] *= 2
                self.board[i][2] = self.board[i][1] *2
                self.board[i][1] = '.'
                self.board[i][0] = '.'
                can_combine[i] = False
                score += self.board[i][3] + self.board[i][2]
                if not self.copied:
                    self.game.draw()
                   
        while move_count != 0:
            move_count = 0
            a=[1]
            for j in [2,1,0]:
                for i in range(4):
                    if self.board[i][j] != '.':
                        if self.board[i][j+1] == '.':
                            self.board[i][j], self.board[i][j+1] = self.board[i][j+1],self.board[i][j]
                            move_count += 1
                        elif self.board[i][j+1] == self.board[i][j] and can_combine[i]:
                            if self.board[i][j]==512:
                                a.append(9)
                            elif self.board[i][j]==256:
                                a.append(8)
                            elif self.board[i][j]==128:
                                a.append(7)
                            elif self.board[i][j]==64:
                                a.append(6)
                            elif self.board[i][j]==32:
                                a.append(5)    
                            elif self.board[i][j]==16:
                                a.append(4)    
                            elif self.board[i][j]==8:
                                a.append(3)
                            elif self.board[i][j] == 4:
                                a.append(2)
                            self.board[i][j+1] *= 2
                            self.board[i][j] = '.'
                            can_combine[i] = False
                            score += self.board[i][j+1]
                            move_count += 1
                if not self.copied:
                    self.game.draw()
            a.sort()
            if a[len(a)-1] == 9:
                pygame.mixer.music.load("he.mp3")
                pygame.mixer.music.play(1,0.0)
                 
            elif a[len(a)-1] == 8:
                pygame.mixer.music.load("expect.mp3")
                pygame.mixer.music.play(1,0.0)
                
            elif a[len(a)-1] == 7:
                pygame.mixer.music.load("learn.mp3")
                pygame.mixer.music.play(1,0.0)
                
            elif a[len(a)-1] == 6:
                pygame.mixer.music.load("problem.mp3")
                pygame.mixer.music.play(1,0.0)
               
            elif a[len(a)-1] == 5:
                pygame.mixer.music.load("alright.mp3")
                pygame.mixer.music.play(1,0.0)
                
            elif a[len(a)-1] == 4:
                pygame.mixer.music.load("coo.mp3")
                pygame.mixer.music.play(1,0.0)
                
            elif a[len(a)-1] == 3:
                pygame.mixer.music.load("pig.mp3")
                pygame.mixer.music.play(1,0.0)
                
            elif a[len(a)-1] == 2:
                pygame.mixer.music.load('anyway.mp3')
                pygame.mixer.music.play(1,0.0)
        return score
                       
   
class Cell(pygame.sprite.Sprite):
    colors = {'.':'orange', 2:'green',4:'deepskyblue',8:'red',16:'cornsilk',32:'blue', 64:'gray60',
              128:'hotpink', 256:'khaki4', 512:'olivedrab1', 1024:'plum4', 2048: 'turquoise4',4096:'gold'}
    def __init__(self, pos, width=100, height=100, value=2):
        myFont = pygame.font.Font('freesansbold.ttf', 48)
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.value = value
        self.rect = Rect(0,0,self.width, self.height)
        self.rect.center = pos
        self.image = pygame.Surface(self.rect.size)
        self.image.fill(Color(self.colors[self.value]))
       
        self.label = myFont.render(str(self.value), 1, (100,100,100))
        self.labelrect = self.label.get_rect()
        self.imagerect = self.image.get_rect()
        self.labelrect.center = self.imagerect.center
        if self.value != '.':
            self.image.blit(self.label, self.labelrect)
    def update(self, direction):
        pass
 
class GameMain():
    done = False
    color_bg = Color('gray30')
    
    def __init__(self, width=550, height=550, high_score = 0):
        pygame.init()
        self.game_over = False
        self.font = pygame.font.Font('freesansbold.ttf', 24)
        self.width, self.height = width, height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.board = Board(self)
        self.score = 0
        try:
            if high_score == 0:
                with open("high_score.txt", "rb") as f:
                    self.high_score = int(f.read().strip())
        except:
            self.high_score = high_score
 
    def draw_board(self):
        self.cells = pygame.sprite.Group()
 
        cur_x, cur_y = 100,100
        for row in self.board.board:
            for square in row:
                new_cell = Cell((cur_x, cur_y), value = square)
                self.cells.add(new_cell)
                cur_x += 110
            cur_y += 110
            cur_x = 100
        self.cells.draw(self.screen)    
 
    def main_loop(self):
        while not self.done:
            self.handle_events()
           
            if self.score > self.high_score:
                self.high_score = self.score
               
            self.draw()
            self.clock.tick(30)
            if self.board.no_moves():
                self.game_over = True
                self.end_screen = pygame.Surface((500,500))
                self.end_screen_rect = self.end_screen.get_rect()
                # self.done = True
        with open("high_score.txt", 'wb') as f:
            f.write(str(self.high_score))
        pygame.quit()
        sys.exit()
 
    def draw(self):
        self.screen.fill(self.color_bg)
        if self.game_over:
            self.game_over_label1 = self.font.render("Game Over", 1, WHITE)
            self.game_over_label2 = self.font.render("Final Score: %d" % (self.score), 1, WHITE)
            self.game_over_label3 = self.font.render("Press Space Bar to Play Again", 1, WHITE)
            self.end_screen.blit(self.game_over_label1, (175,50))
            self.end_screen.blit(self.game_over_label2, (150,100))
            self.end_screen.blit(self.game_over_label3, (75,470))
            self.screen.blit(self.end_screen, (25,25))
        else:
            self.draw_board()
            self.score_label = self.font.render("Score: %d" % (self.score), 1, WHITE)
            self.screen.blit(self.score_label, (50,10))
            self.hiscore_label = self.font.render("High Score: %d" % (self.high_score), 1, WHITE)
            self.screen.blit(self.hiscore_label, (320,10))
        pygame.display.update()
 
    def handle_events(self):
        events = pygame.event.get()
        keys = pygame.key.get_pressed()
        for event in events:
            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == KEYDOWN and not self.game_over:
                if event.key == K_ESCAPE:
                    self.done = True
                elif event.key in [K_UP,K_DOWN,K_LEFT,K_RIGHT]:
                    self.current_board = copy.deepcopy(self.board.board)
                    if event.key == K_UP:
                        self.score += self.board.up()
                    elif event.key == K_DOWN:
                        self.score += self.board.down()
                    elif event.key == K_LEFT:
                        self.score += self.board.left()
                    elif event.key == K_RIGHT:
                        self.score += self.board.right()                     
                    if self.current_board != self.board.board:
                        self.board.create_random()
            elif event.type == KEYDOWN and self.game_over:
                if event.key == K_SPACE:
                    self.__init__(high_score = self.high_score)
                   
class Point3D:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x, self.y, self.z = float(x), float(y), float(z)
 
    def rotateX(self, angle):
        """ Rotates the point around the X axis by the given angle in degrees. """
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        y = self.y * cosa - self.z * sina
        z = self.y * sina + self.z * cosa
        return Point3D(self.x, y, z)
 
    def rotateY(self, angle):
        """ Rotates the point around the Y axis by the given angle in degrees. """
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        z = self.z * cosa - self.x * sina
        x = self.z * sina + self.x * cosa
        return Point3D(x, self.y, z)
 
    def rotateZ(self, angle):
        """ Rotates the point around the Z axis by the given angle in degrees. """
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        x = self.x * cosa - self.y * sina
        y = self.x * sina + self.y * cosa
        return Point3D(x, y, self.z)
 
    def project(self, win_width, win_height, fov, viewer_distance):
        """ Transforms this 3D point to 2D using a perspective projection. """
        factor = fov / (viewer_distance + self.z)
        x = self.x * factor + win_width / 2
        y = -self.y * factor + win_height / 2
        return Point3D(x, y, self.z)
'animation below'
class Simulation:
    def __init__(self, win_width = 550, win_height = 550):
        pygame.init()

        self.screen = pygame.display.set_mode((win_width, win_height))
        pygame.display.set_caption("2048")
    
        self.clock = pygame.time.Clock()

        self.vertices = [
            Point3D(-1,1,-1),
            Point3D(1,1,-1),
            Point3D(1,-1,-1),
            Point3D(-1,-1,-1),
            Point3D(-1,1,1),
            Point3D(1,1,1),
            Point3D(1,-1,1),
            Point3D(-1,-1,1)
        ]

        self.faces  = [(0,1,2,3),(1,5,6,2),(5,4,7,6),(4,0,3,7),(0,4,5,1),(3,2,6,7)]

        self.images = [(255,255,255),(0,0,0),(255,255,255),(0,0,0),(255,255,255),(0,0,0)]

        self.angle = 0
        
    def run(self):
        """ Main Loop """
        pygame.mixer.music.load("65daysofstatic - Heat Death Infinity Splitter2.mp3")
        pygame.mixer.music.play(2,0.0)
        while 1:
            for event in pygame.event.get():
             
                if (event.type == KEYUP) or (event.type == KEYDOWN):
                         
                    game = GameMain()
                    game.main_loop()
                    break
           
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.clock.tick(100)
            self.screen.fill((50,50,50))

            t = []
            
            for v in self.vertices:
                r = v.rotateX(self.angle).rotateY(self.angle).rotateZ(self.angle)
                p = r.project(self.screen.get_width(), self.screen.get_height(), 256, 4)
                t.append(p)

            avg_z = []
            i = 0
            for f in self.faces:
                z = (t[f[0]].z + t[f[1]].z + t[f[2]].z + t[f[3]].z) / 4.0
                avg_z.append([i,z])
                i = i + 1

            for tmp in sorted(avg_z,key=itemgetter(1),reverse=True):
                face_index = tmp[0]
                f = self.faces[face_index]
                pointlist = [(t[f[1]].x, t[f[0]].y), (t[f[1]].x, t[f[0]].y),
                             (t[f[0]].x, t[f[1]].y), (t[f[2]].x, t[f[2]].y),
                             (t[f[2]].x, t[f[2]].y), (t[f[3]].x, t[f[3]].y),
                             (t[f[3]].x, t[f[3]].y), (t[f[0]].x, t[f[1]].y)]
                pygame.draw.polygon(self.screen,self.images[face_index],pointlist)

                
            self.angle += 1

            pygame.display.flip()

if __name__ == "__main__":
    Simulation().run()   