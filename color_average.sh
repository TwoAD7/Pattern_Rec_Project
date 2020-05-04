#!/bin/bash

#Roy Salinas
#To parse through the subdirectories that contain all of our images

directory="/home/pi/Downloads/train/"
script="/home/pi/code/color_average.py"
echo "You are now looking to extract the color information!"

#The name you enter has to be exact as it appears
echo -n "Enter the exact color FILE NAME you are wanting to use as it appears in '/home/pi/ext_drive': "
read n
color_file_directory="/home/pi/ext_drive/${n}"

echo ${color_file_directory}
#Look through all of the sub-directories in train
for subdir in ${directory}* ; do
	echo "Currently in directory ${subdir}"
	python3 "${script}" "${color_file_directory}" "${subdir}"
done