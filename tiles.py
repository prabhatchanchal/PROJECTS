import pygame
import sys
from pygame.locals import *
import random
import time
colors=list(pygame.colordict.THECOLORS.values())

def homescreen(screen,setText,running,home):
    play=setText.render('Play',False,colors[35])
    # screen.blit(play,(200,150))
    resume=setText.render('Resume',False,colors[22])
    quit=setText.render('Quit',False,colors[2])
    x,y=200,120
    for objects in [play,resume,quit]:
        screen.blit(objects,(x,y))
        y+=30

    
