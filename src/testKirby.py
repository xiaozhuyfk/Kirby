import pygame, os, sys, kirby, loadStartScene, handCursor
import spriteGroup, landscape, enemies, menu, load
from pygame.locals import *

pygame.mixer.pre_init(44100, 16, 2, 4096)
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
menu = menu.menu()
startGame = False
pause = False
shotzoList = []
pikeyList = []
bulletList = []
waddleDeeList = []
waddleDooList = []
start = False
menuMusic = load.load_music("menu.wav")
menuMusic.set_volume(4)

def addEnemy():
    if kirby.frame_w % 173 == 50:
        pikey = enemies.pikey(600,336)
        pikeyList.append(pikey)
    if kirby.frame_w % 253 == 0:
        shotzo = enemies.shotzo(600,336)
        shotzoList.append(shotzo)
    if kirby.frame_w % 211 == 20:
        waddleDee = enemies.waddleDee(600,336)
        waddleDeeList.append(waddleDee)
    if kirby.frame_w % 197 == 66:
        waddleDoo = enemies.waddleDoo(600,336)
        waddleDooList.append(waddleDoo)
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
            spriteGroup.enemies.remove(b.sprite)
        elif b.x < -26 or b.x > 626:
            spriteGroup.enemies.remove(b.sprite)
    for dee in waddleDeeList:
        dee.movement(screen,spriteGroup,hand,mouseEvent)
        if dee.x < -26:
            waddleDeeList.remove(dee)
            spriteGroup.enemies.remove(dee.sprite)
        if dee.dead:
            waddleDeeList.remove(dee)
            spriteGroup.enemies.remove(dee.sprite)
    for doo in waddleDooList:
        doo.movement(screen,spriteGroup,hand,mouseEvent)
        if doo.x < -26:
            waddleDooList.remove(doo)
            spriteGroup.enemies.remove(doo.sprite)
        if doo.dead:
            waddleDooList.remove(doo)
            spriteGroup.enemies.remove(doo.sprite)       
        

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
    if key[pygame.K_r]:
        shotzoList = []
        pikeyList = []
        bulletList = []
        waddleDeeList = []
        waddleDooList = []
        spriteGroup.enemies.empty()
        spriteGroup.sparkshield.empty()
        kirby.init()
    start = menu.start
    if start:
        menuMusic.stop()
        if pause == False and kirby.life > 0:
            screen.fill((255,255,255))
            landscape.create(screen,spriteGroup)
            #spriteGroup.enemies.draw(screen)
            addEnemy()
            kirby.update2(event,screen,key,spriteGroup)
            #hand.drawCircle(mouse_pos,mouseEvent,screen,kirby,spriteGroup)
            #spriteGroup.circlePixel.draw(screen)
            hand.cursor(mouse_pos,mouseEvent,screen,kirby,spriteGroup)
            clock.tick(20)
            pygame.display.update()
    else:
        menuMusic.play(-1)
        menu.run(screen,event,key)
        pygame.display.update()
        
