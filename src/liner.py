import pygame, load
from pygame.locals import *


class liner(object):
    def __init__(self):
        self.start = None
        

    def setStart(self,start):
        self.start = start
        
    def setCurrent(self, current):
        self.current = current

    def update(self,screen,event):
        self.line = pygame.draw.line(screen,(255,0,0),(int(self.start[0]),int(self.start[1])),(int(self.current[0]),int(self.current[1])))

