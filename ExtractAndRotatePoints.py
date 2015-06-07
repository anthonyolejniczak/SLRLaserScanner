axis = 2291

from PIL import Image
import os
import math
import time
import sys

fo = open("/Users/aolejniczak/Desktop/SLRLaserScanner/TestImages/FullWicketResults/Points.txt", "w")
dirlist = os.listdir("/Users/aolejniczak/Desktop/SLRLaserScanner/TestImages/FullWicketResults/")
for files in dirlist:
	if files != "CenterCalibration.png" and files != "RotationalAxis.txt" and files != ".DS_Store" and files != ".." and files != "." and files != "Points.txt":
		print "Now processing: " + files
		theta = float(os.path.splitext(files)[0])
		fileToOpen = "/Users/aolejniczak/Desktop/SLRLaserScanner/TestImages/FullWicketResults/" + files
		im = Image.open(fileToOpen)
		width, height = im.size
		px = im.load()
		for i in range(height):
			for j in range(width):
				r, g, b = im.getpixel((j,i))
				if r > 0:
					x = axis - j
					y = i
					z = 0
					xPrime = float("{0:.2f}".format(x*(math.cos(theta*(math.pi/180)))))
					yPrime = float("{0:.2f}".format(y))
					zPrime = float("{0:.2f}".format(x*(math.sin(-1*theta*(math.pi/180)))+z*(math.cos(theta*(math.pi/180)))))
					newPoint = [xPrime, yPrime, zPrime]
					with open('/Users/aolejniczak/Desktop/SLRLaserScanner/TestImages/FullWicketResults/Points.txt','a+') as f:
						f.write(str(newPoint))
						f.write("\n")
