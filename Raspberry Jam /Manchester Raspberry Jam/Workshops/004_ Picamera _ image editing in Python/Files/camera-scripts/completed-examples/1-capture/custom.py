
#import libraries
import picamera
from time import sleep

#set up the camera
camera = picamera.PiCamera()

try:
	#capture at maximum resolution (~5MP)
	camera.resolution = (1280, 720)
	camera.vflip = True
	camera.hflip = False
	camera.start_preview()
	
	sleep(0.5)
	g = camera.awb_gains
	camera.awb_mode = 'off'
	camera.awb_gains = g

	camera.shutter_speed = 1500
	camera.iso = 50

	#allow camera to AWB
	sleep(3)
	camera.resolution = (2592, 1944)
	camera.capture('custom.jpg')

finally:
	camera.close()

