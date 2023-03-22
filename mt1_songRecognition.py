#Import libs
import requests
import json
import SaveImage
import os
import eyed3
from eyed3.id3.frames import ImageFrame


class recognizeSong:
    def __init__(self, SongLink):

        #Sending song to API
        data = {
            'url': SongLink,
            'return': 'spotify',
            'api_token': 'test'
        }

        resultURL = requests.post('https://api.audd.io/', data=data)
        rstxt = resultURL.text
        data = json.loads(rstxt)
        print(rstxt)
       
       #If there isn't an error

        if not data["status"] == "error":

            #Getting artist, title and album
            data2 = json.dumps(data["result"])
            data3 = json.loads(str(data2))

            self.Artist = data3["artist"]
            self.Title = data3["title"]
            self.Album = data3["album"]
            self.Year = data3["release_date"][0:4]
            print(self.Year)

            #Getting track number
            data4 = json.dumps(data3["spotify"])
            data5 = json.loads(str(data4))

            self.TrackNumber = data5["track_number"]
            self.DiscNumber = data5["disc_number"]

            #Getting Album Cover Image URL
            data6 = json.dumps(data5["album"])
            data7 = json.loads(str(data6))
            imagelist = str(data7["images"]).split(",", 3)
            imagelist2 = str(imagelist[2]).split(":")
            link = imagelist2[1] + ":" +imagelist2[2]

            charactersToDelete = " '}"

            for x in range(len(charactersToDelete)):
                link = link.replace(charactersToDelete[x], "")
            
            self.CoverLink = link

        else:
            print("3rror")

    #Set the metadata to the audio file
    def SetData_Method1(self, FilePath1):
        #Download the image
        SaveImage.SaveImage("cover.jpg", self.CoverLink)

        #select the file and set the metadata
        audiofile = eyed3.load(FilePath1)
        audiofile.tag.artist = self.Artist
        audiofile.tag.album_artist = self.Artist
        audiofile.tag.album = self.Album
        audiofile.tag.title = self.Title
        audiofile.tag.release_date = int(self.Year)
        audiofile.tag.recording_date = int(self.Year)
        audiofile.tag.track_num = int(self.TrackNumber)
        audiofile.tag.disc_num = int(self.DiscNumber)

        #Add album cover
        audiofile.tag.images.set(ImageFrame.FRONT_COVER, open('cover.jpg','rb').read(), 'image/jpeg')

        audiofile.tag.save()
        
        #Delete cover.jpg
        if os.path.exists("cover.jpg"):
            os.remove("cover.jpg")

if __name__ == '__main__':
    testeo = recognizeSong("https://transfer.sh/tJdOy9/y2mate.com%20-%20The%20Smashing%20Pumpkins%20Where%20Boys%20Fear%20to%20Tread.mp3")
    print("Artista: " + testeo.Album)
    print("------------------")
    testeo.SetData_Method1(r"C:\Users\Usuario\Desktop\mtst2\y2mate.com - The Smashing Pumpkins Where Boys Fear to Tread.mp3")
    print("parece que si sirvio")
