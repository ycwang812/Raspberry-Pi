
#import libraries
import picamera
from time import sleep
from PIL import Image

#set up the camera
camera = picamera.PiCamera()

try:
	#capture at maximum resolution (~5MP)
	camera.resolution = (1280, 720)
	camera.framerate = 60
	camera.vflip = True
	camera.hflip = True
	camera.start_preview()

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
				r_temp = (j/4) / 200.0
				g_temp = (j/4) / 200.0
				b_temp = (j/2) / 200.0

				r_temp = int(r_temp * r)
				g_temp = int(g_temp * g)
				b_temp = int(b_temp * b)

				r = r_temp + r / 2
				g = g_temp + g / 2
				b = b_temp + b / 2

				#update the pixel
				pixel = (r, g, b)	
				#place the pixel back in the image
				pixels[i,j] = pixel
	finally:
		photo.save('6_vertical.jpg', quality=90)

finally:
	camera.close()

