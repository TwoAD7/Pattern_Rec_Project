#!/bin/bash

#Roy Salinas
#To parse through the subdirectories that contain all of our images

directory="/home/pi/Downloads/train/"
script="/home/pi/code/color_average_single.py"
echo "You are now looking to extract the color information from a single picture!"


echo -n "Enter the exact color IMAGE NAME you are wanting to use as it appears in '/home/pi/ext_drive': "
read n
image_directory="/home/pi/ext_drive/${n}"

echo ${image_directory}
python3 "${script}" "${image_directory}" 