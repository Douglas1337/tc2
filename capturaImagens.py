import RPi.GPIO as GPIO
from picamera import PiCamera
import time
from PIL import Image
import numpy as np
    
class CapturaImagens:
    gpios = [(18,6),(23,25),(27,24),(12,17),(22,21)]
    path = '/home/pi/Documents/tc2/'
    
    def captura(self,overlay):
        # W = Branco G=Verde, R=Verm, Y=Amarelo, B=Azul
        try:
            camera = PiCamera()
            camera.resolution = (800,600)
            camera.start_preview()
            ##Parte de incluir a ROI no preview da camera
            if(overlay ==64):
                img = Image.open('overlay64.png')
            else:
                img = Image.open('overlay64.png')
                
            pad = Image.new('RGB',
                    (((img.size[0] + 31)//32)*32,
                     ((img.size[1] + 15)//16) * 16,
                     ))
            pad.paste(img,(0,0))
            o = camera.add_overlay(pad.tostring(),size = img.size)
            o.alpha = 128
            o.layer = 3
            
            choice =input("Pressione 1 para iniciar: \n ")
            while choice != 1:
                choice = input("Pressione 1 para iniciar: \n")
            
            GPIO.setmode(GPIO.BCM)
            for x in range(len(self.gpios)):
                GPIO.setup(self.gpios[x][0],GPIO.OUT)
                GPIO.setup(self.gpios[x][1],GPIO.OUT)
                GPIO.output(self.gpios[x][0],True)
                GPIO.output(self.gpios[x][1],True)
                time.sleep(5)
                if(x==0):
                    camera.capture(self.path+'white.jpg',resize=(800,600))
                elif(x==1):
                    camera.capture(self.path+'green.jpg',resize=(800,600))
                elif(x==2):
                    camera.capture(self.path+'red.jpg',resize=(800,600))
                elif(x==3):
                    camera.capture(self.path+'yellow.jpg',resize=(800,600))
                elif(x==4):
                    camera.capture(self.path+'blue.jpg',resize=(800,600))
                    
                ##camera.stop_preview()
                GPIO.output(self.gpios[x][0],False)
                GPIO.output(self.gpios[x][1],False)
            camera.stop_preview()
            GPIO.cleanup()
            camera.stop_preview()
            pass
        finally:
            camera.close()
                
            
            
        
    
    
    