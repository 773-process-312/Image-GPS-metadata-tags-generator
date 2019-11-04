import os
from PIL import Image
import piexif
from random import randint
import random


def gpsch(dir1, imgg):


    exiff = piexif.load(imgg)

    if str(exiff['GPS'][2]) and str(exiff['GPS'][4]) and str(exiff['GPS'][6]):
        print(exiff['GPS'][2],"   ",exiff['GPS'][4],"   ",exiff['GPS'][6])


    os.chdir(dir1)
    archivos = os.listdir(dir1)
    for dirlist in archivos:
        i1 = random.randint(-99, 99)
        i2 = random.randint(-99, 99)

        im = Image.open(dirlist)
        exif_dict = piexif.load(im.info["exif"])
        if str(exiff['GPS'][2]) and str(exif_dict['GPS'][2]):
            exif_dict['GPS'][2] = (
            (exiff['GPS'][2][0][0], exiff['GPS'][2][0][1]), (exiff['GPS'][2][1][0], exiff['GPS'][2][1][1]),
            (exiff['GPS'][2][2][0] + i1, exiff['GPS'][2][2][1]))
        if str(exiff['GPS'][4]) and str(exif_dict['GPS'][4]):
            exif_dict['GPS'][4] = (
            (exiff['GPS'][4][0][0], exiff['GPS'][4][0][1]), (exiff['GPS'][4][1][0], exiff['GPS'][4][1][1]),
            (exiff['GPS'][4][2][0] + i2, exiff['GPS'][4][2][1]))
        if str(exiff['GPS'][6]) and str(exif_dict['GPS'][6]):
            exif_dict['GPS'][6] = exiff['GPS'][6]

        print(exif_dict['GPS'][2],"   ",exif_dict['GPS'][4],"   ",exif_dict['GPS'][6])

        try:
            exif_bytes = piexif.dump(exif_dict)
            im.save(dirlist, "jpeg", exif=exif_bytes)
        except:
            print("Error ")


Ref = input(" Ingresa el nombre de la imagen:")
Dir = input(" Ingresa el nombre de la carpeta:")
gpsch(Dir, Ref)