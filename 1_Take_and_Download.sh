for i in 1 2 3 4 5 6 7 8 9 10
do
	# First locate the USB port that is connected to the Canon and reset it.
	lsusb | while read line;
	do
        	if [[ $line == *"Canon"* ]]
                	then
                		numOne=$(cut -d ' ' -f2 <<< "$line")
                		numTwo=$(cut -d ' ' -f4 <<< "$line")
                		numTwo=$(cut -c 1-3 <<< "$numTwo")
                		sudo ./usbreset /dev/bus/usb/$numOne/$numTwo
        	fi
	done
	# Now take the picture.
	gphoto2 --capture-image-and-download --filename Images/Picture$i.cr2 --force-overwrite;
done
