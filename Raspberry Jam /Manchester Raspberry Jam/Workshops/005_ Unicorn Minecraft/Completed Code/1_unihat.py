#!/usr/bin/env python

# Load Libraries
import time
import math
import mcpi.minecraft as minecraft
import mcpi.block as block
import unicornhat as UH

############ Write your program below #############

#Connect Minecraft API to the currently open world
#mc = minecraft.Minecraft.create()

for y in range(8):
	for x in range(8):
		UH.set_pixel(x, y, 150, 150, 150)
		UH.show();

time.sleep(1)
