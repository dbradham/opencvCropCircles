import cv2
import numpy as np
#load in a xml file that has feature data
cascade = cv2.CascadeClassifier('third.xml')

img = cv2.imread('coloCircles2013.png')
h = img.shape[0]
w = img.shape[1]
locations = []

pivots = cascade.detectMultiScale(img, 22, 22)
for (x, y, w, h) in pivots:
  cv2.circle(img,(x+w/2,y+h/2), 3, (0,0,255), -1)
  cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
  locations.append([x+w/2,y+h/2])
print(len(locations))
name = 'coloCircles2013_markup.png'
cv2.imwrite(name, img)
#keep this line commented out if you are using large imagery, such as the .png's being used in this project.
#cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
