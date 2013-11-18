from pygame.locals import *
import pygame

class spriteGroup(object):
    def __init__(self):
        self.player = pygame.sprite.Group()
        self.handCursor = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.landscape = pygame.sprite.Group()
        self.dragable = pygame.sprite.Group()
        self.spark = pygame.sprite.Group()
        self.circlePixel = pygame.sprite.Group()
