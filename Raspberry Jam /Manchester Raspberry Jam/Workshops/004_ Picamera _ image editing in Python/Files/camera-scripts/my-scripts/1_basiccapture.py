#import libraries
import picamera
from time import sleep

#set up the camera
camera = picamera.PiCamera()

try:
	#capture at maximum resolution (5MP)
	camera.resolution = (2592, 1944)
	camera.vflip = True
	camera.hflip = True

	#allow camera to AWB
	sleep(3)
	
	#Take the photo
	camera.capture('1_basiccapture.jpg')

finally:
	camera.close()

