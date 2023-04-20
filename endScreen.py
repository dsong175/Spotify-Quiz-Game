from fontColor import *
import spotify

# end screen
class EndScreen():
    def __init__(this,father,display,event,mainLoop):
        this.parent = father
        this.display = display
        this.event = event
        this.mainLoop = mainLoop


    def update(this):
        this.displayUpdate()
        if this.event.click[0] and this.event.mouseHeld == False:
            this.parent.screenState = 0


    def displayUpdate(this):
        this.display.fill(SPOTIFYGREEN)
        titleText = ssubtitleFont.render("Congratulations, you got " + str(this.mainLoop.score) + " out of 10",True,WHITE)
        dirText = ssubtitleFont.render("Click anywhere to return to the menu.",True,WHITE)
        this.display.blit(titleText, (60,100))
        this.display.blit(dirText, (190,350))