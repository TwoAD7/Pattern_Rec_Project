import json 
import sys
#Written by: Roy Salinas
#Purpose: To iterate through the .json files

#with open("/mnt/c/Users/Owner/Desktop/Annotations/train.json","r") as f:
#with open("test.json","r") as f:

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
def duplicate_check(ourlist):  
    setOfElems = set()
    for elem in ourlist :
        if elem in setOfElems:
            return True
        else:
            setOfElems.add(elem)        
    return False

def parser(inputfile,outfile,myList=[],*args):
    print(f"{inputfile}\n")
    print(myList)
    with open(inputfile,"r") as f:
        data = json.load(f)
        f.close()
    image_files = []
    _counter =0
    for _map in data: #loop for maps in .json file
        if _counter % 1000 == 0:
            print(f"Have parsed through {_counter} out of 23953")
        for key in _map: #loop for each key in the map 
            if(key == "question"):
                for word in _map[key].split(): #loop for each word in the value for the "question" key
                    if(word == "color" or word == "color?"):       #if our question has anything to do with color 
                        #image_files.append(_map["image"])
                        counter =0
                        for _col_index, _col in enumerate(myList):
                            for sub_map in _map["answers"]: #loop to iterate through each map in the "answer" key
                                #print(f"Beginnig to iterate through new sub_map c:{counter} _i:{_col_index}")
                                for _word in sub_map["answer"].split(): #loop through each word in the answer string
                                    if _word == myList[_col_index]:
                                        #print(f"{myList[_col_index]} passed the if statement")
                                        #print(f"{_color}")
                                        #print(sub_map["answer"])
                                        counter = 1 +counter
                                        if counter >= 3:	#out threshold to save an image file.
                                            if(duplicate_check(image_files)):
                                                #print(f"counter is {counter}")
                                                #print("checking for duplicates")
                                                continue
                                            else:
                                                image_files.append("%s : %s" %(myList[_col_index],_map["image"]))
                                                #image = "image"
                                                #print(f"appended {_map[image]}")
                                                counter = 0
                                                continue
                                        #else: #for debuggin purposes 
                                        #    print(f"counter is not greater than 3 {counter}")
                                    
                        
        _counter=counter+1 
    print(len(image_files))	
    #To writw out to file 
    with open(outfile,"w") as fout:
        for item in image_files:
           # print(f"{item}\n")
            fout.write(f"{item}\n")
        fout.close()    
#print(len(image_files))
#print(image_files[:3])
