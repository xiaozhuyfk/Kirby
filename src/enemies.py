from pygame.locals import *
import pygame, load, block
import math


class pikey(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.pikey1 = load.load_image("pikey1.png")
        self.pikey2 = load.load_image("pikey2.png")
        self.pikey = [self.pikey1,self.pikey1,self.pikey2,self.pikey2]
        self.frame = 0
        self.sprite = block.Block(19,19)
        self.x = x
        self.y = y
        self.speed_y = 3
        self.gravity = 0.5
        self.localGrab = False
        self.air = False
        self.dead = False

    def drag(self,spriteGroup,hand,event):
        if pygame.sprite.spritecollide(self.sprite,spriteGroup.handCursor,False)\
                and event[0] == 1 and hand.grab == False:
            hand.grab = True
            self.localGrab = True
        if self.localGrab:
            self.x = hand.x-9
            self.y = hand.y-9
        if self.localGrab and hand.grab == False:
            self.localGrab = False
            self.air = True

    def throw(self,spriteGroup,hand,event):
        pass
    # This function gives the movement of the pikey
    def movement(self,screen,spriteGroup,hand,event):
        self.drag(spriteGroup,hand,event)
        if self.air == False and self.localGrab == False:
            self.sprite.rect.x = self.x + 3
            self.sprite.rect.y = self.y + 3
            spriteGroup.enemies.add(self.sprite)
            # Pikey bouncing up and down
            if self.y < 270:
                self.speed_y = -self.speed_y
            if self.y > 336:
                self.y = 336
                self.speed_y = -self.speed_y
            self.y += self.speed_y
        elif self.air:
            self.y += self.speed_y
            self.speed_y += self.gravity
            if self.y > 336:
                self.speed_y = 336
                self.speed_y = 3
                self.air = False
        self.x -= 3
        screen.blit(self.pikey[self.frame%4],(self.x,self.y))
        if pygame.sprite.spritecollide(self.sprite,spriteGroup.sparkshield,False):
            self.dead = True
        self.frame += 1
        
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
        self.shotzo = [self.shotzo1, self.shotzo2, self.shotzo6,
                       self.shotzo7, self.shotzo4]
        self.sprite1 = block.Block(20,20)
        self.sprite2 = block.Block(8,8)
        self.x = x
        self.y = y
        self.x2 = self.x
        self.y2 = self.y
        self.frame = 0
        self.dir = (0,0)

    # This function makes shotzo's movement
    def movement(self,screen,spriteGroup,kirby):
        d_x = self.x - kirby.x
        d_y = self.y - kirby.y
        # The shotzo changes direction according to the kirby's position
        if d_x > 0 and 1.0*d_y/d_x < 1:
            index = 0
            self.dir = (-1,0)
        elif d_x > 0 and 1.0*d_y/d_x >= 1:
            index = 1
            self.dir = (-1,-1)
        elif d_x < 0 and 1.0*d_y/abs(d_x) >= 1:
            index = 2
            self.dir = (1,-1)
        elif d_x < 0 and 1.0*d_y/abs(d_x) < 1:
            index = 3
            self.dir = (1,0)
        elif d_x == 0:
            index = 4
            self.dir = (0,-1)
        screen.blit(self.shotzo[index],(self.x,self.y))
        #self.shoot(screen,spriteGroup)
        self.x -= 3
        self.sprite1.rect.x = self.x+3
        self.sprite1.rect.y = self.y+3
        spriteGroup.enemies.add(self.sprite1)
        #spriteGroup.enemies.draw(screen)
        self.frame += 1

class bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,dir):
        self.bullet = load.load_image("shotzoBullet.png")
        self.x = x+13
        self.y = y+5
        self.sprite = block.Block(6,6)
        self.speed_x = 5*dir[0]/math.hypot(*dir)
        self.speed_y = 5*dir[1]/math.hypot(*dir)
        self.dead = False
        self.frame = 0
        
    def shoot(self,screen,spriteGroup):
        self.sprite.rect.x = self.x-4
        self.sprite.rect.y = self.y-4
        spriteGroup.enemies.add(self.sprite)
        self.x += self.speed_x
        self.y += self.speed_y
        self.x -= 3
        screen.blit(self.bullet,(self.x,self.y))
        if self.x < -26 or self.x > 626:
            self.dead = True
        if pygame.sprite.spritecollide(self.sprite,spriteGroup.player,False):
            self.dead = True

class waddleDee(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.waddleDee1 = load.load_image("waddleDee1.png")
        self.waddleDee2 = load.load_image("waddleDee2.png")
        self.waddleDee3 = load.load_image("waddleDee3.png")
        self.waddleDee4 = load.load_image("waddleDee4.png")
        self.waddleDee5 = load.load_image("waddleDee5.png")
        self.waddleDee = [self.waddleDee1,self.waddleDee2,
                          self.waddleDee3,self.waddleDee4]
        self.frame = 0
        self.sprite = block.Block(17,17)
        self.x = x
        self.y = y
        self.speed_y = 3
        self.gravity = 0.5
        self.localGrab = False
        self.air = False
        self.dead = False

    def drag(self,spriteGroup,hand,event):
        if pygame.sprite.spritecollide(self.sprite,spriteGroup.handCursor,False)\
                and event[0] == 1 and hand.grab == False:
            hand.grab = True
            self.localGrab = True
        if self.localGrab:
            self.x = hand.x-9
            self.y = hand.y-9
        if self.localGrab and hand.grab == False:
            self.localGrab = False
            self.air = True

    def throw(self,spriteGroup,hand,event):
        pass
    # This function gives the movement of the pikey
    def movement(self,screen,spriteGroup,hand,event):
        self.drag(spriteGroup,hand,event)
        if self.air == False and self.localGrab == False:
            self.sprite.rect.x = self.x + 3
            self.sprite.rect.y = self.y + 3
            spriteGroup.enemies.add(self.sprite)
            # Pikey bouncing up and down
            if self.y < 270:
                self.speed_y = -self.speed_y
            if self.y > 336:
                self.y = 336
                self.speed_y = -self.speed_y
            self.y += self.speed_y
        elif self.air:
            self.y += self.speed_y
            self.speed_y += self.gravity
            if self.y > 336:
                self.speed_y = 336
                self.speed_y = 3
                self.air = False
        self.x -= 3
        screen.blit(self.pikey[self.frame%4],(self.x,self.y))
        if pygame.sprite.spritecollide(self.sprite,spriteGroup.sparkshield,False):
            self.dead = True
        self.frame += 1
        
        
        
    
        
