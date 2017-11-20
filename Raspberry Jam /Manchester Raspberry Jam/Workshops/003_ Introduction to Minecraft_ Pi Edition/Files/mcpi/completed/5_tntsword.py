#Load the Minecraft API
import mcpi.minecraft as minecraft
import mcpi.block as block

#Load the time library, for delays
import time

#Connect API to the currently open world
mc = minecraft.Minecraft.create()

############ Write your program below #############

while True:
	#Get all recent sword hits
	blockhits = mc.events.pollBlockHits()

	#Make the tnt
	for hit in blockhits:
		mc.setBlock(hit.pos.x, hit.pos.y, hit.pos.z, 46, [1])

	#clear hits list and add a short delay
	mc.events.clearAll()
	time.sleep(0.1)

