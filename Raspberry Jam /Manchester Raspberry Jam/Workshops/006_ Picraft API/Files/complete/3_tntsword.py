#API setup
from picraft import Vector
from picraft import World, Block

def operation(world, position):
	world.blocks[position] = Block(8, 1)

def main():
    #API setup
    world = World()

    while True:
        #get recent sword hits
        hits = world.events.poll()
        for hit in hits:
            currenthit = hit.pos
            operation(world, currenthit)

if __name__ == "__main__":
	main()
