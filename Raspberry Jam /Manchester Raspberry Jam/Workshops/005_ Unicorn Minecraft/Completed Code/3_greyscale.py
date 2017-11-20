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
				if block_colour == 7:
					UH.set_pixel(x, z, 50, 50, 50)
				elif block_colour == 8:
					UH.set_pixel(x, z, 100, 100, 100)
				elif block_colour == 0:
					UH.set_pixel(x, z, 150, 150, 150) 
				UH.show()
			else:
				UH.set_pixel(x, z, 0, 0, 0)
				UH.show()
