from fontColor import *
import spotify
import button
import random

# main loop
class MainLoop():
    def __init__(this,father,display,event):
        this.parent = father
        this.display = display
        this.event = event
        this.link = None
        this.songLoaded = False
        this.songNames = []

        # initializes a list which randomly determines the placement of the correct answer
        this.correct = [False,False,False,False]
        i = random.randint(0,3)
        this.correct[i] = True

        # intializes a list which will contain the text for each box
        this.cName = [None,None,None,None]


        this.score = 0

        this.index = 0

        # initializes each of the four buttons based on determined parameters
        this.buttons = [None,None,None,None]
        this.buttons[0] = button.Button(this,this.display,this.event,(650,180,250,100),this.correct[0],this.cName[0])
        this.buttons[1] = button.Button(this,this.display,this.event,(950,180,250,100),this.correct[1],this.cName[1])
        this.buttons[2] = button.Button(this,this.display,this.event,(650,380,250,100),this.correct[2],this.cName[2])
        this.buttons[3] = button.Button(this,this.display,this.event,(950,380,250,100),this.correct[3],this.cName[3])

        # initializes the img associated with the song
        this.img = pygame.transform.scale(pygame.image.load("int.jpg"),(500,500))

        

    def update(this):
        this.displayUpdate()


        # plays the song when it is done downloading
        if this.songLoaded == False:
            this.parent.spotify.play_file()
            this.songLoaded = True
        
        # displays the album cover
        this.display.blit(this.img,(100,100))

        # updates the buttons
        for i in range(0,4):
            this.buttons[i].update()
        
        # updates the image for the next question
        this.img = pygame.transform.scale(pygame.image.load("int.jpg"),(500,500))

        instr = ssubtitleFont.render("Listen to the song snippet and click on its name.",True,DARKRBG)
        this.display.blit(instr, (200,35))



    # called at the end of each question, indicating to move on to the next song or go to the end screen
    def nextInd(this):
        this.correct = [False,False,False,False]
        i = random.randint(0,3)
        this.correct[i] = True
        this.index += 1
        if this.index >= 10:
            this.complete_reset()
            this.parent.screenState = 3
            return
        this.choices()
        this.newFiles()

    # sets the text for its corresponding box
    # also helps set up for the next question
    def choices(this):
        for i in range(0,len(this.correct)):
            if this.correct[i]:
                this.cName[i] = this.songNames[this.index]
            else:
                this.cName[i] = this.parent.spotify.randName()
        for i in range(0,4):
            this.buttons[i].reconfig(this.cName[i],this.correct[i])
            print(this.cName[i])

                
    # resets the game at the end, preparing for the next loop
    def complete_reset(this):
        this.right = 0
        this.songLoaded = False
        this.parent.playlistData = None
        this.index = 0
        this.parent.indices = []
        this.parent.spotify.indices = []
        this.songNames = []
        this.parent.playlistMenu.playID = None


    # a separate initialization which prepares the game
    def initFile(this):    
        this.parent.indices = this.parent.spotify.get_indices(this.parent.spotify.playlist)
        while this.parent.indices == None:
            this.parent.indices = this.parent.spotify.get_indices(this.parent.spotify.playlist)
        print(this.parent.indices)
        for i in this.parent.indices:
            this.songNames.append(this.parent.spotify.get_songName(i))
        print(this.songNames)
        this.choices()
        this.newFiles()

    # downloads the files necessary for each question
    def newFiles(this):
        if this.index < 10:
            this.parent.spotify.get_file(this.parent.spotify.get_songURL(this.parent.indices[this.index]))
            this.parent.spotify.play_file()

            this.parent.spotify.get_img(this.parent.spotify.get_imgURL(this.parent.indices[this.index]))


    def displayUpdate(this):
        this.display.fill(SGBG)
