import os
from PIL import Image
im=Image.open("images/1.jpg")
#out=im.transpose(Image.FLIP_LEFT_RIGHT)
#out=im.transpose(Image.FLIP_TOP_BOTTOM)
#out=im.transpose(Image.ROTATE_90)
#out=im.transpose(Image.ROTATE_180)
out=im.transpose(Image.ROTATE_270)
out.show()