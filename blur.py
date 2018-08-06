import os
from PIL import Image
from PIL import ImageFilter
for f in os.listdir("pictures"):
	if f.endswith('.jpg'):
		im=Image.open("pictures/"+str(f))
		filename,file_extn=os.path.splitext(f)
		
		im.thumbnail(size)
		im=Image.open("pictures/1.jpg")
		blurred_image = im.filter(ImageFilter.GaussianBlur(radius=50))
		out.show()
		im.show()
		im.save(f"300/{filename}.jpg")
