#Load the picraft API
from picraft import World, Block, Vector

#Connect API to the world
world = World()

############ Write your program below #############

while True:
    #get recent sword hits
    hits = world.events.poll()

    #for each recent hit
    for hit in hits:
        #place some TNT at the hit location
        currentpos = hit.pos
        world.blocks[currentpos] = Block(46, 1)
        #place additional blocks
        world.blocks[currentpos + Vector(x=1)] = Block(46, 1)
        world.blocks[currentpos - Vector(x=1)] = Block(46, 1)
        world.blocks[currentpos + Vector(y=1)] = Block(46, 1)
        world.blocks[currentpos - Vector(y=1)] = Block(46, 1)
        world.blocks[currentpos + Vector(z=1)] = Block(46, 1)
        world.blocks[currentpos - Vector(z=1)] = Block(46, 1)
