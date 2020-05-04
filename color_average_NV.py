
#Partly written but mostly put together by Roy (Thankgoodnes for the internet)
#Code to get average color 
#https://stackoverflow.com/questions/43111029/how-to-find-the-average-colour-of-an-image-in-python-with-opencv/43111221

import cv2, numpy as np
from sklearn.cluster import KMeans
from sklearn.cluster import MiniBatchKMeans 
import matplotlib.colors as mc
#from __future__ import print_function
import webcolors
from scipy.spatial import KDTree
import os
import sys

rgb2hex = lambda r,g,b: '#%02x%02x%02x' %(r,g,b)
#RGB_values = []

def closest_colour(requested_colour):
    min_colours = {} #creat our map
    #Let's iterate through the map that contains our names and hex values
    for name,key in webcolors.CSS3_NAMES_TO_HEX.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name #our key is the distance from that color and our value is the name of that closes color
    #print(min_colours[min(min_colours.keys())])
    #Return the minimum 
    return min_colours[min(min_colours.keys())] #organize the map ascending based on the keys (distance) Return min value in list

def get_colour_name(requested_colour):
    try:
        #print("We are trying")
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        #print("We are in the exception")
        closest_name = closest_colour(requested_colour)
       # print(closest_name)
        actual_name = None
    return actual_name, closest_name


def visualize_colors(cluster, centroids):
    # Get the number of different clusters, create histogram, and normalize
    labels = np.arange(0, len(np.unique(cluster.labels_)) + 1)
    (hist, _) = np.histogram(cluster.labels_, bins = labels)
    hist = hist.astype("float")
    hist /= hist.sum()

    # Create frequency rect and iterate through each cluster's color and percentage
    rect = np.zeros((50, 300, 3), dtype=np.uint8)
    colors = sorted([(percent, color) for (percent, color) in zip(hist, centroids)]) #list from zipped values. Returns: [percent, [RGB VAL]]

    #Moved this piece of code inside for loop. Need to extract this info for every picture without clutering return statement 
    """
    for i in range(len(colors[:])): #loop through all of the rows
    	RGB_values.append(list(colors[i][1])) #append all the RGB values 
    RGB_val = np.array(RGB_values,dtype=int)
    a = [ rgb2hex(*RGB_val[i,:]) for i in range(RGB_val.shape[0]) ] #holds hex values for colors 
    _color_names = []
    for color_index in range(len(RGB_val[:])):
        requested_colour = (RGB_val[color_index][0],RGB_val[color_index][1],RGB_val[color_index][2])
        actual_name, closest_name = get_colour_name(requested_colour)
        _color_names.append(closest_name)
        #print(f"The color is {closest_name}")
        #print("Actual colour name: %s closest colour name: %s" % (actual_name,closest_name))

    start = 0
    i = 0
    #loop to get percentages
    for (percent, color) in colors:
        perc ="{:0.2f}%".format(percent * 100)
        #print(f"RGB values are {color} with {perc} in the image for color {_color_names[i]}")
        end = start + (percent * 300)
        cv2.rectangle(rect, (int(start), 0), (int(end), 50), \
                      color.astype("uint8").tolist(), -1)
        start = end
        i=i+1
    """
    return rect,colors #returns the rectangle to visualize the color percentages and list containing our sorted colors [%, [RGB]


# Load image and convert to a list of pixels

#filedirectory = "/home/pi/ext_drive/red.txt"
#rootdir = "/home/pi/Downloads/train/{}".format(sys.arv[1])

#reading in our image names 
filedirectory=sys.argv[1]
with open(filedirectory,"r") as imgn:
    print("Opening your file")
    print(f"{filedirectory}")
    img_names = imgn.readlines() #read line by line 
    imgn.close()


print("Starting the loop")
save_all = []
counter = 0

split_color_file = os.path.splitext(filedirectory)
print(split_color_file) #splits it from the ".txt" extension

def color_average(rootdir):
    counter = 0
#looping through all of our images
    #fout = open("{}_colorinfo.txt".format(split_color_file[0]),"w")
    with open("{}_colorinfo.txt".format(split_color_file[0]),"a") as fout:
        for _file in os.listdir(rootdir):
            #print(f"{_file}")
            for IMAGE in img_names:
                #print(IMAGE.rstrip("\n"))
                if str(_file) == IMAGE.strip(): #strip the new line character 
                    img_names.remove(IMAGE) #to get rid of that image name to speed up the loop 
                    print(f"WE FOUND IT HER SIR, HERE SHE IS {_file}")
                    RGB_values = []
                    temp = []
                    print("LOOKING TO TRY IT NOW SIR")
                    image = cv2.imread(os.path.join(rootdir, _file))
                    print("read the image")
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                    print("converted image")
                    reshape = image.reshape((image.shape[0] * image.shape[1], 3))
                    print("reshaped image")
                    #https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans
                    cluster = MiniBatchKMeans(init= 'k-means++',n_clusters=5,max_no_improvement= 15).fit(reshape)
                    #cluster = KMeans(n_clusters=5).fit(reshape)
                    print("clustering")
                    visualize,_col = visualize_colors(cluster, cluster.cluster_centers_)
                    #visualize = cv2.cvtColor(visualize, cv2.COLOR_RGB2BGR) #comment out since we are not visualizing our color percentages, just grabbing colors 

                    print("Grabbing RGB values and percentages")

# Since we are not wanting to print info out for every picture, we can comment this section out. We are not needing hex values either.
#                """
#               #grab RGB values 
#                for i in range(len(_col[:])): #loop through all of the colors for that image 
#                    RGB_values.append(list(_col[i][1]) + list(_col[i][0])*100)#save RGB vals and percentages 
#                RGB_val = np.array(RGB_values,dtype=int)
#                """
#
#                """
#                #get hex values
#                hex_values = [ rgb2hex(*RGB_val[i,:]) for i in range(RGB_val.shape[0]) ] #holds hex values for colors 
#                _color_names = []
#
#                #get closest color name
#                for color_index in range(len(RGB_val[:])): #Nx3 array (N being the number of dominant colors in the image)
#                    requested_colour = (RGB_val[color_index][0],RGB_val[color_index][1],RGB_val[color_index][2])
#                    actual_name, closest_name = get_colour_name(requested_colour)
#                    _color_names.append(closest_name)
#                """
# 
#           Grabbing percentages and colors 
                    start=0
                    i=0
                    for (percent, color) in _col:
                        #perc ="{:0.2f}%".format(percent * 100)
                        print("{} {:0.2f}%".format(color,percent*100))
                        a = "{:0.2f}".format(percent * 100)
                        _color = "{}".format(color)
                        z = [_color,a]
                        #print(z)
                        temp.append(z)
                        #print(temp)
                        end = start + (percent * 300)
                        cv2.rectangle(visualize, (int(start), 0), (int(end), 50), \
                            color.astype("uint8").tolist(), -1)
                        start = end
                        i=i+1

                    d = _file.split() + temp #merged list
                    #print(_file.split())
                    print("Writing out to file now")
                    #for data in d:
                    #print(f"{d[0]} {d[1]} {d[2]} {d[3]} {d[4]} {d[5]}")
                    fout.write(f"{d[0]} {d[1]} {d[2]} {d[3]} {d[4]} {d[5]}\n")

                    #save_all.append(d) #save file name and color information 
                    #print(save_all)
                    counter = counter+1
                    print(f"You have gone through {counter} images.")

#with open("/home/pi/ext_drive/red_colorinfo.txt","w") as fout:
#    print("Writing out to file now")
#   fout.writelines(save_all)
    fout.close()

color_average(sys.argv[2])



#fout.write(f"RGB values are {color} with {perc} in the image for color {_color_names[i]}")
"""
#image = cv2.imread('flower.jpg')
#img =cv2.imread('pic.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
reshape = image.reshape((image.shape[0] * image.shape[1], 3))
# Find and display most dominant colors
cluster = KMeans(n_clusters=5).fit(reshape)
visualize = visualize_colors(cluster, cluster.cluster_centers_)
visualize = cv2.cvtColor(visualize, cv2.COLOR_RGB2BGR)

cv2.imshow('visualize', visualize)
cv2.imshow('Input image', img)
while True:
    k = cv2.waitKey(30000) & 0xFF
    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()
    elif k == ord('s'):  # wait for 's' key to save and exit
        cv2.imwrite('arvid2.jpg', img)
        cv2.destroyAllWindows()
    if cv2.getWindowProperty("image", 0) == -1:
        break
"""
#if k == ord('q'):       # wait for ESC key to exit

#To show the image and the color palette together 
#print(visualize.shape)
#print(image.shape)
#img = image.reshape(visualize.shape[0],visualize.shape[1])

#img_concate_Hori=np.concatenate((visualize,img),axis=1)
#cv2.imshow("Results",img_concate_Hori)
#cv2.waitKey()