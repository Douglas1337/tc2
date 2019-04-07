import RPi.GPIO as GPIO
from picamera import PiCamera
import time
    
class CapturaImagens:
    gpios = [(18,6),(23,25),(27,24),(12,17),(22,21)]
    path = '/home/pi/Documents/tc2/'
    
    def captura(self):
        # W = Branco G=Verde, R=Verm, Y=Amarelo, B=Azul
        try:
            camera = PiCamera()
            camera.start_preview(alpha = 128, fullscreen=False, window=(300,300,640,480))
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
                
            
            
        
    
    
    