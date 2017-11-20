#Load the Minecraft API
import mcpi.minecraft as minecraft
import mcpi.block as block

#Connect API to the world
mc = minecraft.Minecraft.create()

############ Write your program below #############

mc.postToChat("Hello, World!");
