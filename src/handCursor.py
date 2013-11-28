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

        self.fist1 = load.load_image("fist1.png")
        self.fist2 = load.load_image("fist2.png")
        self.fist3 = load.load_image("fist3.png")
        self.fist4 = load.load_image("fist4.png")
        self.fist5 = load.load_image("fist5.png")
        self.fist = [self.hand1,self.fist1,self.fist2,self.fist3,
                     self.fist4,self.fist5,self.fist5,self.fist5,
                     self.fist5]
        self.fistState = False
        self.fistEnd = False
        self.x2, self.y2 = 0, 0
        self.sprite = block.Block(45,45)
        self.speed_y = 15
        self.frame = 0
        self.frame_end = 0

    def hit(self,screen,spriteGroup):
        if self.y2 > 307:
            self.fistEnd = True
            self.y2 = 307
        elif self.fistEnd == False:
            self.y2 += self.speed_y
        if self.frame%9 != 7:
            self.frame += 1
        if self.fistEnd:
            spriteGroup.fist.empty()
            self.frame_end += 1
        if self.frame_end > 10:
            self.fistState = False
            self.frame_end = 0
            self.frame = 0
        screen.blit(self.fist[self.frame%9],(self.x2,self.y2))
        self.sprite.rect.x = self.x2+5
        self.sprite.rect.y = self.y2+10
        if self.fistEnd == False:
            spriteGroup.fist.add(self.sprite)
        
    def cursor(self,pos,event,screen,kirby,spriteGroup):
        #spriteGroup.fist.draw(screen)
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
            self.fistState = False
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
        if event[2] == 1 and cursor_y < 307:
            self.fistState = True
            self.x2, self.y2 = cursor_x, cursor_y
            self.frame, self.frame_end = 0, 0
        if self.fistState == False:
            screen.blit(self.hand[self.frame_hand%2],(cursor_x,cursor_y))
            spriteGroup.fist.empty()
            self.fistEnd = False
        else:
            self.hit(screen,spriteGroup)
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
            
