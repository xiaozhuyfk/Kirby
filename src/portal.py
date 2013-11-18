import pygame, load, math
from pygame.locals import *

class portal(pygame.sprite.Sprite):
    def __init__(self,start,end):
        pygame.sprite.Sprite.__init__(self)
        self.start = start
        self.end = end
        self.center = ((self.start[0]+self.end[0])/2,(self.start[1]+self.end[1])/2)
        self.images =[load.load_image("red_1.png"),load.load_image(
                "red_2.png"), load.load_image("red_3.png")]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = self.center
        if end[0]-start[0] != 0:
            self.slope = float(end[1] - start[1])/(end[0]-start[0])
        else:
            self.slope = float(end[1] - start[1])/(end[0]-start[0]+0.1)
        self.angle = math.atan(self.slope)
        if self.start <= self.end:
            self.up = 1                     # self.up tells you the position
        if self.start > self.end:
            self.up =0
    def anim(self,screen,event,FRAME):
        if self.up:
            surface = pygame.transform.rotate(self.images[FRAME/15%3],-self.angle/math.pi*180)
        else:
            surface = pygame.transform.rotate(self.images[FRAME/15%3],180-self.angle/math.pi*180)
        screen.blit(surface,(self.center[0]-28,self.center[1]-26))

class portal2(pygame.sprite.Sprite):
    def __init__(self,start,end):
        pygame.sprite.Sprite.__init__(self)
        self.start = start
        self.end = end
        self.center = ((self.start[0]+self.end[0])/2,(self.start[1]+self.end[1])/2)
        self.images =[load.load_image("blue_1.png"),load.load_image(
                "blue_2.png"), load.load_image("blue_3.png")]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = self.center
        if end[0]-start[0] != 0:
            self.slope = float(end[1] - start[1])/(end[0]-start[0])
        else:
            self.slope = float(end[1] - start[1])/(end[0]-start[0]+0.1)
        self.angle = math.atan(self.slope)
        if self.start <= self.end:
            self.up = 1                     # self.up tells you the position
        if self.start > self.end:
            self.up =0
    def anim(self,screen,event,FRAME):
        if self.up:
            surface = pygame.transform.rotate(self.images[FRAME/15%3],-self.angle/math.pi*180)
        else:
            surface = pygame.transform.rotate(self.images[FRAME/15%3],180-self.angle/math.pi*180)
        screen.blit(surface,(self.center[0]-28,self.center[1]-26))

    
    
