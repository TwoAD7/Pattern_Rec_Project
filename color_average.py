
#Partly written but mostly put together by Roy (Thankgoodnes for the internet)
#Code to get average color 
#https://stackoverflow.com/questions/43111029/how-to-find-the-average-colour-of-an-image-in-python-with-opencv/43111221

import cv2, numpy as np
from sklearn.cluster import KMeans
from matplotlib.colors import rgb2hex

#from __future__ import print_function
import webcolors
from scipy.spatial import KDTree


rgb2hex = lambda r,g,b: '#%02x%02x%02x' %(r,g,b)
RGB_values = []

def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
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
    colors = sorted([(percent, color) for (percent, color) in zip(hist, centroids)])
    start = 0
    for i in range(len(colors[:])):
    	RGB_values.append(list(colors[i][1]))
    	#print(colors[i][1])
    #print(RGB_values)
    #print("hey")
    #print(colors[0][1])
    #print(list(colors[0][1]))
    RGB_val = np.array(RGB_values)
    a = [ rgb2hex(*RGB_val[i,:]) for i in range(RGB_val.shape[0]) ] #holds hex values for colors 
    print(a)
    #print(RGB_val)
    for color_index in range(len(RGB_val[:])):
    	requested_colour = (RGB_val[color_index][0],RGB_val[color_index][1],RGB_val[color_index][2])
    	actual_name, closest_name = get_colour_name(requested_colour)
    	print("Actual colour name: %s closest colour name: %s" % (actual_name,closest_name))

    for (percent, color) in colors:
        print(color, "{:0.2f}%".format(percent * 100))
        end = start + (percent * 300)
        cv2.rectangle(rect, (int(start), 0), (int(end), 50), \
                      color.astype("uint8").tolist(), -1)
        start = end
    return rect

#_perc, _col = colors[0]

# Load image and convert to a list of pixels
image = cv2.imread('pic.jpg')
img =cv2.imread('pic.jpg')
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

#if k == ord('q'):       # wait for ESC key to exit

#To show the image and the color palette together 
#print(visualize.shape)
#print(image.shape)
#img = image.reshape(visualize.shape[0],visualize.shape[1])

#img_concate_Hori=np.concatenate((visualize,img),axis=1)
#cv2.imshow("Results",img_concate_Hori)
#cv2.waitKey()