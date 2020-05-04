#!/bin/bash

echo "Enter the file name of color info file you want to transfer data from."
echo -n "The name should be as it appears in '/home/pi/ext_drive/': "
read filename 

script="/home/pi/code/data_pickling.py"
fin="/home/pi/ext_drive/${filename}"
echo "${fin}"
python3 "${script}" "${fin}"
