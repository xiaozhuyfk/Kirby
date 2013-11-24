from pygame.locals import *
import pygame, load, block
import kirby
import spriteGroup
import time

block1 = block.Block(12,12)

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
        self.circle_x = []
        self.circle_y = []
        self.block1 = block.Block(12,12)
        self.vector = (0,0)
        self.startPos = (0,0)
        self.endPos = (0,0)
        self.startTime = 0
        self.endTime = 0

    def cursor(self,pos,event,screen,kirby,spriteGroup):
        x, y = pos
        self.x, self.y = x, y
        self.event = event
        cursor_x = x - self.hand1.get_width()*2/7
        cursor_y = y - self.hand1.get_height()*5/7
        self.block1.rect.x = x-6
        self.block1.rect.y = y-6
        spriteGroup.handCursor.add(self.block1)
        if event[0] == 1:
            self.frame_hand = 1
            self.startPos = (x, y)
            self.startTime = time.time()
        elif event[0] == 0:
            self.frame_hand = 0
            self.grab = False
            self.endPos = (x,y)
            self.vector = (self.endPos[0]-self.startPos[0],
                           self.endPos[1]-self.startPos[1])
            self.endTime = time.time()
            delta = self.endTime - self.startTime
            self.vector = ((self.endPos[0]-self.startPos[0])/delta,
                           (self.endPos[1]-self.startPos[1])/delta)

        screen.blit(self.hand[self.frame_hand%2],(cursor_x,cursor_y))
        #spriteGroup.handCursor.draw(screen)

    def drag(self,event,spriteGroup):
        if event[0] == 1:
            self.frame_hand = 1
        elif event[0] == 0:
            self.frame_hand = 0
            self.grab = False

    def drawCircle(self,pos,event,screen,kirby,spriteGroup):
        x, y = pos
        if event[0] == 1:
            block2 = block.Block(8,8)
            block2.rect.x = x-4
            block2.rect.y = y-4
            spriteGroup.circlePixel.add(block2)
            self.circle_x.append(x)
            self.circle_y.append(y)
        else:
            for element in spriteGroup.circlePixel:
                spriteGroup.circlePixel.remove(element)
            
