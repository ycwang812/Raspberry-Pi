
#import libraries
import picamera
from time import sleep
from PIL import Image

#set up the camera
camera = picamera.PiCamera()

try:
	#capture at maximum resolution (~5MP)
	camera.resolution = (1280, 720)
	camera.framerate = 90
	camera.shutter_speed = 1000
	camera.iso = 50
	camera.vflip = True

	#allow camera to AWB
	sleep(1)
	camera.capture('1_unedited.jpg')

	#load the image back into python
	photo = Image.open('1_unedited.jpg')
	pixels = photo.load()

	#apply an edit to each pixel
	try:
		for i in range(photo.size[0]):
			for j in range(photo.size[1]):
				#seperate the current pixel
				pixel = pixels[i,j]

				#seperate the colours
				r = pixel[0]
				g = pixel[1]
				b = pixel[2]

				#Perform our edits
				r = r + 50
				g = g + 50
				b = b + 50

				#update the pixel
				pixel = (r, g, b)	
				#place the pixel back in the image
				pixels[i,j] = pixel
	finally:
		photo.save('2_brightness.jpg', quality=90)

finally:
	camera.close()

