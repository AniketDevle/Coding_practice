from bs4 import BeautifulSoup as BS
import requests

req = requests.get("https://www.azlyrics.com/lyrics/zaynmalik/dusktilldawn.html")
soup = BS(req.text , 'xml')

Lyr = soup.find_all('div' , { 'class': 'col-xs-12 col-lg-8 text-center'})[0]

so = Lyr.find_all('div' , {'class' : 'addthis_toolbox addthis_default_style'})[0]

lr = so.find_all('div' , {'class': None})[0]

print(lr)


"""
We can also use python PyLyrics API

1. Search for artist and List albums

    from PyLyrics import *

    albums = PyLyrics.getAlbums(singer='Eminem')
    for a in albums:
        print (a) #Each album printed is a Album Object


2. List all tracks of an Album

    
    from PyLyrics import *

    albums = PyLyrics.getAlbums(singer='Eminem')
    myalbum = albums[4] #Select your album based on Index

    *****This .tracks() function gives an error while working in terminal****
    
    tracks = myalbum.tracks() #or PyLyrics.getTracks(myalbum)
    for track in tracks:
        print (track) #Each track is a track object
        print (track.getLyrics()) #Get the lyrics

3.Get Lyrics of a song

    from PyLyrics import *

    print(PyLyrics.getLyrics('Taylor Swift','Blank Space')) #Print the lyrics directly

"""



