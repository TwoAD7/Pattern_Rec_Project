### Approach to problem 
The over all goal of this is to be able to classfiy images based on the following features:
- Color
- Brightness 
- Size 
- Shape
---

__The approach entails__
* Extracting images from [Viz-wiz](https://vizwiz.org/tasks-and-datasets/vqa/) 
  * Extraction of images will be chosen to best represent each feature 
* Pixel data extraction 
  * This will be done with OpenCV or the Python Image Library (PIL)
  * This will be done in pre-processing the images
  * This is where feature specification will be handled. 
  * Color
     * Will be extracted via the RGB channels
  * Brightness 
     * Will look at contour maps of pixels based on intensity gradient. This will compare pixels that are next to each other. 
  * Shape 
     * Will utilize OpenCV for edge recogntion. 
  * Size 
      * Will utilize OpenCV for this. This is still to be thought about further as a _close up_ picture of a pen might seem large when it really isn't.
  
---

__Webhosting and data storage__
* The data is hoped to be stored remotely on a webserver on a raspberrypi in which an external hardrive will be connected to. SSH capabilities will be set up to access RPI to access data and download to local machines if necessary. 
---
__User Interface__
The goal of the MCC group is to have the user interface hosted on a webserver (of jupyter notebook) in which the user can do the following:
* Upload image 
* Ask simple questions such as:
   > What is this?
   
   > What color is this?
   
   > What shape is this?
   
* Have answer returned on same server in a couple of seconds. 
* Allow user to upload multiple images 

