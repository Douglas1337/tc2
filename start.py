#coding: utf

#######################
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
import cv2

choice =input("Pressione 1 para iniciar")
while choice != 1:
        choice = input("Pressione 1 para iniciar")


camera = picamera.PiCamera()
camera.start_preview()
GPIO.setmode(GPIO.BCM)

######BRANCA##########
GPIO.setup(18, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.output(18,True)
GPIO.output(6,True)
time.sleep(5)
camera.capture('/home/pi/Documents/tc2/snapshotwhite.jpg')
camera.stop_preview()
GPIO.output(18,False)
GPIO.output(6,False)

######VERDE#######
GPIO.setup(23, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.output(23,True)
GPIO.output(25,True)
time.sleep(5)
camera.capture('/home/pi/Documents/tc2/snapshotgreen.jpg')
camera.stop_preview()
GPIO.output(23,False)
GPIO.output(25,False)

######VERMELHO#######
GPIO.setup(27, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.output(27,True)
GPIO.output(24,True)
time.sleep(5)
camera.capture('/home/pi/Documents/tc2/snapshotred.jpg')
camera.stop_preview()
GPIO.output(27,False)
GPIO.output(24,False)

######AMARELO#######
GPIO.setup(12, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17,True)
GPIO.output(12,True)
time.sleep(5)
camera.capture('/home/pi/Documents/tc2/snapshotyellow.jpg')
camera.stop_preview()
GPIO.output(17,False)
GPIO.output(12,False)

######AZUL#######
GPIO.setup(22, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.output(22,True)
GPIO.output(5,True)
time.sleep(5)
camera.capture('/home/pi/Documents/tc2/snapshotblue.jpg')
camera.stop_preview()
GPIO.output(22,False)
GPIO.output(5,False)

