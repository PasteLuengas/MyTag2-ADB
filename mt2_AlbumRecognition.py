"""
Hey, if you're reading this...
I'm so sorry for the messy code, this code is from
the first version of MyTag, I was starting with Python... and
even I am confused with this code. I'm trying to clean up this code
and make it better; Also, the code has a lot of bugs that I'm solving.
I apologize
Nicolás Luengas
"""




#Import Libs
from urllib.request import urlopen
from xml.etree.ElementTree import parse
import SaveImage
import os
import eyed3
from eyed3.id3.frames import ImageFrame


#here is saved the audio files from the selected folder
thefiles = []
MinOneFile = False
folder_path = []

class SearchAssign:
    def __init__(self, Mt2_Album, Mt2_Artist, Mt2_Folder):

        self.FoundedTracks = []
        mt2_dir_list = os.listdir(Mt2_Folder)

        for mt2_file in mt2_dir_list:
            if mt2_file[-4:] == ".mp3":
                print(mt2_file)
                thefiles.append(mt2_file)


        #fit the album and artist name to URL enconde
        album1 = Mt2_Album.replace(' ','%20')
        artist1 = Mt2_Artist.replace(' ','%20')
        album1 = album1.replace('ü','%C3%BC')
        artist1 = artist1.replace('ü','%C3%BC')
        
        #the Last.Fm API is opened
        var_url = urlopen('http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key=9431a6366225e88f9a1d9d0ce988e893&artist='+ artist1 +'&album='+ album1 +'&format=xml')
        xmldoc = parse(var_url)
        root = xmldoc.getroot()

        #Here MyTag gets the album, artist, and the album cover... Aqui todo es un dolor de cabeza
        self.Album = root[0][0].text
        self.Artist = root[0][1].text
        self.CoverLink = root[0][8].text

        print(self.Album + ": " + self.CoverLink)

        #Download the album cover
        SaveImage.SaveImage("cover.jpg", self.CoverLink)

        #For each album's track
        for track in root.iter('track'):
            #Gets track name
            nametrack = track.find('name').text
            #Gets track number
            numbertrack = track.get('rank')

            for file in thefiles:
                if nametrack.lower() in file.lower():
                    print("un " + nametrack + " osea el " + numbertrack)
                    MinOneFile = True
                    #Aqui se asignan los metadatos a cada archivo... lalalla falta por programar
                    #select the file and set the metadata
                    audiofile = eyed3.load(Mt2_Folder + "/" + file)
                    audiofile.tag.artist = self.Artist
                    audiofile.tag.album = self.Album
                    audiofile.tag.title = nametrack
                    audiofile.tag.track_num = int(numbertrack)
                    
                    #Set the album cover
                    audiofile.tag.images.set(ImageFrame.FRONT_COVER, open('cover.jpg','rb').read(), 'image/jpeg')

                    audiofile.tag.save()

                    self.FoundedTracks.append(nametrack)


if __name__ == '__main__':
    test = SearchAssign("Pinkerton", "Weezer", r"C:\Users\Usuario\Desktop\efgh")