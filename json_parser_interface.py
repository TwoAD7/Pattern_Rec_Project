import json_parser_module as jp
import sys 


#colors are the colors we are looking for
inputfile = sys.argv[1] #passed in by shell script
outfile = sys.argv[2]	#^
#inputfile="./test.json"
#For colors, insert the colors you are interested in finding in the .json file
colors = ["red","green"]
jp.parser(inputfile,outfile,colors)
