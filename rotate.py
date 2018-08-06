import os
from PIL import Image


for f in os.listdir("pictures"):
	if f.endswith('.jpg'):
		im=Image.open("pictures/"+str(f))
		filename,file_extn=os.path.splitext(f)
		
		im.thumbnail(size)
		im=Image.open("pictures/1.jpg")
		if ch==1:
			out = im.rotate(90)
		else:
			out = im.rotate(-90)	
		out.show()
		im.show()
		im.save(f"300/{filename}.jpg")