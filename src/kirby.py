import pygame, load, random, spriteGroup, block, time
from pygame.locals import *

#block = block.Block(16,16)

class kirby(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.kirby1 = load.load_image("Kirby1.png")
        self.kirbyMove1 = load.load_image("KirbyMove1.png")
        self.kirbyMove2 = load.load_image("KirbyMove2.png")
        self.kirbyMove3 = load.load_image("KirbyMove3.png")
        self.kirbyMove4 = load.load_image("KirbyMove4.png")
        self.kirbyMove5 = load.load_image("KirbyMove5.png")
        self.kirbyMove6 = load.load_image("KirbyMove6.png")
        self.kirbyMove7 = load.load_image("KirbyMove7.png")
        self.kirbyMove8 = load.load_image("KirbyMove8.png")
        self.kirbyMove9 = load.load_image("KirbyMove9.png")
        self.kirbyMove10 = load.load_image("KirbyMove10.png")
        self.kirby1i = load.load_image("Kirby1i.png")
        self.kirbyMove1i = load.load_image("KirbyMove1i.png")
        self.kirbyMove2i = load.load_image("KirbyMove2i.png")
        self.kirbyMove3i = load.load_image("KirbyMove3i.png")
        self.kirbyMove4i = load.load_image("KirbyMove4i.png")
        self.kirbyMove5i = load.load_image("KirbyMove5i.png")
        self.kirbyMove6i = load.load_image("KirbyMove6i.png")
        self.kirbyMove7i = load.load_image("KirbyMove7i.png")
        self.kirbyMove8i = load.load_image("KirbyMove8i.png")
        self.kirbyMove9i = load.load_image("KirbyMove9i.png")
        self.kirbyMove10i = load.load_image("KirbyMove10i.png")
        self.kirbyMove = [self.kirby1, self.kirbyMove1,
        self.kirbyMove2, self.kirbyMove3, self.kirbyMove4, 
        self.kirbyMove5, self.kirbyMove6, self.kirbyMove7, 
        self.kirbyMove8, self.kirbyMove9, self.kirbyMove10]
        self.kirbyMovei = [self.kirby1i, self.kirbyMove1i,
        self.kirbyMove2i, self.kirbyMove3i, self.kirbyMove4i, 
        self.kirbyMove5i, self.kirbyMove6i, self.kirbyMove7i, 
        self.kirbyMove8i, self.kirbyMove9i, self.kirbyMove10i]

        self.kirbyFly1 = load.load_image("kirbyFly1.png")
        self.kirbyFly2 = load.load_image("kirbyFly2.png")
        self.kirbyFly3 = load.load_image("kirbyFly3.png")
        self.kirbyFly4 = load.load_image("kirbyFly4.png")
        self.kirbyFly5 = load.load_image("kirbyFly5.png")
        self.kirbyFly6 = load.load_image("kirbyFly6.png")
        self.kirbyFly7 = load.load_image("kirbyFly7.png")
        self.kirbyFly8 = load.load_image("kirbyFly8.png")
        self.kirbyFly = [self.kirbyFly1, self.kirbyFly2,
        self.kirbyFly3, self.kirbyFly4, self.kirbyFly5,
        self.kirbyFly6, self.kirbyFly7, self.kirbyFly8]

        self.kirbyFly1i = load.load_image("kirbyFly1i.png")
        self.kirbyFly2i = load.load_image("kirbyFly2i.png")
        self.kirbyFly3i = load.load_image("kirbyFly3i.png")
        self.kirbyFly4i = load.load_image("kirbyFly4i.png")
        self.kirbyFly5i = load.load_image("kirbyFly5i.png")
        self.kirbyFly6i = load.load_image("kirbyFly6i.png")
        self.kirbyFly7i = load.load_image("kirbyFly7i.png")
        self.kirbyFly8i = load.load_image("kirbyFly8i.png")
        self.kirbyFlyi = [self.kirbyFly1i, self.kirbyFly2i,
        self.kirbyFly3i, self.kirbyFly4i, self.kirbyFly5i,
        self.kirbyFly6i, self.kirbyFly7i, self.kirbyFly8i]

        self.kirbyJump1 = load.load_image("kirbyJump1.png")
        self.kirbyJump2 = load.load_image("kirbyJump2.png")
        self.kirbyJump3 = load.load_image("kirbyJump3.png")
        self.kirbyJump4 = load.load_image("kirbyJump4.png")
        self.kirbyJump5 = load.load_image("kirbyJump5.png")
        self.kirbyJump6 = load.load_image("kirbyJump6.png")
        self.kirbyJump7 = load.load_image("kirbyJump7.png")
        self.kirbyJump8 = load.load_image("kirbyJump8.png")
        self.kirbyJump9 = load.load_image("kirbyJump9.png")
        self.kirbyJump = [self.kirbyJump1,
        self.kirbyJump3, self.kirbyJump4, self.kirbyJump5,
        self.kirbyJump6, self.kirbyJump7, self.kirbyJump8,
        self.kirbyJump9]

        self.kirbyJump1i = load.load_image("kirbyJump1i.png")
        self.kirbyJump2i = load.load_image("kirbyJump2i.png")
        self.kirbyJump3i = load.load_image("kirbyJump3i.png")
        self.kirbyJump4i = load.load_image("kirbyJump4i.png")
        self.kirbyJump5i = load.load_image("kirbyJump5i.png")
        self.kirbyJump6i = load.load_image("kirbyJump6i.png")
        self.kirbyJump7i = load.load_image("kirbyJump7i.png")
        self.kirbyJump8i = load.load_image("kirbyJump8i.png")
        self.kirbyJump9i = load.load_image("kirbyJump9i.png")
        self.kirbyJumpi = [self.kirbyJump1i,
        self.kirbyJump3i, self.kirbyJump4i, self.kirbyJump5i,
        self.kirbyJump6i, self.kirbyJump7i, self.kirbyJump8i,
        self.kirbyJump9i]

        self.kirbyBlow1 = load.load_image("kirbyBlow1.png")
        self.kirbyBlow2 = load.load_image("kirbyBlow2.png")
        self.kirbyBlow = [self.kirbyBlow1, self.kirbyBlow2]

        self.kirbyBlow1i = load.load_image("kirbyBlow1i.png")
        self.kirbyBlow2i = load.load_image("kirbyBlow2i.png")
        self.kirbyBlowi = [self.kirbyBlow1i, self.kirbyBlow2i]

        self.kirbyAir1 = load.load_image("kirbyAir1.png")
        self.kirbyAir2 = load.load_image("kirbyAir2.png")
        self.kirbyAir3 = load.load_image("kirbyAir3.png")
        self.kirbyAir3i = load.load_image("kirbyAir3i.png")
        self.kirbyAir = [self.kirbyAir1, self.kirbyAir2, self.kirbyAir3]
        self.kirbyAiri = [self.kirbyAir1,self.kirbyAir2, self.kirbyAir3i]

        self.x = 300
        self.y = 336
        self.speed_x = 0
        self.speed_x2 = 0
        self.speed_y = 0
        self.speed_y2 = 0
        self.frame_w = 0
        self.frame_f = 0
        self.frame_turn = 0
        self.frame_blow = -1
        self.left = False
        self.gravity = 0.8
        self.gravity2 = 0.1
        self.airstate = False
        self.flystate = False
        self.blowstate = False
        self.doubleJump = False
        self.djTime = 0
        self.life = 10
        self.dead = False

        self.spark1 = load.load_image("spark1.png")
        self.spark2 = load.load_image("spark2.png")
        self.spark3 = load.load_image("spark3.png")
        self.sparkle1 = load.load_image("sparkle1.png")
        self.sparkle2 = load.load_image("sparkle2.png")
        self.sparkle3 = load.load_image("sparkle3.png")
        self.spark = [self.spark1,self.spark2,self.spark3]
        self.frame_spark = 0
        self.fire = False

        self.kirbyInvincible1 = load.load_image("kirbyInvincible1.png")
        self.kirbyInvincible2 = load.load_image("kirbyInvincible2.png")
        self.frame_inv = 0
        self.invincible = False
        self.sprite = block.Block(16,16)
        self.sprite_spark = block.Block(60,60)

    def init(self):
        self.x = 300
        self.y = 336
        self.speed_x = 0
        self.speed_x2 = 0
        self.speed_y = 0
        self.speed_y2 = 0
        self.frame_w = 0
        self.frame_f = 0
        self.frame_turn = 0
        self.frame_blow = -1
        self.left = False
        self.gravity = 0.8
        self.gravity2 = 0.1
        self.airstate = False
        self.flystate = False
        self.blowstate = False
        self.doubleJump = False
        self.djTime = 0
        self.life = 10
        self.frame_spark = 0
        self.fire = False
        self.frame_inv = 0
        self.invincible = False
        self.dead = False
        

    def update(self,event,screen,key,spriteGroup):
        self.kirbyControl_a_right(screen,key,event)
        self.kirbyControl_a_left(screen,key,event)
        self.kirbyControl_redux(screen,key,event)
        self.checkState_a(screen,key,event)

        block.rect.x = self.x
        block.rect.y = self.y

        spriteGroup.player.add(block)

    def kirbyControl_a_right(self,screen,key,event):
        if self.left == False:
            #kirby moves
            if key[pygame.K_RIGHT] and self.airstate == False:
                screen.blit(self.kirbyMove[self.frame_w%11], (self.x, self.y))
            elif self.flystate and key[pygame.K_x] and not self.blowstate:
                self.flystate = False
                self.blowstate = True
                self.speed_y = 0
                screen.blit(self.kirbyBlow1, (self.x, self.y))
            elif self.flystate == False and self.blowstate:
                screen.blit(self.kirbyBlow2, (self.x, self.y))
                screen.blit(self.kirbyAir[self.frame_blow%3],
                (self.x+20+self.frame_blow*5,self.y+13-self.frame_blow*2))
                if self.frame_blow > 2:
                    self.frame_blow = -1
                    self.blowstate = False
            elif self.airstate == True and self.flystate == False and self.speed_y>0:
                screen.blit(self.kirbyJump1, (self.x, self.y))
            elif self.airstate == True and self.flystate == False and self.speed_y<=0:
                screen.blit(self.kirbyJump7, (self.x, self.y))
            #kirby fly
            elif self.airstate == True and self.flystate == True and key[pygame.K_z]:
                screen.blit(self.kirbyFly[self.frame_f%8], (self.x, self.y))
            #kirby steady fly mode
            elif self.airstate == True and self.flystate == True:
                screen.blit(self.kirbyFly1, (self.x, self.y))
            else:
                screen.blit(self.kirbyMove[0], (self.x, self.y))

    def kirbyControl_a_left(self,screen,key,event):
        if self.left == True:
            if key[pygame.K_LEFT] and self.airstate == False: 
                screen.blit(self.kirbyMovei[self.frame_w%11], (self.x, self.y))
            elif self.flystate == True and key[pygame.K_x] and not self.blowstate:
                self.flystate = False
                self.blowstate = True
                self.speed_y = 0
                screen.blit(self.kirbyBlow1i, (self.x, self.y))
            elif self.flystate == False and self.blowstate:
                screen.blit(self.kirbyBlow2i, (self.x, self.y))
                screen.blit(self.kirbyAiri[self.frame_blow%3],(self.x-13-self.frame_blow*5,self.y+13-self.frame_blow*2))
                if self.frame_blow > 2:
                    self.frame_blow = -1
                    self.blowstate = False
            elif self.airstate == True and self.flystate == False and self.speed_y>0:
                screen.blit(self.kirbyJump1i, (self.x, self.y))
            elif self.airstate == True and self.flystate == False and self.speed_y<=0:
                screen.blit(self.kirbyJump7i, (self.x, self.y))
            elif self.airstate == True and self.flystate == True and key[pygame.K_z]:
                screen.blit(self.kirbyFlyi[self.frame_f%8], (self.x, self.y))
            elif self.airstate == True and self.flystate == True:
                screen.blit(self.kirbyFly1i, (self.x, self.y))
            else:
                screen.blit(self.kirbyMovei[0], (self.x, self.y))

    def kirbyControl_redux(self,screen,key,event):
        if key[pygame.K_LEFT] and not key[pygame.K_RIGHT]:
            self.left = True
            self.speed_x = -3
            self.frame_turn += -1
        elif key[pygame.K_RIGHT] and not key[pygame.K_LEFT]:
            self.left = False
            self.speed_x = 3
            self.frame_turn += 1
        elif key[pygame.K_LEFT] and key[pygame.K_RIGHT] and self.frame_turn < 0:
            self.left = False
            self.speed_x = 3
            self.frame_turn = 0
        elif key[pygame.K_RIGHT] and key[pygame.K_RIGHT] and self.frame_turn > 0:
            self.left = True
            self.speed_x = -3
            self.frame_turn = 0
        if key[pygame.K_z] and self.flystate:
            self.speed_y2 = 2.5

        if key[pygame.K_z] and (self.airstate == False):
            self.speed_y = 8
            self.airstate = True
        elif self.airstate and key[pygame.K_z]:
            self.flystate = True
            self.speed_y2 = 2
            self.gravity2 = 0.1
        if key[pygame.K_x] and self.flystate:
            self.speed_y = 0
            self.flystate = False
        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                self.speed_x = 0
                

    def checkState_a(self,screen,key,event):
        self.x += self.speed_x

        if self.blowstate:
            self.frame_blow += 1

        if self.airstate == True:
            if self.flystate == False:
                self.y -= self.speed_y
                self.speed_y -= self.gravity
            elif self.flystate == True:
                self.y -= self.speed_y2
                if self.speed_y2 <= -2:
                    self.gravity2 = 0
                self.speed_y2 -= self.gravity2

        if self.y > 336:
            self.airstate = False
            self.flystate = False
            self.speed_y = 0
            self.speed_y2 = 0
            self.y = 336
        
        if key[pygame.K_RIGHT] or key[pygame.K_LEFT]:
            self.frame_w += 1
        if key[pygame.K_z] and self.flystate == True:
            self.frame_f += 1
        
        

    def update2(self,event,screen,key,spriteGroup):
        self.kirbyControl_p(screen,key,spriteGroup)
        self.checkState_p(screen,key,spriteGroup)

        if pygame.sprite.spritecollide(self.sprite,spriteGroup.enemies,False)\
                and self.invincible == False:
            self.invincible = True
            self.life -= 1
        if self.invincible:
            self.frame_inv += 1
        if self.frame_inv > 30:
            self.invincible = False
            self.frame_inv = 0
        #spriteGroup.player.draw(screen)
        #spriteGroup.sparkshield.draw(screen)
            
        
    def fireSpark(self,screen,spriteGroup):
        self.sprite_spark.rect.x = self.x-17
        self.sprite_spark.rect.y = self.y-17
        spriteGroup.sparkshield.add(self.sprite_spark)
        screen.blit(self.spark[self.frame_spark%3],(self.x-21,self.y-21))
        self.frame_spark += 1

    def kirbyControl_p(self,screen,key,spriteGroup):
        if key[pygame.K_SPACE]:
            self.fire = True
        if self.fire:
            self.fireSpark(screen,spriteGroup)
        if self.frame_spark > 150:
            self.fire = False
            self.frame_spark = 0
            spriteGroup.sparkshield.empty()
        if self.invincible == False:    
            if self.airstate == False:
                screen.blit(self.kirbyMove[self.frame_w%11],(self.x,self.y))
            elif self.airstate == True and self.speed_y>0:
                screen.blit(self.kirbyJump1, (self.x, self.y))
            elif self.airstate == True and self.speed_y<=0:
                screen.blit(self.kirbyJump7, (self.x, self.y))
        else:
            if self.airstate == False:
                if self.frame_inv % 3 == 0:
                    screen.blit(self.kirbyMove[self.frame_w%11],(self.x,self.y))
            elif self.airstate == True and self.speed_y>0:
                if self.frame_inv % 3 == 0:
                    screen.blit(self.kirbyJump1, (self.x, self.y))
            elif self.airstate == True and self.speed_y<=0:
                if self.frame_inv % 3 == 0:
                    screen.blit(self.kirbyJump7, (self.x, self.y))

    def checkState_p(self,screen,key,spriteGroup):
        if key[pygame.K_z] and self.airstate == False:
            self.djTime = time.time()
            self.speed_y = 10
            self.airstate = True
        elif self.airstate and key[pygame.K_z] and self.doubleJump == False:
            if time.time()-self.djTime > 0.3:
                self.doubleJump = True
                self.speed_y = 8

        if self.airstate == True:
            self.y -= self.speed_y
            self.speed_y -= self.gravity
            
        self.sprite.rect.x = self.x+5
        self.sprite.rect.y = self.y+5
        
        if self.y > 336:
            self.airstate = False
            self.flystate = False
            self.doubleJump = False
            self.speed_y = 0
            self.speed_y2 = 0
            self.y = 336

        if self.y < 336:
            self.airstate = True

        self.frame_w += 1

        spriteGroup.player.add(self.sprite)
        
        

        

        
