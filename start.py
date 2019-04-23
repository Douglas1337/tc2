#coding: utf

####### GPIOS #########
#LED BRANCO = 6, 18   #
#LED AMARELO = 17, 12 #
#LED AZUL = 22 ,5     #
#LED VERMELHO= 24 ,27 #
#LED VERDE =  25, 23  #
#######################

#import Tkinter as tk
import picamera
import RPi.GPIO as GPIO
import time
from time import sleep
import capturaImagens
import ImProc
import cv2
import sys

#choice =input("Pressione 1 para iniciar: \n ")

#while choice != 1:
#    choice = input("Pressione 1 para iniciar: \n")

#camera.close()
overlay = sys.argv[1]
captura = capturaImagens.CapturaImagens()
captura.captura(overlay)


##pega o tamanho da imagem
tamanhoImg = str(overlay)

listaDeCores = ['green','red','white','yellow','blue']
intensidadeDePixelsEmCadaCor=[]
for x in range (len(listaDeCores)):
    processamento = ImProc.ImProc()
    process = processamento.firstTec(listaDeCores[x],tamanhoImg)
    intensidadeDePixelsEmCadaCor.append(process)
print (len(intensidadeDePixelsEmCadaCor[1]))

