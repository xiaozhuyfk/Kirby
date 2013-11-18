from pygame.locals import *
import pygame, load, block, spriteGroup, kirby

block = block.Block(69,56)

class Hand(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.hand1 = load.load_image("hand1.png")
        self.hand2 = load.load_image("hand2.png")
        self.hand3 = load.load_image("hand3.png")
        self.hand4 = load.load_image("hand4.png")
        self.hand = [self.hand1,self.hand4]

        self.frame = 0

    def cursor(self,pos,event,screen):
        x, y = pos
        cursor_x = x - self.hand1.get_width()*2/7
        cursor_y = y - self.hand1.get_height()*5/7
        block.rect.x = x-10
        block.rect.y = y-10
        
        if event.type == MOUSEBUTTONDOWN:
            self.frame = 1
            """if pygame.sprite.spritecollide(block,spriteGroup.spriteGroup().player,False):
                kirby.kirby().x = x
                kirby.kirby().y = y"""
        elif event.type == MOUSEBUTTONUP:
            self.frame = 0
        screen.blit(self.hand[self.frame%2],(cursor_x,cursor_y))
