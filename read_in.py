import numpy as np
import os 
#Function to read in data after it has been parsed and to format it the way we need it for the 
#classifiers (a multi-dimensional array)
#Reads in the {COLOR}_colorinfo.txt from the ext_drive on the RPI to conver 

def reader(inputfile):
    with open(inputfile,"r") as fin:
        marray= []
        for line in fin:
            array = []
            weights = []
            line = line.strip() #get rid of white space such as "\n"
            line_info = line.split() #split the line based on "words" or "character shapes"
            for element in line_info:
                for character in element:
                    if( character == "]" or character == "'" or character == "[" or character == ","):
                        element =element.replace(character,"") #get rid of the "non-word character"
                try:
                    array.append(float(element))
                except ValueError:
                    continue 
            #grab the percentages for each color for each image 
            if(len(array) <=3):
                weights.append(array[3])
                junk = array.pop(3)
                temp1 = [i * weights[0] for i in array[:3]]
                array = temp1
                marray.append(array)
                continue

            else:
                weights.append(array[3])
                weights.append(array[7])
                weights.append(array[11])
                weights.append(array[15])
                weights.append(array[19])

                #pop the percentages out of the array 
                junk = array.pop(3)
                junk = array.pop(6)
                junk = array.pop(9)
                junk = array.pop(12)
                junk = array.pop(15)
            
                #apply the percentages as the weights 
                temp1 = [i * weights[0] for i in array[:3]]
                temp2 = [i * weights[1] for i in array[3:6]]
                temp3 = [i * weights[2] for i in array[6:9]]
                temp4 = [i * weights[3] for i in array[9:12]]
                temp5 = [i * weights[4] for i in array[12:15]]
            
                array = temp1 +temp2+temp3+temp4+temp5
            
                #print(array)
                marray.append(array)
    
        #print(marray)
        marray = np.asarray(marray)
        print(marray.shape)
    yarray = []
    #Append all of the RGB values for Red as the target variables. Can change this to the word "red" or however we choose
    yname = os.path.split(inputfile) #get rid of path 
    yname = yname[1]
    yname = os.path.splitext(yname)[0]  #get rid of extension
    for i in range(marray.shape[0]):
        yarray.append(yname)
    yarray = np.asarray(yarray)
    return marray,yarray

    fin.close()
