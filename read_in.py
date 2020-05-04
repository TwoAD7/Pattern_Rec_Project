import numpy as np


def reader(inputfile):
	with open("red_colorinfo.txt","r") as fin:
		marray= []
		for line in fin:
			array = []
			weights = []
			line = line.strip() #get rid of white space such as "\n"
			line_info = line.split()
			for element in line_info:
				for character in element:
					if( character == "]" or character == "'" or character == "[" or character == ","):
						element =element.replace(character,"")
				try:
					array.append(float(element))
				except ValueError:
					continue 
			#grab the percentages for each color for each image 
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
		return marray

	fin.close()