import numpy as np
import cv2 as cv
from skimage import io
from google.colab.patches import cv2_imshow

url = "https://drive.google.com/uc?id=1tbNvzsQRtLSgbeuW3DwBmq683lcLCM-g"


myimg2 = io.imread(url)
myimg5 = cv.cvtColor(myimg2,cv.COLOR_BGR2RGB)

cv2_imshow(myimg5)

boundry = [([0,0,150], [100,100,255]),
           ([0,150,0], [100,255,100]),
           ([150,0,0], [255,100,100])]

for (lower,upper) in boundry:
  lower = np.array(lower, dtype = "uint8")
  upper = np.array(upper, dtype = "uint8")
  mask = cv.inRange(myimg5, lower,upper)
  cv2_imshow(mask)
  img = cv.bitwise_and(myimg5,myimg5,mask = mask)
  cv2_imshow(img)
