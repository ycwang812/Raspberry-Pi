#!/usr/bin/env python

# Load Libraries
import time
import math
import mcpi.minecraft as minecraft
import mcpi.block as block
import unicornhat as UH

############ Write your program below #############

#Connect Minecraft API to the currently open world
mc = minecraft.Minecraft.create()

#draw canvas
mc.setBlocks(0,0,0, 7,64,7, 0)
mc.setBlocks(0,-1,0, 7,-1,7, 7)

#check canvas
while True:
	for z in range(8):
		for x in range(8):
			#get the current block
			block = mc.getBlockWithData(x, 0, z)
			block_type = block.id
			
			if block_type == 35:
				block_colour = block.data
				if block_colour == 0:
					UH.set_pixel(x, z, 150, 150, 150)
				elif block_colour == 1:
					UH.set_pixel(x, z, 150, 100, 0)
				elif block_colour == 2:
					UH.set_pixel(x, z, 150, 0, 150)
				elif block_colour == 3:
					UH.set_pixel(x, z, 50, 100, 150)
				elif block_colour == 4:
					UH.set_pixel(x, z, 150, 150, 0)
				elif block_colour == 5:
					UH.set_pixel(x, z, 0, 150, 0)
				elif block_colour == 6:
					UH.set_pixel(x, z, 150, 100, 100)
				elif block_colour == 7:
					UH.set_pixel(x, z, 50, 50, 50)
				elif block_colour == 8:
					UH.set_pixel(x, z, 100, 100, 100)
				elif block_colour == 9:
					UH.set_pixel(x, z, 0, 100, 100)
				elif block_colour == 10:
					UH.set_pixel(x, z, 50, 0, 150)
				elif block_colour == 11:
					UH.set_pixel(x, z, 0, 0, 150)
				elif block_colour == 12:
					UH.set_pixel(x, z, 75, 50, 0)
				elif block_colour == 13:
					UH.set_pixel(x, z, 0, 50, 0)
				elif block_colour == 14:
					UH.set_pixel(x, z, 150, 0, 0)
				elif block_colour == 15:
					UH.set_pixel(x, z, 0, 0, 0)
				UH.show()
			else:
				UH.set_pixel(x, z, 0, 0, 0)
				UH.show()
