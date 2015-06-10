import cv2
import numpy as np
import os
import time
import sys


## Importing all the mouth images
mouths = {}
for i in os.listdir("./mouths"):
    if i.endswith(".jpg"):
        print i
        img = cv2.imread("./mouths" + "/" + i, 0)
        mouths["" + i] = img
        continue
print mouths

actualImg = mouths.itervalues().next()

## Ploting them as an animation
for key,value in mouths.items():
    ### Fast mouth showing
    cv2.imshow('window', value)
    cv2.waitKey(1)
    time.sleep(0.2)

    ### Fade Mouths
    # for IN in range(0,10):
    #     fadein = IN/100.0
    #     dst = cv2.addWeighted( actualImg, fadein, value, fadein, 0)#linear $
    #     cv2.imshow('window', dst)
    #     cv2.waitKey(1)
    #     #print fadein
    #     time.sleep(0.05)
    #     if fadein == 1.0: #blendmode mover
    #         fadein = 1.0
    # actualImg = value




