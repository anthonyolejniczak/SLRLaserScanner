from PIL import Image
im = Image.open("../outfile.jpg")
width, height = im.size
px = im.load()
for i in range(height):
	for j in range(width):
		if str(px[j,i]) != "(0, 0, 0)":
			print str(i) + "," + str(j) + " - "  + str(px[j,i])
