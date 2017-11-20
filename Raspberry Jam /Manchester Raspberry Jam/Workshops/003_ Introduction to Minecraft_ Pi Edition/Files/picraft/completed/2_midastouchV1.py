#Load the picraft API
from picraft import World, Block, Vector

#Connect API to the world
world = World()

############ Write your program below #############

#Get the player position
position = world.player.tile_pos

#lower the position below the player
position -= Vector(y=1)

#place a block there
world.blocks[position] = Block('gold_block')

