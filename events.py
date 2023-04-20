import pygame
import sys
from pygame.locals import *

# event handler which records mouse position and the status of the clicks

class Events():
    def  __init__(this):
        this.click = []
        this.mouseHeld = False
        this.click = pygame.mouse.get_pressed()

    def Update(this):
        for event in pygame.event.get(): # Checks each event
            if (event.type == QUIT): # Application closed
                sys.exit(0)

        if this.click[0] == True:
            this.mouseHeld = True
        else:
            this.mouseHeld = False
        
        this.click = pygame.mouse.get_pressed()


    def GetMouse(this):
        mouse_position = pygame.mouse.get_pos()
        return(mouse_position)

    def GetMouseDown(this):
        return(this.click)

