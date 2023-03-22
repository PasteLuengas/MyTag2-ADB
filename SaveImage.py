import os
import requests

def SaveImage(ImageName, ImageUrl):
    f = open(ImageName,'wb')
    response = requests.get(ImageUrl)
    f.write(response.content)
    f.close()