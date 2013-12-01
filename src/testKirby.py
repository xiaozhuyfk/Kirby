# 15-112 Term Project
# Hongyu Li + hongyul + Section J

# main.py

import pygame, os, sys, kirby, loadStartScene, handCursor
import spriteGroup, landscape, enemies, menu, load, subscreen
from pygame.locals import *

#Pygame Init
pygame.init()
pygame.mixer.init()
window = pygame.display.set_mode((600,400),0,32)
pygame.display.set_caption("Kirby")
screen = pygame.display.get_surface()

# Create instances
kirby = kirby.kirby()
loadStartScene = loadStartScene.loadStartScene()
hand = handCursor.Hand()
clock = pygame.time.Clock()
spriteGroup = spriteGroup.spriteGroup()
landscape = landscape.landscape()
menu = menu.menu()
subscreen = subscreen.subscreen()

# Use Struct to store globals
class Struct: pass
data = Struct()
data.menuMusic = load.load_sound("menu.wav")
data.gameMusic = load.load_sound("game.wav")
data.startGame = False
data.pause = False
data.shotzoList = [] # store enemy instances
data.pikeyList = []
data.bulletList = []
data.waddleDeeList = []
data.waddleDooList = []
data.start = False
data.restart = False
data.play1 = False # variables for playing different music
data.play2 = False

# Add Pikey
def addPikey():
    if kirby.frame_w % 173 == 50:
        pikey = enemies.pikey(600,336)
        data.pikeyList.append(pikey)
    for p in data.pikeyList:
        p.movement(screen,spriteGroup,hand,mouseEvent)
        if p.x < -26:
            data.pikeyList.remove(p)
            spriteGroup.enemies.remove(p.sprite)
        if p.dead:
            data.pikeyList.remove(p)
            spriteGroup.enemies.remove(p.sprite)
# Add Shotzo
def addShotzo():
    if kirby.frame_w % 253 == 0:
        shotzo = enemies.shotzo(600,336)
        data.shotzoList.append(shotzo)
    for s in data.shotzoList:
        s.movement(screen,spriteGroup,kirby)
        if s.frame % 67 == 15:
            bullet = enemies.bullet(s.x,s.y,s.dir)
            data.bulletList.append(bullet)
        if s.x < -26:
            data.shotzoList.remove(s)
            spriteGroup.enemies.remove(s.sprite1)
    for b in data.bulletList:
        b.shoot(screen,spriteGroup)
        if b.dead:
            data.bulletList.remove(b)
            spriteGroup.enemies.remove(b.sprite)
        elif b.x < -26 or b.x > 626:
            spriteGroup.enemies.remove(b.sprite)

# Add WaddleDee
def addWaddleDee():
    if kirby.frame_w % 211 == 20:
        waddleDee = enemies.waddleDee(600,336)
        data.waddleDeeList.append(waddleDee)
    for dee in data.waddleDeeList:
        dee.movement(screen,spriteGroup,hand,mouseEvent)
        if dee.x < -26:
            data.waddleDeeList.remove(dee)
            spriteGroup.enemies.remove(dee.sprite)
        if dee.dead:
            data.waddleDeeList.remove(dee)
            spriteGroup.enemies.remove(dee.sprite)

# Add WaddleDoo
def addWaddleDoo():
    if kirby.frame_w % 197 == 66:
        waddleDoo = enemies.waddleDoo(600,336)
        data.waddleDooList.append(waddleDoo)
    for doo in data.waddleDooList:
        doo.movement(screen,spriteGroup,hand,mouseEvent)
        if doo.x < -26:
            data.waddleDooList.remove(doo)
            spriteGroup.enemies.remove(doo.sprite)
        if doo.dead:
            data.waddleDooList.remove(doo)
            spriteGroup.enemies.remove(doo.sprite)

# Add enemies
def addEnemy():
    addPikey()
    addShotzo()
    addWaddleDee()
    addWaddleDoo()

# Init function to restart the game
def init():
    data.startGame = False
    data.pause = False
    data.shotzoList = []
    data.pikeyList = []
    data.bulletList = []
    data.waddleDeeList = []
    data.waddleDooList = []
    data.start = False
    data.restart = False
    data.play1 = False
    data.play2 = False
    spriteGroup.enemies.empty()
    spriteGroup.sparkshield.empty()
    kirby.init()
    
while 1:
    event = pygame.event.poll()
    key = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    mouseEvent = pygame.mouse.get_pressed()
    pygame.mouse.set_visible(False) # hide the cursor
    if event.type == QUIT:
        sys.exit()
    #Stores menu's and subscreen's properties into data
    data.start = menu.start
    data.pause = subscreen.pause
    data.restart = subscreen.restart
    if data.restart:
        init()
        subscreen.init()
    if data.start: # Start the game
        if data.play2 == False:
            data.gameMusic.play(-1)
            data.play2 = True
        data.menuMusic.stop()
        if data.pause == False and kirby.life > 0:
            screen.fill((255,255,255))
            landscape.create(screen,spriteGroup) # load the background
            addEnemy()
            kirby.update(event,screen,key,spriteGroup) # Kirby's movement
            # mouse cursor
            hand.cursor(mouse_pos,mouseEvent,screen,kirby,spriteGroup)
        subscreen.run(screen,event,key,kirby,menu) # load subscreen
        clock.tick(20)
        pygame.display.update()
    else: # if the game is not started, show the menu
        data.gameMusic.stop()
        if data.play1 == False:
            data.menuMusic.play(-1)
            data.play1 = True
        menu.run(screen,event,key) # run menu
        pygame.display.update()
        
