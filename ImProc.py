import picamera
import RPi.GPIO as GPIO
import time
from time import sleep
import capturaImagens
import cv2
import numpy as np


img = cv2.imread('blue.jpg')
imgH = img.shape[0]
imgW = img.shape[1]
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

vR=0
vG=0
vB=0

arrayDeRs=[]
arrayDeGs=[]
arrayDebs=[]

for x in range (imgH):
    for w in range (imgW):
        pxVal= np.array(img[x,w])
        arrayDeRs.append(pxVal[0])
        arrayDeGs.append(pxVal[1])
        arrayDeBs.append(pxVal[2])