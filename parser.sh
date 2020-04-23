#!/bin/bash

#Roy Salinas
#Use this scrip to parse through the .json files 
filedirectory="/mnt/c/Users/Owner/Desktop/Annotations/train.json"
script1=json_parser_module.py
script2=json_parser_interface.py
   
echo -n "Enter the total number of colors you are looking for:"
read n 
echo "Enter colors followed by the 'Enter' key after each one :"
i=0 
  
# Read upto the size of  
# given array starting from 
# index, i=0 
while [ $i -lt $n ]; do
    # To input from user 
    read a[$i] 
  
    # Increment the i = i + 1 
    i=`expr $i + 1` 
done

printf -v outfile "%s," "${a[@]}.txt" 
outfile=${outfile%?}  #to get rid of the last comma 
#echo ${outfile}
echo "The colors you entered are ${a[@]}"
echo "You are running $script1 and $script2"
#pass in the input file, outfile, and the colors we are looking for
python3 $script2 "$filedirectory" "$outfile" ${a[@]}
