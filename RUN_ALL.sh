#!/bin/bash
#Script to execute everything you need 

echo "You are beginning the process!"
echo -n "Are you looking to parse through all or one image? "
read input
if [ "${input}" == "all" ]; then 
	echo "Beginning to parse through your data files..."
	./parser.sh
	echo "Beginning to extract color information from images..."
	./color_average.sh
	echo "Beginning to pickle data..."
	./data_pickling.sh
	echo "DONE"
else
	./color_average_single.sh
	echo "Beginning to pickle data..."
	./data_pickling.sh
fi

