#Load the Minecraft API
import mcpi.minecraft as minecraft
import mcpi.block as block

#Connect API to the currently open world
mc = minecraft.Minecraft.create()

############ Write your program below #############

#Get the player position
position = mc.player.getTilePos()

#lower the position below the player
position.y = position.y - 1

#place a block there
mc.setBlock(position.x, position.y, position.z, block.GOLD_BLOCK)
