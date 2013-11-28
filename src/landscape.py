from pygame.locals import *
import pygame, load, block

block = block.Block(600,38)

class landscape(pygame.sprite.Sprite):
    def __init__(self):
        self.scene1 = load.load_scene("scene1.png")
        self.background1 = load.load_scene("background1.png")
        self.x = 0
        self.y = 312

    def create(self,screen,spriteGroup):
        block.rect.x = 0
        block.rect.y = 362
        spriteGroup.landscape.add(block)
        if self.x == -600:
            self.x = 0
        screen.blit(self.background1,(self.x,0))
        screen.blit(self.background1,(self.x+600,0))
        screen.blit(self.scene1,(self.x,self.y))
        screen.blit(self.scene1,(self.x+600,self.y))
        self.x -= 3
        
    
