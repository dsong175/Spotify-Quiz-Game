# https://stmorse.github.io/journal/spotify-api.html was the main source for helping me understand the Spotify API commands

import requests
import random
import pygame
from copyPaste import paste

class Spotify():
    def __init__(this):
        this.CLIENT_ID = ''
        this.CLIENT_SECRET = ''

        this.AUTH_URL = 'https://accounts.spotify.com/api/token'

        # POST
        this.auth_response = requests.post(this.AUTH_URL, {
            'grant_type': 'client_credentials',
            'client_id': this.CLIENT_ID,
            'client_secret': this.CLIENT_SECRET,
        })

        # convert the response to JSON
        this.auth_response_data = this.auth_response.json()

        # save the access token
        this.access_token = this.auth_response_data['access_token']

        this.headers = {
            'Authorization': 'Bearer {token}'.format(token=this.access_token),
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        # base URL of all Spotify API endpoints
        this.BASE_URL = 'https://api.spotify.com/v1/'

        this.indices = []
        this.playlist = ""
        this.link = ""
        this.playlistData = None
        this.song = None



    def get_playlist_data(this,playlist_id):
        # actual GET request with proper header
        r = requests.get(this.BASE_URL + 'playlists/' + playlist_id + "?market=US", headers=this.headers)

        this.playlistData = r.json()

        return(this.playlistData)


    # Get Playlist
    def get_playlist(this):
        playlist = paste()
        print(playlist)
        if("https://open.spotify.com/playlist" in playlist):
            this.playlist = playlist[34:56]
            return(this.playlist)
        else:
            return(False)

    # gets song link from playlist ID
    def get_songURL(this,index):
        this.link = this.playlistData["tracks"]["items"][int(index)]["track"]["preview_url"]
        return(this.link)
    
    # gets song name
    def get_songName(this,index):
        print(index)
        return(this.playlistData["tracks"]["items"][int(index)]["track"]["name"])

    # gets the usable indices
    def get_indices(this,playlist,length=10):
        count = 0
        max = len(this.playlistData["tracks"]["items"])

        if length > max:
            return(None)
        while len(this.indices) < length:
            i = random.randint(0,max-1)
            print(max,i)
            if i not in this.indices:
                if this.get_songURL(i) != None:
                    this.indices.append(int(i))
            count += 1
            if count == max:
                break
        if len(this.indices) < length:
            return(None)
        else:
            return(this.indices)


    # gets song link from playlist ID
    def get_imgURL(this,index):
        this.link = this.playlistData["tracks"]["items"][int(index)]["track"]["album"]["images"][0]["url"]
        return(this.link)


    # downloads file from link
    def get_img(this,link):
        img = requests.get(link)
        with open("int.jpg",'wb') as jpg:
            jpg.write(img.content)


    # downloads file from link
    def get_file(this,link):
        file = requests.get(link)
        with open("int.mp3",'wb') as song:
            song.write(file.content)

    
    # plays song file from directory
    def play_file(this):
        pygame.mixer.init()
        pygame.mixer.music.load("int.mp3")
        pygame.event.wait()
        pygame.mixer.music.play()
        pygame.event.wait()

    # get random song name from file
    def randName(this):
        i = random.randint(0,len(this.playlistData["tracks"]["items"])-1)
        return(this.get_songName(i))