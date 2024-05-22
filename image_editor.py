from PIL import Image, ImageEnhance, ImageFilter
import os

path = "./imgs" # folder for unedited images
pathOut = "./editedImgs" # folder for edited images

# Loop through and pick files for editing
for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")