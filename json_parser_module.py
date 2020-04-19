import json 
import sys
#Written by: Roy Salinas

#with open("/mnt/c/Users/Owner/Desktop/Annotations/train.json","r") as f:
#with open("test.json","r") as f:

if __name__ == "__main__":
	print("Runnning the parser in terminal!")
else:
	print("Imported the parser module! Running as an imported file.")


#pass in the name of the file, then the list. Important that we have a pointer to the arguments
#since an arrays are just pointers
#print(f"The file name is {filenam
####################################################
#NOTE
#The input file, outfile, and list of colors passed are changed in the interface file (json_parser_interface.py)

####################################################

def parser(inputfile,outfile,myList=[],*args):
    print(f"{inputfile}\n")
    with open(inputfile,"r") as f:
        data = json.load(f)
        f.close()
    image_files = []
    counter =0
    for _map in data: #loop for maps in .json file
        if counter % 1000 == 0:
            print(f"Have parsed through {counter} out of 23953")
        for key in _map: #loop for each key in the map 
            if(key == "question"):
                for word in _map[key].split(): #loop for each word in the value for the "question" key
                    if(word == "color"):
                        #image_files.append(_map["image"])
                        for sub_map in _map["answers"]: #loop to iterate through each map in the "answer" key 
                            for _word in  sub_map["answer"].split(): #loop through each word in the answer string
                                for _index,_color in enumerate(myList): #loop through each color in the list I passed to this function. Check if any word matches the "_color"
                                    if _word == _color:
                                        #print(f"{_color}")
                                        #print(sub_map["answer"])
                                        image_files.append("%s : %s" %(_color,_map["image"]))
        counter=counter+1 
    print(len(image_files))	
    with open(outfile,"w") as fout:
        for item in image_files:
           # print(f"{item}\n")
            fout.write(f"{item}\n")
        fout.close()    
#print(len(image_files))
#print(image_files[:3])
