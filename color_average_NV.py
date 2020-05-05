
#Partly written but mostly put together by Roy (Thankgoodnes for the internet)
#Code to get average color 
#https://stackoverflow.com/questions/43111029/how-to-find-the-average-colour-of-an-image-in-python-with-opencv/43111221

import cv2, numpy as np
from sklearn.cluster import KMeans
from sklearn.cluster import MiniBatchKMeans 
import matplotlib.colors as mc
import webcolors
from scipy.spatial import KDTree
import os
import sys

rgb2hex = lambda r,g,b: '#%02x%02x%02x' %(r,g,b)
#RGB_values = []

def closest_colour(requested_colour):
    min_colours = {} #creat our map
    #Let's iterate through the map that contains our names and hex values
    for name,key in webcolors.CSS3_NAMES_TO_HEX.items(): #look in webcolors.py for this map version 1.11.1
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


    return rect,colors #returns the rectangle to visualize the color percentages and list containing our sorted colors [%, [RGB]


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

split_color_file = os.path.splitext(filedirectory) #split it from the .txt extension 
print(split_color_file) 

def color_average(rootdir):
    counter = 0
    with open("{}_colorinfo.txt".format(split_color_file[0]),"a") as fout:
        for _file in os.listdir(rootdir): #look through our directory of images 
            for IMAGE in img_names:
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

                    #Grabbing percentages and colors 
                    start=0
                    i=0
                    for (percent, color) in _col:
                        print("{} {:0.2f}%".format(color,percent*100))
                        a = "{:0.2f}".format(percent * 100)
                        _color = "{}".format(color)
                        z = [_color,a]
                        temp.append(z)
                        end = start + (percent * 300)
                        cv2.rectangle(visualize, (int(start), 0), (int(end), 50), \
                            color.astype("uint8").tolist(), -1)
                        start = end
                        i=i+1

                    d = _file.split() + temp #merged list
                    print("Writing out to file now")
                    fout.write(f"{d[0]} {d[1]} {d[2]} {d[3]} {d[4]} {d[5]}\n")
                    #              Name RGB%1   RGB%2    RGB%3   RGB%4   RGB%5  

                    counter = counter+1
                    print(f"You have gone through {counter} images.")


    fout.close()

color_average(sys.argv[2])
