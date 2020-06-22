import json_parser_module as jp
import sys 

#Written by: Roy Salinas
#Purpose: Serves as the interface to the json_parser module 
#All arguments come from the shell script "parser.sh"

#Colors are the colors we are looking for
#sys.argv[0] is the name of this script, doesn't make sense to pass that in 
#as that is THIS script
inputfile = sys.argv[1] #passed in by shell script
outfile = sys.argv[2]	#^
colors  = sys.argv[3:] #grabbing all of the arguments in bash array in the third index of input

#For colors, insert the colors you are interested in finding in the .json file
color_input = colors#.split()

jp.parser(inputfile,outfile,color_input)
