# 15-112 Term Project
# Hongyu Li + hongyul + Section J

# enemies.py

from pygame.locals import *
import pygame, load, block
import math

# Pikey Class
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
        self.speed_x = 0
        self.speed_y = 3
        self.gravity = 0.3
        self.localGrab = False
        self.air = False
        self.dead = False
        self.v_x = 0
        self.v_y = 0

    # drag function
    def drag(self,spriteGroup,hand,event):
        if pygame.sprite.spritecollide(self.sprite,spriteGroup.handCursor,False)\
                and event[0] == 1 and hand.grab == False:
            hand.grab = True
            self.localGrab = True
        if self.localGrab: # if grabed, follow the hand cursor
            self.x = hand.x-9
            self.y = hand.y-9
        # if released, create vectors
        if self.localGrab and hand.grab == False:
            self.v_x, self.v_y = hand.vector[0], hand.vector[1]
            self.speed_y += self.v_y
            self.localGrab = False
            self.air = True

    # Movement function
    def movement(self,screen,spriteGroup,hand,event):
        self.drag(spriteGroup,hand,event)
        if self.air == False and self.localGrab == False:
            # Pikey bouncing up and down
            if self.y < 270:
                self.speed_y = -self.speed_y
            if self.y > 336:
                self.y = 336
                self.speed_y = -self.speed_y
            self.x += self.speed_x
            self.y += self.speed_y
        elif self.air: # if in the air, follows the gravity
            self.x += self.v_x
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
        self.sprite.rect.x = self.x 
        self.sprite.rect.y = self.y 
        spriteGroup.enemies.add(self.sprite)

# Shotzo class
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
        self.x -= 3
        self.sprite1.rect.x = self.x+3
        self.sprite1.rect.y = self.y+3
        spriteGroup.enemies.add(self.sprite1)
        self.frame += 1

# Shotzo's bullet class
class bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,dir):
        self.bullet = load.load_image("shotzoBullet.png")
        self.x = x+13
        self.y = y+5
        self.sprite = block.Block(6,6)
        # calculate the speed according to the input direction
        self.speed_x = 5*dir[0]/math.hypot(*dir)
        self.speed_y = 5*dir[1]/math.hypot(*dir)
        self.dead = False
        self.frame = 0

    # shoot function for the bullet
    def shoot(self,screen,spriteGroup):
        self.x += self.speed_x
        self.y += self.speed_y
        self.x -= 3
        screen.blit(self.bullet,(self.x,self.y))
        if self.x < -26 or self.x > 626:
            self.dead = True
        # Remove the bullet if collided with Kirby or the spark
        if pygame.sprite.spritecollide(self.sprite,spriteGroup.player,False):
            spriteGroup.enemies.remove(self.sprite)
            self.dead = True
        if pygame.sprite.spritecollide(self.sprite,spriteGroup.sparkshield,False):
            self.dead = True
        self.sprite.rect.x = self.x+4
        self.sprite.rect.y = self.y+4
        spriteGroup.enemies.add(self.sprite)

class waddleDee(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.loadImage()                  
        self.frame = 0
        self.sprite = block.Block(17,17)
        self.x = x
        self.y = y
        self.speed_x = 2
        self.speed_y = 3
        self.gravity = 0.3
        self.localGrab = False
        self.air = False
        self.dead = False
        self.left = True
        self.v_x = 0
        self.v_y = 0

    # load images
    def loadImage(self):
        self.waddleDee1 = load.load_image("waddleDee1.png")
        self.waddleDee2 = load.load_image("waddleDee2.png")
        self.waddleDee3 = load.load_image("waddleDee3.png")
        self.waddleDee4 = load.load_image("waddleDee4.png")
        self.waddleDee5 = load.load_image("waddleDee5.png")
        self.waddleDee1i = load.load_image("waddleDee1i.png")
        self.waddleDee2i = load.load_image("waddleDee2i.png")
        self.waddleDee3i = load.load_image("waddleDee3i.png")
        self.waddleDee4i = load.load_image("waddleDee4i.png")
        self.waddleDee5i = load.load_image("waddleDee5i.png")
        self.waddleDee = [self.waddleDee1,self.waddleDee1,
                          self.waddleDee2,self.waddleDee2,
                          self.waddleDee3,self.waddleDee3,
                          self.waddleDee4,self.waddleDee4]
        self.waddleDeei = [self.waddleDee1i,self.waddleDee1i,
                           self.waddleDee2i,self.waddleDee2i,
                           self.waddleDee3i,self.waddleDee3i,
                           self.waddleDee4i,self.waddleDee4i]

    # Drag function
    def drag(self,spriteGroup,hand,event):
        if pygame.sprite.spritecollide(self.sprite,spriteGroup.handCursor,False)\
                and event[0] == 1 and hand.grab == False:
            hand.coordList = []
            hand.grab = True
            self.localGrab = True
        if self.localGrab: # if grabed, follows the hand cursor
            self.x = hand.x-9
            self.y = hand.y-9
        # if released, create vector
        if self.localGrab and hand.grab == False:
            self.v_x, self.v_y = hand.vector[0], hand.vector[1]
            self.speed_y += self.v_y
            self.localGrab = False
            self.air = True

    def checkState(self):
        # if not in the air and not grabed, moves back and forth
        if self.air == False and self.localGrab == False:
            if self.y > 336:
                self.y = 336
            if self.frame % 50 == 1:
                self.speed_x = -self.speed_x
                self.left = not self.left
            self.x -= self.speed_x
        elif self.air: # if in the air, follows the gravity
            self.x += self.v_x
            self.y += self.speed_y
            self.speed_y += self.gravity
            if self.y > 336:
                self.speed_y = 336
                self.speed_y = 3
                self.air = False
        
    # Movement function
    def movement(self,screen,spriteGroup,hand,event):
        self.drag(spriteGroup,hand,event)
        self.checkState()
        self.x -= 3
        if self.left:
            screen.blit(self.waddleDee[self.frame%8],(self.x,self.y))
        else:
            screen.blit(self.waddleDeei[self.frame%8],(self.x,self.y))
        if pygame.sprite.spritecollide(self.sprite,spriteGroup.sparkshield,False):
            self.dead = True
        if pygame.sprite.spritecollide(self.sprite,spriteGroup.fist,False):
            self.dead = True
        self.frame += 1
        # add the collision rect into sprite group
        self.sprite.rect.x = self.x + 3
        self.sprite.rect.y = self.y + 3
        spriteGroup.enemies.add(self.sprite)

# WaddleDoo Class
class waddleDoo(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.loadImage()
        self.frame = 0
        self.sprite = block.Block(18,18)
        self.x = x
        self.y = y
        self.speed_x = 2
        self.speed_y = 3
        self.gravity = 0.3
        self.localGrab = False
        self.air = False
        self.dead = False
        self.left = True
        self.v_x = 0
        self.v_y = 0

    def loadImage(self):
        self.waddleDoo1 = load.load_image("waddleDoo1.png")
        self.waddleDoo2 = load.load_image("waddleDoo2.png")
        self.waddleDoo3 = load.load_image("waddleDoo3.png")
        self.waddleDoo4 = load.load_image("waddleDoo4.png")
        self.waddleDoo5 = load.load_image("waddleDoo5.png")
        self.waddleDoo1i = load.load_image("waddleDoo1i.png")
        self.waddleDoo2i = load.load_image("waddleDoo2i.png")
        self.waddleDoo3i = load.load_image("waddleDoo3i.png")
        self.waddleDoo4i = load.load_image("waddleDoo4i.png")
        self.waddleDoo5i = load.load_image("waddleDoo5i.png")
        self.waddleDoo = [self.waddleDoo1,self.waddleDoo1,
                          self.waddleDoo2,self.waddleDoo2,
                          self.waddleDoo3,self.waddleDoo3,
                          self.waddleDoo4,self.waddleDoo4,
                          self.waddleDoo5,self.waddleDoo5]
        self.waddleDooi = [self.waddleDoo1i,self.waddleDoo1i,
                           self.waddleDoo2i,self.waddleDoo2i,
                           self.waddleDoo3i,self.waddleDoo3i,
                           self.waddleDoo4i,self.waddleDoo4i,
                           self.waddleDoo5i,self.waddleDoo5i]

    # Drag Function
    def drag(self,spriteGroup,hand,event):
        if pygame.sprite.spritecollide(self.sprite,spriteGroup.handCursor,False)\
                and event[0] == 1 and hand.grab == False:
            hand.grab = True
            self.localGrab = True
        if self.localGrab: # if grabed, follows the hand cursor
            self.x = hand.x-9
            self.y = hand.y-9
        # if released, create vector
        if self.localGrab and hand.grab == False:
            self.v_x, self.v_y = hand.vector[0], hand.vector[1]
            self.speed_y += self.v_y
            self.localGrab = False
            self.air = True

    def checkState(self):
        # if not in the air and not grabed, moves back and forth
        if self.air == False and self.localGrab == False:
            if self.y > 336:
                self.y = 336
            if self.frame % 60 == 1:
                self.speed_x = -self.speed_x
                self.left = not self.left
            self.x -= self.speed_x
        elif self.air: # if in the air, follows the gravity
            self.x += self.v_x
            self.y += self.speed_y
            self.speed_y += self.gravity
            if self.y > 336:
                self.speed_y = 336
                self.speed_y = 3
                self.air = False

    # Movement function
    def movement(self,screen,spriteGroup,hand,event):
        self.drag(spriteGroup,hand,event)
        self.checkState()
        self.x -= 3
        if self.localGrab == False:
            if self.left:
                screen.blit(self.waddleDoo[self.frame%10],(self.x,self.y))
            else:
                screen.blit(self.waddleDooi[self.frame%10],(self.x,self.y))
        else:
            if self.left:
                screen.blit(self.waddleDoo5,(self.x,self.y))
            else:
                screen.blit(self.waddleDoo5i,(self.x,self.y))
        if pygame.sprite.spritecollide(self.sprite,spriteGroup.sparkshield,False):
            self.dead = True
        if pygame.sprite.spritecollide(self.sprite,spriteGroup.fist,False):
            self.dead = True
        self.frame += 1
        # add collision rect into the sprite group
        self.sprite.rect.x = self.x + 3
        self.sprite.rect.y = self.y + 3
        spriteGroup.enemies.add(self.sprite)
        
        
        
        
    
        
