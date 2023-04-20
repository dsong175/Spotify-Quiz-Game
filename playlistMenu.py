from fontColor import *
import spotify
from copyPaste import copy


# playlist insert menu
class PlaylistMenu():
    def __init__(this,father,display,event,spotoify):
        this.playID = None
        this.parent = father
        this.display = display
        this.event = event
        this.spotify = spotoify
        this.error = textFont.render("",True,RED)

        this.text1 = WHITE
        this.text2 = WHITE
        this.text3 = WHITE
        this.box1 = LTUR
        this.box2 = DTUR
        this.box3 = RTUR


    def update(this):
        this.displayUpdate()

        # instances allowing the user to copy provided playlists
        pygame.draw.rect(this.display, this.box1, (60,350,140,70))
        b1Text = boxFont1.render("mint",True,this.text1)
        this.display.blit(b1Text, (90,370))
        cbox1 = pygame.Rect(60,350,150,70)

        pygame.draw.rect(this.display, this.box2, (250,350,150,70))
        b2Text = boxFont2.render("Top 100",True,this.text2)
        this.display.blit(b2Text, (275,375))
        cbox2 = pygame.Rect(250,350,150,70)

        pygame.draw.rect(this.display, this.box3, (440,350,160,70))
        b2Text = boxFont3.render("Top Rock",True,this.text2)
        this.display.blit(b2Text, (465,375))
        cbox3 = pygame.Rect(440,350,160,70)

        # If right click on screen, get the copied value and paste it on the screen
        if this.event.click[2] and this.event.mouseHeld == False:

            # call get playlist function
            this.playID = this.spotify.get_playlist()
        
            # Go on to the next screen if its a valid playlist,otherwise print error message
            if this.playID == False:
                this.error = textFont.render("Enter a valid playlist",True,RED)
            elif len(this.playID)==22:
                this.error = textFont.render(this.playID, True, BLUE)
                this.parent.screenState = 2
                this.parent.playlistData = this.spotify.get_playlist_data(this.playID)

                # begins initializing the game
                this.parent.mainLoop.initFile()

        # allows the user to copy given playlists
        elif this.event.click[0]:
            print(this.event.GetMouse())
            if cbox1.collidepoint(this.event.GetMouse()):
                this.error = textFont.render("Copied!",True,GREEN)
                copy("https://open.spotify.com/playlist/37i9dQZF1DX4dyzvuaRJ0n?si=c482d442afcc442a")
                
            elif cbox2.collidepoint(this.event.GetMouse()):
                this.error = textFont.render("Copied!",True,GREEN)
                copy("https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M?si=fdda68410cab4b29")
            
            elif cbox3.collidepoint(this.event.GetMouse()):
                this.error = textFont.render("Copied!",True,GREEN)
                copy("https://open.spotify.com/playlist/37i9dQZF1DXcF6B6QPhFDv?si=be68590398614242")

        this.display.blit(this.error, (60,250)) 



    def displayUpdate(this):     
        this.display.fill(BLACK)
        titleText = textFont.render("If you want to enter your own playlist, copy the playlist link and paste it by right clicking the screen",True,GREEN)
        provPlText = textFont.render("Or, click one of these playlists to copy it :) ", True, GREEN)
        plTxt = textFont.render("Enter playlist: ", True, BLUE)
        this.display.blit(plTxt, (60,200))
        this.display.blit(titleText, (60,60))
        this.display.blit(provPlText, (60, 300))
