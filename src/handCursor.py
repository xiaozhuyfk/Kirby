from pygame.locals import *
import pygame, load, block
import kirby
import spriteGroup
import time

block = block.Block(8,8)

class Hand(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.hand1 = load.load_image("hand1.png")
        self.hand2 = load.load_image("hand2.png")
        self.hand3 = load.load_image("hand3.png")
        self.hand4 = load.load_image("hand4.png")
        self.hand = [self.hand1,self.hand4]
        self.frame_hand = 0
        self.grab = False

    def cursor(self,pos,event,screen,kirby,spriteGroup):
        x, y = pos
        cursor_x = x - self.hand1.get_width()*2/7
        cursor_y = y - self.hand1.get_height()*5/7
        block.rect.x = x-4
        block.rect.y = y-4
        spriteGroup.handCursor.add(block)
        if event[0] == 1:
            self.frame_hand = 1
            if pygame.sprite.spritecollide(block,spriteGroup.player,False):
                self.grab = True
            if self.grab:
                kirby.x = x-13
                kirby.y = y-13
                kirby.speed_y = 0
                kirby.speed_y2 = 0
        elif event[0] == 0:
            self.frame_hand = 0
            self.grab = False
        screen.blit(self.hand[self.frame_hand%2],(cursor_x,cursor_y))
        #spriteGroup.handCursor.draw(screen)

    def drawCircle(self,pos,event,screen,kirby,spriteGroup):
        x, y = pos
        if event[0] == 1:
            block = block.Block(8,8)
            block.rect.x = x-4
            block.rect.y = y-4
            spriteGroup.circlePixel.add(block)
            self.startTime = time.time()
        else:
            self.endTime = time.time()
            
        
