#!/bin/sh

#Roy Salinas
#Use this scrip to parse through the .json files 

filedirectory="/home/pi/ext_drive/train.json" #change this to the directory we are looking into. Still needs to be incorporated for the smaller partitions (Roy - 04.17.20)
outfile="test_out.txt"
script1=json_parser_module.py
script2=json_parser_interface.py
echo "You are running $script1 and $script2"
python3 $script2 "$filedirectory" "$outfile"



#python3 hello.py
#print("hello world")
