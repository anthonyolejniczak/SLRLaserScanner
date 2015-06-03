from PIL import Image
import os

dirlist = os.listdir("/Users/aolejniczak/Desktop/SLRLaserScanner/TestImages/Results/")
for files in dirlist:
	sum = 0
	count = 0
	if files == "CenterCalibration.png":
		print "Now processing: " + files
		fileToOpen = "/Users/aolejniczak/Desktop/SLRLaserScanner/TestImages/Results/" + files
		im = Image.open(fileToOpen)
		print im.format, im.size, im.mode
		width, height = im.size
		px = im.load()
		for i in range(height):
			for j in range(width):
				r, g, b = im.getpixel((j,i))
				if r > 0:
					count = count + 1
					sum = sum + j
	if count > 0:
		print "The mean value (and thus the rotational axis) is: " + str(int(sum/count))
