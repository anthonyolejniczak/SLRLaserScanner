# For now, I'm using 100 as the cutoff for the red value.
cutoff = 150

from PIL import Image
import os

dirlist = os.listdir("/Users/aolejniczak/Desktop/SLRLaserScanner/TestImages/FullWicketTIFF/")
for files in dirlist:
	if files.endswith ('.tiff'):
#		print "Now processing: " + files
		newFiles = os.path.splitext(files)[0]
		fileToOpen = "/Users/aolejniczak/Desktop/SLRLaserScanner/TestImages/FullWicketTIFF/" + files
		im = Image.open(fileToOpen)
		print im.format, im.size, im.mode
		width, height = im.size
		px = im.load()
		for i in range(height):
#			print "Row #" + str(i)
			startRed = 0
			endRed = 0
			for j in range(width):
				r, g, b = im.getpixel((j,i))
				if r > cutoff and startRed == 0:
					startRed = j
			for l in reversed(range(width)):
				r, g, b = im.getpixel((l,i))
				if r > cutoff and endRed == 0:
					endRed = l
#			print "     StartRed = " + str(startRed)
#			print "     EndRed = " + str(endRed)
			if startRed == 0 and endRed == 0:
				for k in range(width):
					px[k,i] = (0,0,0)
			if startRed > 0 and endRed == startRed:
				for k in range(width):
					if k == startRed:
						px[k,i] = (100,100,0)
					else:
						px[k,i] = (0,0,0)
			if startRed > 0 and endRed > 0 and endRed != startRed:
				brightest = 0
				brightestLocation = 0
				for a in range(startRed,endRed):
					red, green, blue = im.getpixel((a,i))
					if a == startRed:
						brightestLocation = a
						brightest = red
					else:
						if red > brightest:
# For row 1580, column 2680 is startRed, and 2696 is the brightest red value (196)
							brightest = red
							brightestLocation = a
#							print "New Brightest Location: " + str(a)
				for k in range(width):
					if k == brightestLocation:
						px[k,i] = (100,100,0)
#						print str(k) + "," + str(i) + " | " + str(px[k,i])
					else:
	       	 	                       px[k,i] = (0,0,0)

		fileName = "TestImages/FullWicketResults/" + newFiles + ".png"
		im.save(fileName, "PNG")
