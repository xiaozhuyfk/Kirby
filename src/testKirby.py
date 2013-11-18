import pygame, os, sys, kirby, loadStartScene, handCursor
import spriteGroup, landscape
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

while True:
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
        kirby.update2(event,screen,key,spriteGroup)
        hand.cursor(mouse_pos,mouseEvent,screen,kirby,spriteGroup)
        clock.tick(20)
        pygame.display.update()
