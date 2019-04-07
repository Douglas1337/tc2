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
#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

arrayDeRs=[]
arrayDeGs=[]
arrayDebs=[]

for x in range (imgH):
    for w in range (imgW):
        pxVal= np.array(img[x,w])
        arrayDeRs.append(pxVal[0])
        arrayDeGs.append(pxVal[1])
        arrayDeBs.append(pxVal[2])
        
# Primeira Técnica
vRs = sum(arrayDeRs)
vGs = sum(arrayDeGs)
vBs = sum(arrayDeBs)

#potenciação de cada banda
vRs = vRs**
vGs = vGs**
vBs = vBs**

sTot = vRs + vGs + vBs

#Raiz quadrada de tudo
sTot = (sTot ** 1/2)