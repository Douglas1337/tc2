import picamera
import RPi.GPIO as GPIO
import time
from time import sleep
import capturaImagens
import cv2
import numpy as np
import math

##le a imagem
img = cv2.imread('blue.jpg')
imgH = img.shape[0]
imgW = img.shape[1]
#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

arrayDeRs=[]
arrayDeGs=[]
arrayDeBs=[]

# na imagem ele separa o R, G, B de cada pixel em posicoes do array
for x in range (imgH):
    for w in range (imgW):
        pxVal= np.array(img[x,w])
        arrayDeRs.append(pxVal[0])
        arrayDeGs.append(pxVal[1])
        arrayDeBs.append(pxVal[2])
        
# Primeira Tecnica

# Potencia de 2 em todos os Rs, Gs e Bs da imagem
arrayDeRs = np.power(arrayDeRs,2)
arrayDeGs = np.power(arrayDeGs,2)
arrayDeBs = np.power(arrayDeBs,2)

intensidadeDeCadaPixel = np.empty(0);


## -- AINDA NAO ACABADO -- ###
for x in np.nditer (arrayDeRs):
    u = math.sqrt(arrayDeRs[x]+arrayDeGs[x]+arrayDeBs[x])
    np.append(intensidadeDeCadaPixel,u)
    
print(u)
   ## np.append(intensidadeDeCadaPixel,u)
    
    
    