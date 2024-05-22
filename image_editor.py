from PIL import Image, ImageEnhance, ImageFilter
import os

path = "./imgs" # folder for unedited images
pathOut = "./editedImgs" # folder for edited images

# Loop through and pick files for editing
for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")
    
# sharpening, BW
    edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(-90)

    # contrast
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)