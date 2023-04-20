from fontColor import *
import spotify

# main loop
class Button():
    def __init__(this,father,display,event,coords,correct,name):
        this.parent = father
        this.display = display
        this.event = event
        this.correct = correct
        this.color = BOXCOLOR
        this.coords = coords
        this.name = name


    
        # initializes the displayed box, text, and interactive box
        pygame.draw.rect(this.display, this.color, this.coords)
        this.text = smallFont.render(this.name,True,WHITE)
        this.box = pygame.Rect(coords[0],coords[1],coords[2],coords[3])


    def update(this):
        if this.event.click[0] and this.event.mouseHeld == False:
            if this.box.collidepoint(this.event.GetMouse()):

                # stops the music if a box is clicked
                pygame.mixer.quit()

                # adds a point to the score if the correct box is chosen
                if this.correct:
                    this.color = SPOTIFYGREEN
                    this.parent.score += 1
                    print(this.parent.score)
                else:
                    this.color = RED
                pygame.draw.rect(this.display,this.color,this.coords)
                
                # runs the functions required to switch to the next question
                this.parent.nextInd()
       
        # displays the box
        pygame.draw.rect(this.display,this.color,this.coords)

        # displays the text in the box
        this.display.blit(this.text, (this.coords[0]+10,this.coords[1]+20))


    # resets certain characteristics of the button for the next question
    def reconfig(this,name,correct):
        this.color = BOXCOLOR
        
        this.name = name
        # cuts the length of the name if too long
        if len(this.name) > 13:
            this.name = this.name[:10] + "..."

        this.correct = correct
        this.text = boxFont1.render(this.name,True,WHITE)
