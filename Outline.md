### PHASE 1: Setting up the data  
- Extract images to pi  [keaton,roy]
---

### PHASE 2: Preprocessing the files <---- CURRENTLY ON
- parse through the .json files [Roy]
  - look for questions that have the words "colors", "color" 
  - Separate those from our overall testing file. Call it "Color questions"
    - Loop through the answers in color questions to find specific colors 
      - If the question has the keyword "color" and at least half of the answers (5/10) have the color we're looking for, save that image filename.
      - <u>Possible option:</u> make a word bank either with an enumerate call or map (similar to a dictionary in c++). Only look for images that have two (or one) of the colors in the word bank
      - The point of this is to get rid of images that are going to be hard to classify due to large amounts of deviations on the RGB channels of the picture.
- Have separate files for different colors. This will have the color (y_train) since we know all of these pictures should be some "color" [Roy]
---
### PHASE 3: Processing each selected file
- We can download all that we need to the RPI to run this on the Pi. This is preferable to be able to have it centralized where we can all access the code. [Keaton, Roy]
- Use openCV to classify objects in the image from phase 2(if there are multiple objects, grab the largest one) [keaton]
  - Begin to extract features (these are the pixels)  from within the object in question. We are now preparing x_train to have features. [Christine, Roy]
  - We will want our images to have the same number of pixels in order to properly pass them to a classifier. This will be done by looking at the smallest "object" in a picture and reshaping each image to the same amount of pixels. Will have to make sure to use Anti-Aliasing to smooth out picture.(I have something like this already done for something else I did, It's not hard)  [Keaton,Chritsine, Roy]
- Use the pixels inside the object to create an average RGB value. These will be our final x_train features.
---
### PHASE 4: Begin classifying 
- Look at different classifiers to work with [keaton,roy]
  - Need justification for method
- Test each method and error analysis [keaton]
- Take a look at over all status [keaton,roy,christine]
---
### PHASE 5: Testing
- The test.json file does not have answers for its pictures. We will have to use the validation images. 
- Do similar pre-processing to get images that deal with color.
- Test the different methods with the new images from validation. 
- Get error report 
