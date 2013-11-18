from pygame.locals import *
import pygame, load, block

class pikey(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.pikey1 = load.load_image("pickey1.png")
        self.pikey2 = load.load_image("pickey2.png")
        self.pikey = [self.pikey1,self.pikey2]
        self.x = x
        self.y = y
        self.frame = 0
        self.block = block.Block(25,25)
    def movement(self,screen,spriteGroup):
        screen.blit(self.pikey[self.frame%2],(self.x,self.y))
        self.frame += 1
        self.x -= 3
        self.block.rect.x = self.x
        self.block.rect.y = self.y
        spriteGroup.enemies.add(self.block)
        
class shotzo(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.shotzo1 = load.load_image("shotzo1.png")
        self.shotzo2 = load.load_image("shotzo2.png")
        self.shotzo3 = load.load_image("shotzo3.png")
        self.shotzo4 = load.load_image("shotzo4.png")
        self.shotzo5 = load.load_image("shotzo5.png")
        self.shotzo6 = load.load_image("shotzo6.png")
        self.shotzo7 = load.load_image("shotzo7.png")
        self.bullet = load.load_image("shotzoBullet.png")
        self.shotzo = [self.shotzo1, self.shotzo2, self.shotzo3,
                       self.shotzo4, self.shotzo5, self.shotzo6,
                       self.shotzo7]
        self.block = block.Block(26,26)

    def movement(self,spriteGroup):
        self.x -= 3
        self.block.rect.x = self.x
        self.block.rect.y = self.y
        spriteGroup.enemies.add(self.block)
