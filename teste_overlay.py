from time import sleep
import picamera
import numpy as np
from PIL import Image


with picamera.PiCamera() as camera:
    camera.resolution=(1024,768)
    camera.start_preview()
    img = Image.open('overlay.png')
    pad = Image.new('RGB',
                    (((img.size[0] + 31)//32)*32,
                     ((img.size[1] + 15)//16) * 16,
                     ))
    pad.paste(img,(0,0))
    
    o = camera.add_overlay(pad.tostring(),size = img.size)
    o.alpha = 128
    o.layer = 3
    
    while True:
        sleep(1)
                    
	