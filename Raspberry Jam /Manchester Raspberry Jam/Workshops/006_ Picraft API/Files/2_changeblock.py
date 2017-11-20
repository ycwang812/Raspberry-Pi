#Change block
#change the block the player is standing on

#API setup
from picraft import Vector
from picraft import World, Block
world = World()

#-------Your Code-------#

#get block below player
position = world.player.tile_pos
position -= Vector(y=1) 

#set the block
world.blocks[position] = Block(1, 0)
