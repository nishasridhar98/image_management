import os					#helps in navgating to different folders in the text editors
from PIL import Image

# im = Image.open("Images/1.png")			#to open a single image in bitmap format
# im.show()



size = (300,300)


for f in os.listdir("Images"):
	if f.endswith(".jpg"):
		im = Image.open("Images/"+ str(f))			#to open a single image in bitmap format
		filename, file_extn = os.path.splitext(f)
		im.thumbnail(size)
		#im.show()		
		print(filename)							#to show the edited image on screen
		im.save(f"thumbnail_300/{filename}.png")		#to save it in a designated file