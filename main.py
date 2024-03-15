from os import remove
import os
from PIL import Image


def png_to_jpg():
    try:
        os.mkdir('Normal_Size_Images')
    except FileExistsError:
        print('Folder already exists')

    path = ('/home/ecmge/documentos/AWS_Test/'
            'Normal_Size_Images/')

    listnames = []
    listdir = os.walk(path)

    print("...Changing Images to jpg...")
    for root, dirs, files in listdir:
        for file in files:
            (fileName, extension) = os.path.splitext(file)
            if (extension == ".png"):
                listnames.append(fileName)

    if (len(listnames) == 0):
        print("No images to change")
    else:
        for i in listnames:
            im = Image.open('Normal_Size_Images/{}.png'.format(i))
            rgb_im = im.convert('RGB')
            rgb_im.save('Normal_Size_Images/{}.jpg'.format(i), quality=95)
            remove('Normal_Size_Images/{}.png'.format(i))
    print("...Finishing Changing Images...")


def changing_names():

    path = ('/home/ecmge/documentos/AWS_Test/'
            'Normal_Size_Images/')
    listdir = os.walk(path)
    a = 1
    for root, dirs, files in listdir:
        for file in files:
            os.rename('{}{}'.format(path, file),
                      '{}image-{}.jpg'.format(path, a))
            a += 1


def re_size():
    try:
        os.mkdir('Thumbnail_Size')
    except FileExistsError:
        print('Folder already exists')

    path = ('/home/ecmge/documentos/AWS_Test/'
            'Normal_Size_Images/')
    images = os.listdir(path)

    print("Starting Image Resize")
    for i in range(len(images)):
        img = Image.open('{}image-{}.jpg'.format(path, i+1))
        small_img = img.resize((1280, 720))
        small_img.save('Thumbnail_Size/image-{}.jpg'.format(i+1))

    print("All images resized")


png_to_jpg()
changing_names()
re_size()
