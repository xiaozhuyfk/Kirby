import pygame, os, sys, kirby, loadStartScene, handCursor
import spriteGroup, landscape, enemies
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((600,400),0,32)
pygame.display.set_caption("Kirby")
screen = pygame.display.get_surface()
kirby = kirby.kirby()
loadStartScene = loadStartScene.loadStartScene()
hand = handCursor.Hand()
clock = pygame.time.Clock()
spriteGroup = spriteGroup.spriteGroup()
landscape = landscape.landscape()
startGame = False
pause = False
shotzoList = []
pikeyList = []
bulletList = []

def addEnemy():
    if kirby.frame_w % 173 == 0:
        pikey = enemies.pikey(600,336)
        pikeyList.append(pikey)
    if kirby.frame_w %253 == 0:
        shotzo = enemies.shotzo(600,336)
        shotzoList.append(shotzo)
    for p in pikeyList:
        p.movement(screen,spriteGroup,hand,mouseEvent)
        if p.x < -26:
            pikeyList.remove(p)
            spriteGroup.enemies.remove(p.sprite)
        if p.dead:
            pikeyList.remove(p)
            spriteGroup.enemies.remove(p.sprite)
    for s in shotzoList:
        s.movement(screen,spriteGroup,kirby)
        if s.frame % 67 == 15:
            bullet = enemies.bullet(s.x,s.y,s.dir)
            bulletList.append(bullet)
        if s.x < -26:
            shotzoList.remove(s)
            spriteGroup.enemies.remove(s.sprite1)
    for b in bulletList:
        b.shoot(screen,spriteGroup)
        if b.dead:
            bulletList.remove(b)
        elif b.x < -26 or b.x > 626:
            spriteGroup.enemies.remove(b.sprite)
        

while 1:
    event = pygame.event.poll()
    key = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    mouseEvent = pygame.mouse.get_pressed()
    pygame.mouse.set_visible(False)
    if event.type == QUIT:
        sys.exit()
    if key[pygame.K_ESCAPE]:
        sys.exit()
    elif key[pygame.K_p]:
        pause = True
    if pause and key[pygame.K_c]:
        pause = False
    if pause == False:
        screen.fill((255,255,255))
        landscape.create(screen,spriteGroup)
        addEnemy()
        kirby.update2(event,screen,key,spriteGroup)
        hand.drawCircle(mouse_pos,mouseEvent,screen,kirby,spriteGroup)
        #spriteGroup.circlePixel.draw(screen)
        hand.cursor(mouse_pos,mouseEvent,screen,kirby,spriteGroup)
        clock.tick(20)
        pygame.display.update()
