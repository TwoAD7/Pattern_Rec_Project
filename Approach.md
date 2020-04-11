### Approach to problem 
The over all goal of this is to be able to classfiy images based on the following features:
- Color
- Brightness 
- Size 
- Shape
---

_The approach entails_
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
  

