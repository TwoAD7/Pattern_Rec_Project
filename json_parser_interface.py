import json_parser_module as jp
import sys 


inputfile = sys.argv[1] #passed in by shell script
outfile = sys.argv[2]	#^
#For colors, insert the colors you are interested in finding in the .json file
color_input = color_input.split() #returns array 
colors = color_input

jp.parser(inputfile,outfile,colors)
