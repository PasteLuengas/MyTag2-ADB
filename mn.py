import mt1_FileUpload
import mt1_songRecognition

FileLink = mt1_FileUpload.uploadFile(r"C:\Users\Usuario\Desktop\y2mate.com - The World Has Turned And Left Me Here.mp3")

Song = mt1_songRecognition.recognizeSong(FileLink)

print("----------------------")
print(Song.Artist)
print(Song.Title)
print(Song.Album)
print(Song.TrackNumber)
print(Song.CoverLink)

Song.SetData_Method1(r"C:\Users\Usuario\Desktop\y2mate.com - The World Has Turned And Left Me Here.mp3")