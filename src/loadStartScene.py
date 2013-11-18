import pygame,os,sys,kirby,load
from pygame.locals import *

class loadStartScene(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.startScene1 = load.load_scene("startScene1.png")
        self.startScene2 = load.load_scene("startScene2.png")
        self.x = 0
        self.y = 0

    def update(self,screen):
        screen.blit(self.startScene2, (self.x,self.y))
        screen.blit(self.startScene1, (self.x,self.y))
        
        
    
