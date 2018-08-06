import os
from PIL import Image




im = Image.open("Images/1.jpg")
im = im.convert(mode = "L")					#L ->converting to black and white
im.show()