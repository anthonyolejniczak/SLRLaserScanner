# For now, I'm using 30 as the cutoff for the red value.
cutoff = 100

from PIL import Image
im = Image.open("TestImages/135.tiff")
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
#		print str(i) + " has ZERO red pixels above the threshold."
		for k in range(width):
			px[k,i] = (0,0,0)
	if startRed > 0 and endRed == 0:
#		print str(i) + " has ONE red pixel above the threshold."
		for k in range(width):
			if k == startRed:
				px[k,i] = (100,100,0)
			else:
				px[k,i] = (0,0,0)
	if startRed > 0 and endRed > 0:
#		print str(i) + " has MULTIPLE red pixel above the threshold."
		mean = int((startRed + endRed)/2)
#		print str(startRed) + "," + str(endRed) + " - Mean: " + str(mean)
		for k in range(width):
			if k == mean:
				px[k,i] = (100,100,0)
				print str(k) + "," + str(i) + " | " + str(px[k,i])
			else:
                               px[k,i] = (0,0,0)
im.save("TestImages/outfile.png", "PNG")
