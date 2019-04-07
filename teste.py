import picamera
import RPi.GPIO as GPIO
import time
from time import sleep
import capturaImagens
import cv2


camera = picamera.PiCamera()
GPIO.setmode(GPIO.BCM)
camera.start_preview()
sleep(10)
camera.start_preview()

GPIO.setup(22, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.output(22,True)
GPIO.output(21,True)
sleep(5)
camera.capture('/home/pi/Documents/tc2/snapshotblue.jpg')
camera.stop_preview()
GPIO.output(22,False)
GPIO.output(21,False)
###################
GPIO.cleanup()




'''
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
GPIO.setup(21, GPIO.OUT)
GPIO.output(22,True)
GPIO.output(21,True)
time.sleep(5)
camera.capture('/home/pi/Documents/tc2/snapshotblue.jpg')
camera.stop_preview()
GPIO.output(22,False)
GPIO.output(21,False)
###################
GPIO.cleanup()
'''