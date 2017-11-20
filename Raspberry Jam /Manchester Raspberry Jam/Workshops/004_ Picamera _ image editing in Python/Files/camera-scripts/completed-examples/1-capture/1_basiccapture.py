
#import libraries
import picamera
from time import sleep

#set up the camera
camera = picamera.PiCamera()

try:
	#capture at previewable resolution
	camera.resolution = (1824, 984)
	camera.vflip = True
	camera.hflip = True
	camera.start_preview()

	#allow camera to AWB
	sleep(5)
	camera.capture('1_basiccapture.jpg')

finally:
	camera.close()

