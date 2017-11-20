#API setup
from picraft import Vector
from picraft import World, Block

def operation(world, position, data):
	#center block
	world.blocks[position] = Block(53, data)

	#left block
	
	#right block


def main():
	#API setup
	world = World()

	while True:
		#get recent sword hits
		hits = world.events.poll()
		
		for hit in hits:
			#get position and orientation for stairs
			position = hit.pos
			data = face_to_dataval(hit.face) #this function needs to be made
			
			#call the building function
			if data != -1:
				operation(world, position, data)


if __name__ == "__main__":
	main()
