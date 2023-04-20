Written by CDT Daniel Song.

Overview of Files:
README.txt - a file which should be read before running the program
game.py - is the ***main*** file which the game is run. Initializes each screen to allow for easy transitioning between screen states.
startMenu.py - contains the class for the initial start screen
playlistMenu.py - contains the class for the Spotify playlist selection screen.
mainLoop.py - contains the screen which the user interacts with in order to play the game
button.py - contains a class for the multiple choice buttons in the mainLoop class, allowing for the user to interact with the game more effectively
endScreen.py - contains the class for the game over screen which loops back to the start screen
spotify.py - contains all the functions pertainig to interacting with the Spotify API
events.py - an event handler which allows for easier interaction between the program and user
copyPaste.py - a file containing two functions which use the win32clipboard module which assists with copy and paste functions
fontColor.py - a file containing most of the fonts and colors used in this program
int.jpg - a constantly changing file which contains the currently used image pertaining to the particular question
int.mp3 - a constantly changing file which contains the currently playing music clip pertaining to the particular question


Project Overview:
This project is a quiz game based on the Spotify Web API. I often use Spotify to listen to music, so I was wondering what I am capable with when controlling Spotify thorugh Python.
This project asks for a Spotify Playlist and returns a 10 question multiple choice quiz, asking the user to identify the song.
It was difficult to constantly work around the limitations in the download and playing capabilities of the Spotify Web API, as well as troubleshooting the interactions between the game screens.


How to run:
Open the game.py file and run it to play the Spotify quiz game.


Required Packages:
Download pygame using the following command:
python3 -m pip install -U pygame --user

Download win32clipboard using the following command:
pip install pywin32


Required Input:
On the second screen, the playlist selection screen, a Spotify playlist link must be provided. It is sufficient to right click on a playlist > Share > Copy Spotify URI
or click the three horizontal dots on the playlist page > Share > Copy Spotify URI
The link can be pasted by right clicking anywhere on the screen.
The Spotify playlist must be public.


Created Files:
The int.jpg and int.mp3 files are already included in the zip file, so no further files will be created. These two files will be continuously overwritten for each subsequent question.


Citations:
https://coderslegacy.com/python/python-pygame-tutorial/
Provides a basic tutorial of the pygame module, of which I began to understand the implementation of displays, basic shapes, and text in my code.

https://www.pygame.org/docs/
Contains extensive documentation for the pygame module, which I used for my shape creation, shape interaction, text displays,
music controls, and the entire display.

https://stackoverflow.com/questions/101128/how-do-i-read-text-from-the-clipboard
https://stackoverflow.com/questions/579687/how-do-i-copy-a-string-to-the-clipboard/4203897#4203897
These two links provided similar information on methods to copy and paste items from the Windows Clipboard using the win32clipboard module.
This helped me with pasting the copied Spotify link as well as copying provided Spotify links.

https://stmorse.github.io/journal/spotify-api.html
This journal helped me understand and guided me through a basic Spotify Web API exploration, of which I implemented a few key ideas
such as data gathering from a large amount of data in a json format.

https://developer.spotify.com/documentation/web-api/reference/#/
This website contains the specific documentation for the Spotify Web API, which I used to find specific commands to find links to downloading the images and song snippets.
