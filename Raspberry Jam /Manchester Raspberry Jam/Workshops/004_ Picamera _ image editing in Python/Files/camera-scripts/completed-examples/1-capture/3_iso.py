
#import libraries
import picamera
from time import sleep

#set up the camera
camera = picamera.PiCamera()

try:
	#capture at maximum resolution (~5MP)
	camera.resolution = (1280, 720)
	camera.vflip = True
	camera.start_preview()

	camera.framerate = 90
	camera.shutter_speed = 1000
	camera.iso = 50

	#allow camera to AWB
	sleep(2)
	camera.capture('2_iso.jpg')
	

	camera.iso = 400
	sleep(2)
	camera.capture('3_iso.jpg')

finally:
	camera.close()

