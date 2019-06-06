#coding: utf

####### GPIOS #########
#LED BRANCO = 6, 18   #
#LED AMARELO = 17, 12 #
#LED AZUL = 22 ,5     #
#LED VERMELHO= 24 ,27 #
#LED VERDE =  25, 23  #
#######################


import picamera
import RPi.GPIO as GPIO
import time
from time import sleep
import capturaImagens
import ImProc
import numpy as np
import cv2
import sys
import os
 
    
path = '/home/pi/Documents/tc2/'


overlay = sys.argv[1]
captura = capturaImagens.CapturaImagens()
captura.captura(overlay)

tamanhoImg = str(overlay)
nomeAmostra =raw_input("ID Amostra: \n")
listaDeCores = ['green','red','white','yellow','blue']
processamento = ImProc.ImProc()
processamento.histogramas(nomeAmostra,listaDeCores,tamanhoImg)



#Salva os arrays de cada cor em um CSV
a0 = np.asarray(intensidadeDePixelsEmCadaCor[0])
np.savetxt(path+"planilhas/green.csv", a0,delimiter=",", fmt='%f')
caminhoTodos = path+"planilhas/Green/Green.csv"
createCSV(a0,caminhoTodos)
a1 = np.asarray(intensidadeDePixelsEmCadaCor[1])
np.savetxt(path+"planilhas/red.csv", a1,delimiter=",", fmt='%f')
caminhoTodos = path+"planilhas/Red/Red.csv"
createCSV(a1,caminhoTodos)
a2 = np.asarray(intensidadeDePixelsEmCadaCor[2])
np.savetxt(path+"planilhas/white.csv", a2,delimiter=",", fmt='%f')
caminhoTodos = path+"planilhas/White/White.csv"
createCSV(a2,caminhoTodos)
a3 = np.asarray(intensidadeDePixelsEmCadaCor[3])
np.savetxt(path+"planilhas/yellow.csv", a3,delimiter=",", fmt='%f')
caminhoTodos = path+"planilhas/Yellow/Yellow.csv"
createCSV(a3,caminhoTodos)
a4 = np.asarray(intensidadeDePixelsEmCadaCor[4])
np.savetxt(path+"planilhas/blue.csv", a4,delimiter=",", fmt='%f')
caminhoTodos = path+"planilhas/Blue/Blue.csv"
createCSV(a4,caminhoTodos)


