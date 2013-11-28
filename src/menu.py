import pygame, os, sys, load
from pygame.locals import *

class menu(object):
    def __init__(self):
        self.menu1 = load.load_image("menu1.png")
        self.menu2 = load.load_image("menu2.png")
        self.menu3 = load.load_image("menu3.png")
        self.menu = [self.menu1,self.menu2,self.menu3]
        self.index = 0
        self.start = False

    def run(self,screen,event,key):
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                self.index += 1
            if event.key == K_UP:
                self.index -= 1
        """if key[pygame.K_DOWN]:
            self.index += 1
        if key[pygame.K_UP]:
            self.index -= 1"""
        screen.blit(self.menu[self.index%3],(0,0))
        if self.index%3 == 0 and key[pygame.K_RETURN]:
            self.start = True
        elif self.index%3 == 2 and key[pygame.K_RETURN]:
            sys.exit()
        
        
