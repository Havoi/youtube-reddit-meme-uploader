from PIL import Image
from resizeimage import resizeimage
def resize():

    img = Image.open("Images/1.png")
    img = resizeimage.resize_contain(img, [1080,1920],bg_color=(0,0,0))
    img.save('Images/1.png', img.format)
    img.close()