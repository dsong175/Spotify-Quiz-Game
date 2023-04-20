from fontColor import *
import spotify

# start menu,  a simple click to start screen
class StartMenu():
    def __init__(this,father,display,event):
        this.parent = father
        this.display = display
        this.event = event

    def __str__(this):
        pass

    def update(this):
        this.displayUpdate()
        if this.event.click[0] and this.event.mouseHeld == False:
            this.parent.screenState = 1


    def displayUpdate(this):
        this.display.fill(SPOTIFYGREEN)
        titleText = titleFont.render("Welcome to Spotify!",True,WHITE)
        dirText = subtitleFont.render("Click anywhere to begin.",True,WHITE)
        this.display.blit(titleText, (60,100))
        this.display.blit(dirText, (190,350))