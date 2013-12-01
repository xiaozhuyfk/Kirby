import pygame, os, sys, load
from pygame.locals import *

class menu(object):
    def __init__(self):
        self.menu1 = load.load_image("menu1.png")
        self.menu2 = load.load_image("menu2.png")
        self.menu3 = load.load_image("menu3.png")
        self.menu = [self.menu1,self.menu2,self.menu3]
        self.instruction = load.load_image("instruction.png")
        self.index = 0
        self.start = False
        self.info = False
        self.menuSound = load.load_sound("menuDing.WAV")
        self.enter = False

    def run(self,screen,event,key):
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                self.index += 1
            if event.key == K_UP:
                self.index -= 1
            if event.key == K_RETURN:
                self.enter = True
        if event.type == KEYUP:
            if event.key == K_RETURN:
                self.enter = False
        screen.blit(self.menu[self.index%3],(0,0))
        if self.index%3 == 0 and self.enter:
            self.start = True
        elif self.index%3 == 2 and self.enter:
            sys.exit()
        elif self.index%3 == 1 and self.enter:
            self.info = True
        if self.info:
            screen.blit(self.instruction,(50,25))
        if self.info and key[pygame.K_ESCAPE]:
            self.info = False
        
        
