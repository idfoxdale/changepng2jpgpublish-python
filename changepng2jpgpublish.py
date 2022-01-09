#Following is the code for converting png to jpg with the help of pillow library and
#the original file name will be entact. 
#provided extension is 3 characters long for png lol.
#the code is written by me(ishantkumardas) copy it spread it like omiocron.
import os
from PIL import Image
import glob

cwd = os.getcwd() # current working directory unecesarrily long

for image in glob.glob("./*.png"):
    print (image) # just monitoring input image
    im = Image.open(image)
    im.save("{}.jpg".format(image[:-4])) # saving the image with the same name but with jpg extension