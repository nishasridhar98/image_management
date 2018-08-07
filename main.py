from PIL import Image, ImageFilter
import os

while True:
	print("1. Rotate Image /n 2. Convert Image to Black and White /n 3. Blur the Image /n 4. Change the size")
	num = int(input("Enter the index number what you want to do: "))
	# Open all the images present in the folder where images are stored
	
	if num == 1:
		x = input("Enter 'R' to rotate right or 'L' to rotate left: ")
		# Add code to perform rotate operation and save the images
	if num == 2:
		# Add code to convert images to black and white
		dest = input("Enter the full path to where you want to store the images: ")
		for f in os.listdir("Images"):#listdir gives the list of files in that folder
			if f.endswith('.jpg'):
				im = Image.open("Images/"+ str(f))#y is str(f) used??
				filename, file_extn = os.path.splitext(f)#splitext splits the filename nd extension
				im=im.convert(mode='L')
				im.save(f"{dest}/{filename}.jpg")

	if num == 3:
		# Add code to blur the images
		dest = input("Enter the full path to where you want to store the images: ")
		for f in os.listdir("Images"):#listdir gives the list of files in that folder
			if f.endswith('.jpg'):
				im = Image.open("Images/"+ str(f))#to open a single image n bitmap format
				filename, file_extn = os.path.splitext(f)#splitext splits the filename nd extension
				im = im.filter(ImageFilter.BLUR)
				im.save(f"{dest}/{filename}.jpg")

	if num == 4:
		# Add code to change the size of the images
		dest = input("Enter the full path to where you want to store the images: ")
		size = input("Enter the size: ")
		for f in os.listdir("Images"):#listdir gives the list of files in that folder
			if f.endswith('.jpg'):
				im = Image.open("Images/"+ str(f))
				filename, file_extn = os.path.splitext(f)#splitext splits the filename nd extension
				im.thumbnail(size)
		 		#im.save(f) #saves in the same folder
				im.save(f"{dest}/{filename}.jpg")
