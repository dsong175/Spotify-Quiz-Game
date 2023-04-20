###
# Written by: CDT Daniel Song
###


import pygame
from pygame.locals import *
from events import Events
from spotify import Spotify
from fontColor import *
from playlistMenu import PlaylistMenu
from startMenu import StartMenu
from mainLoop import MainLoop
from endScreen import EndScreen


class Game():
    def __init__(this):
        this.screenState = 0
        this.event = Events()
        this.game = True
        this.spotify = Spotify()
        this.playlistData = None
        this.FPS = 24
        this.clock = pygame.time.Clock()
        this.display = pygame.display.set_mode((1280,720))

        # Initialize the screens
        this.startMenu = StartMenu(this,this.display,this.event)
        this.playlistMenu = PlaylistMenu(this,this.display,this.event,this.spotify)
        this.mainLoop = MainLoop(this,this.display,this.event)
        this.endScreen = EndScreen(this,this.display,this.event,this.mainLoop)

        this.indices = []
        

        pygame.init()
        # Setup Display
        this.display.fill(BLACK)
    
    # Game Loop
    def start(this):
        while this.game:
            this.event.Update()
            if this.screenState == 0:
                this.startMenu.update()
            elif this.screenState == 1:
                this.playlistMenu.update()
            elif this.screenState == 2:
                this.mainLoop.update()
            elif this.screenState == 3:
                this.endScreen.update()

            pygame.display.update()

            this.clock.tick(this.FPS)


game = Game()
game.start()


