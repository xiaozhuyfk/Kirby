# Kai
# This module is for loading sources
# Usage:
# load_image('name',scale)
# load_images('name1','name2'....)    return a list of images
# load_sound('name')
# load_scene('name')
# load_music('name')
# load_font('name',size)
# load_images('name1','name2',...)

import os,pygame
from pygame.locals import *

def load_image(fileName,scale=1):
    file = os.path.join('..','data','images',fileName)
    try:
        image = pygame.image.load(file)
    except pygame.error:
        pygame.quit()
        raise SystemExit, "Failed to import image %s" %fileName
    #image = pygame.transform.scale(image.convert_alpha(),(int(scale*image.get_width()),int(scale*
                                         # image.get_height())))
    return image

def load_images(*files):
    l = []
    for i in xrange(files):
        l.append(load_image(files[i]))
    return l

def load_sound(fileName):
    file = os.path.join('..','data','sounds',fileName)
    try:
        sound = pygame.mixer.Sound(file)
    except pygame.error:
        pygame.quit()
        raise SystemExit, "Failed to load sound %s" %fileName
    return sound

def load_scene(fileName):
    file = os.path.join('..','data','scenery',fileName)
    try:
        scenery = pygame.image.load(file)
    except pygame.error:
        pygame.quit()
        raise SystemExit, "Failed to load scenery %s" %fileName
    return scenery

def load_music(fileName):
    file = os.path.join('..','data','music',fileName)
    try:
        music = pygame.mixer.Sound(file)
    except pygame.error:
        pygame.quit()
        raise SystemExit, "Failed to load music %s" %fileName
    return music

def load_font(fileName,size):
    file = os.path.join('..','data','fonts',fileName)
    try:
        font = pygame.font.Font(file,size)
    except pygame.error:
        pygame.quit()
        raise SystemExit, "Failed to load font %s" %fileName
    return font
    