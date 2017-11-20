
#import libraries
import picamera
from time import sleep
from PIL import Image

#set up the camera
camera = picamera.PiCamera()

try:
	#capture at maximum resolution (~5MP)
	camera.resolution = (800, 600)
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
				r=0
				g=0
				b=0
	
				#get an average of nearby colours
				for u in range(-2, 3):
					for v in range(-2, 3):
						try:
							pixel = pixels[i+u, j+v]
						except IndexError:
							pixel = (0,0,0)

						r = r + pixel[0]
						g = g + pixel[1]
						b = b + pixel[2]
				
				#get the average value
				#(we covered a 3x3 region, so divide by 9)
				r = int(r/25)
				g = int(g/25)
				b = int(b/25)

				#update the pixel
				pixel = (r, g, b)	
				#place the pixel back in the image
				pixels[i,j] = pixel
	finally:
		photo.save('4_blur.jpg', quality=90)

finally:
	camera.close()

