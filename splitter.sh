#!/bin/bash

#Roy Salinas
#Used to split a large directory (folder) to a smaller one
#Run this in the directory of the file you are splitting 
#In our case, sudo sh ../train
#However, this has been done already and no need to run it again


size=5000 #amount of pictures in each directory 
dir_name="train"
n=$((`find . -maxdepth 1 -type f | wc -l`/$size+1))
for i in `seq 1 $n`; do
	mkdir -p $dir_name$i;
	find . -maxdepth 1 -type f | head -n $size | xargs -i mv "{}" "$dir_name$i"
done



