import picamera
import RPi.GPIO as GPIO
import time
from time import sleep
from PIL import Image
import matplotlib.pyplot as plt
import capturaImagens
import cv2
import numpy as np
import math
import os


class ImProc:
    path = '/home/pi/Documents/tc2/histogramas/'
    
    
    def histogramas(self,nome,cores,overlay):
        
        
        RGBArray = np.empty([0])
    #concatena todos os RGB de das cores 'green','red','white','yellow','blue' nesta ordem
        
        for x in range(len(cores)):
            nomeArquivo = 'CRPD_'+overlay+cores[x]+'.jpg'
            #img = cv2.imread(self.path+nomeArquivo)
            img = cv2.imread(nomeArquivo)
            bgr= cv2.split(img)
            histB= np.array(cv2.calcHist(bgr,[0],None,[256],[0,256]))
            RGBArray = np.append(RGBArray,histB)
            histG= np.array(cv2.calcHist(bgr,[1],None,[256],[0,256]))
            RGBArray = np.append(RGBArray,histG)
            histR= np.array(cv2.calcHist(bgr,[2],None,[256],[0,256]))
            RGBArray = np.append(RGBArray,histB)

        #se o arquivo existe
        if(os.path.isfile(self.path+'Todos.csv')): #SE SIM 
            csv=np.genfromtxt(self.path+'Todos.csv', delimiter='\t') #LE O ARRAY EXISTENTE
            data = np.array(csv) #TRANSFORMA NUM NPARRAY
            data = np.column_stack((data,RGBArray)) #STACK COLOCA EM OUTRA COLUNA
            np.savetxt(self.path+'Todos.csv',data, delimiter='\t',fmt='%d')
                          
        else: #SENAO
            f = open(self.path+'Todos.csv','w+') #CRIA O CSV
            csv=np.genfromtxt(self.path+'Todos.csv', delimiter='\t')
            data = np.array(csv)
            b = np.append(data,RGBArray)
            np.savetxt(self.path+'Todos.csv',b,delimiter='\t',fmt='%d') #E ESCREVE O ARRAY NA COLUNA
        