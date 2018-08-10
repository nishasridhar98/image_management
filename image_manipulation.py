from PIL import Image, ImageFilter
import os

while True:
	print("1. Rotate Image \
		   2. Convert Image to Black and White \
		   3. Blur the Image \
		   4. Change the size\
		   5. Quit")
	num = int(input("Enter the index number what you want to do: "))
	
	if num == 1:
		src = input("Enter the full path of the folder where the images are present: ")
		x = input("Enter 'R' to rotate right or 'L' to rotate left: ")
		dest = input("Enter the full path to where you want to store the images: ")
		# Add code to perform rotate operation and save the images
		for f in os.listdir(src):#listdir gives the list of files in that folder
			if f.endswith('.jpg') | f.endswith('.JPG'):
				im = Image.open(src+"/"+ str(f))
				filename, file_extn = os.path.splitext(f)#splitext splits the filename nd extension
				if x == "R":
					im=im.rotate(90)
					im.save(f"{dest}/{filename}.jpg")
				elif x == "L":
					im = im.rotate(-90)
					im.save(f"{dest}/{filename}.jpg")
				else:
					print("enter 'R' or 'L' ")

	if num == 2:
		# Add code to convert images to black and white
		src = input("Enter the full path of the folder where the images are present: ")		
		dest = input("Enter the full path to where you want to store the images: ")
		for f in os.listdir(src):#listdir gives the list of files in that folder
			if f.endswith('.jpg') | f.endswith('.JPG'):
				im = Image.open(src+"/"+ str(f))#y is str(f) used??
				filename, file_extn = os.path.splitext(f)#splitext splits the filename nd extension
				im=im.convert(mode='L')
				im.save(f"{dest}/{filename}.jpg")

	if num == 3:
		# Add code to blur the images
		src = input("Enter the full path of the folder where the images are present: ")		
		dest = input("Enter the full path to where you want to store the images: ")
		for f in os.listdir(src):#listdir gives the list of files in that folder
			if f.endswith('.jpg') | f.endswith('.JPG'):
				im = Image.open(src+"/"+ str(f))#to open a single image n bitmap format
				filename, file_extn = os.path.splitext(f)#splitext splits the filename nd extension
				im = im.filter(ImageFilter.BLUR)
				im.save(f"{dest}/{filename}.jpg")

	if num == 4:
		# Add code to change the size of the images
		src = input("Enter the full path of the folder where the images are present: ")		
		dest = input("Enter the full path to where you want to store the images: ")
		size = (300,300)
		for f in os.listdir(src):#listdir gives the list of files in that folder
			if f.endswith('.jpg') | f.endswith('.JPG'):
				im = Image.open(src+"/"+ str(f))
				filename, file_extn = os.path.splitext(f)#splitext splits the filename nd extension
				im.thumbnail(size)
				im.save(f"{dest}/{filename}.jpg")


	if num == 5:
		break

