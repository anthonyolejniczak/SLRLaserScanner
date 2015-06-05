# For now, I'm using 100 as the cutoff for the red value.
cutoff = 100

from PIL import Image
import os

dirlist = os.listdir("/Users/aolejniczak/Desktop/SLRLaserScanner/TestImages/FullShallotTIFF/")
for files in dirlist:
	if files.endswith ('.tiff'):
		print "Now processing: " + files
		newFiles = os.path.splitext(files)[0]
		print newFiles
		fileToOpen = "/Users/aolejniczak/Desktop/SLRLaserScanner/TestImages/FullShallotTIFF/" + files
		print fileToOpen
		im = Image.open(fileToOpen)
		print im.format, im.size, im.mode
		width, height = im.size
		px = im.load()
		#putpixel = px.putpixel
		for i in range(height):
			startRed = 0
			endRed = 0
			foundEnd = False
			for j in range(width):
				r, g, b = im.getpixel((j,i))
				if r > cutoff and startRed == 0:
					startRed = j
				if r < cutoff and startRed > 0 and foundEnd == False and j-1 > startRed:
					endRed = j-1
					foundEnd = True
			if startRed == 0 and endRed == 0:
				for k in range(width):
					px[k,i] = (0,0,0)
			if startRed > 0 and endRed == 0:
				for k in range(width):
					if k == startRed:
						px[k,i] = (100,100,0)
					else:
						px[k,i] = (0,0,0)
			if startRed > 0 and endRed > 0:
				mean = int((startRed + endRed)/2)
				for k in range(width):
					if k == mean:
						px[k,i] = (100,100,0)
#						print str(k) + "," + str(i) + " | " + str(px[k,i])
					else:
	       	 	                       px[k,i] = (0,0,0)

		fileName = "TestImages/FullShallotResults/" + newFiles + ".png"
		im.save(fileName, "PNG")
