import json 
import sys

#Written by: Roy Salinas
#Purpose: Module to parse through the .json file
#Arguments come from json_parser_interface.sh

if __name__ == "__main__":
	print("Runnning the parser in terminal!")
else:
	print("Imported the parser module! Running as an imported file.")


#pass in the name of the file, then the list. Important that we have a pointer to the arguments
#since an arrays are just pointers
####################################################
#NOTE
#The input file, outfile, and list of colors passed are changed in the interface file (json_parser_interface.py)

####################################################


#function to check for duplicates 
def duplicate_check(_ourlist):  
    ourlist = list(set(_ourlist))
    for item in _ourlist :
        if item  not in ourlist:
            ourlist.add(item)
            return True       
        return False

def parser(inputfile,outfile,myList=[],*args):
    print(f"The input file is: {inputfile}")
    #print(f"Colors we are looking for are: {myList}")
    with open(inputfile,"r") as f:
        data = json.load(f)
        f.close()
    image_files = []
    #_counter =0
    for _map in data: #loop for maps in .json file
        for key in _map: #loop for each key in the map 
            if(key == "question"):
                for word in _map[key].split(): #loop for each word in the value for the "question" key
                    if(word == "color" or word == "color?"):       #if our question has anything to do with color 
                        counter =0
                        for _col_index, _col in enumerate(myList):
                            for sub_map in _map["answers"]: #loop to iterate through each map in the "answer" key
                                for _word in sub_map["answer"].split(): #loop through each word in the answer string
                                    if _word == _col:
                                        if counter > 3:
                                            if(duplicate_check(image_files)):
                                                continue
                                            else:
                                                counter =0
                                                image_files.append("%s " %(_map["image"])) #append the image name 
                                        counter = 1 +counter

    #For some strange reason, it appends some images twice. This snippet is to get rid of those.
    updates_images = list(set(image_files))
 	

    print(f"You have {len(updates_images)} image files for {myList}")
    print(f"The outfile is {outfile}")

    #To write out to file 
    with open(outfile,"w") as fout:
        for item in updates_images:
            #print(f"{item}\n")
            fout.write(f"{item}\n")
        fout.close()    
