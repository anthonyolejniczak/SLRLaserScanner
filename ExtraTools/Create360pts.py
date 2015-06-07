from PIL import Image
import os
import shutil

for i in range (1, 359):
	print "Now making image number: " + str(i) + " degrees."
	if i < 10:
		newFileName = "/Users/aolejniczak/Desktop/SLRLaserScanner/TestImages/Shallot360Results/00" + str(i) + ".png"
	else:
		if i < 100:
			newFileName = "/Users/aolejniczak/Desktop/SLRLaserScanner/TestImages/Shallot360Results/0" + str(i) + ".png"
		else:
			newFileName = "/Users/aolejniczak/Desktop/SLRLaserScanner/TestImages/Shallot360Results/" + str(i) + ".png"
	fileToOpen = "/Users/aolejniczak/Desktop/SLRLaserScanner/TestImages/Shallot360Results/000.png"
	shutil.copyfile(fileToOpen,newFileName)
#	im = Image.open(fileToOpen)
#	im.save(newFileName, "Results")
