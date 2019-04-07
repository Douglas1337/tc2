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
import cv2

choice =input("Pressione 1 para iniciar: \n ")

while choice != 1:
    choice = input("Pressione 1 para iniciar: \n")

#camera.close()
captura = capturaImagens.CapturaImagens()
captura.captura()