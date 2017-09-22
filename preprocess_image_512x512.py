import os
import sys
from PIL import Image
from resizeimage import resizeimage


def walkDirectory(rootdir):
    print(rootdir)
    for root, subDirs, files in os.walk(rootdir):
        for dirname in subDirs:
            if not dirname == outputFolder:
                walkDirectory(os.path.join(root,dirname))
        for name in files:
            try:
                transformImage(root,name)
            except IOError:
                print("Coult not read {0}".format(os.path.join(root,name)))


def transformImage(path,name):
    """Cropt the image to a 512x512 square"""
    with open(os.path.join(path,name), 'r+b') as file:
        with Image.open(file) as image:
            transformValid = True  #resizeimage.resize_cover.validate(image,[512,512])
            if transformValid:
                cover = resizeimage.resize_cover(image, outputFormat, validate=False)
                cover.save(os.path.join(outputPath,name),image.format)
            else:
                print("Coult not tranform {0}".format(os.path.join(path,name)))

imageDirectory = 'D:\\CenaInsta\\Images\\InstagramBatch\\Images'
outputFolder = '_Output'
outputPath =  os.path.join(imageDirectory,outputFolder)
if not os.path.exists(outputPath):
    os.makedirs(outputPath)
outputFormat = [512,512]
walkDirectory(imageDirectory)
print("Job done!")
