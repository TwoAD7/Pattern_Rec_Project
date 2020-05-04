import read_in as ri 
import pickle 
import sys 
import os 

#Pickling script
filename = sys.argv[1]
print(filename)
names = os.path.split(filename)
name = names[1]
name = os.path.splitext(name)[0]
print(name)
def object_transfer(filename):
	x,y=ri.reader(filename)
	xob = open("x_data_{}".format(name) ,"wb")
	yob = open("y_data_{}".format(name),"wb")
	pickle.dump(x,xob)
	pickle.dump(y,yob)
	xob.close()
	yob.close()
	#return xob,yob
	print("The pickle files are %s %s" % ("x_data_{}".format(name),"y_data_{}".format(name)))
object_transfer(filename)
