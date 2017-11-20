#API setup
from picraft import Vector
from picraft import World, Block

def translate_left(position, data):
	if data == 0:
		return position - Vector(z=1)
	elif data == 1:
		return position + Vector(z=1)
	elif data == 2:
		return position + Vector(x=1)
	else:
		return position - Vector(x=1)

def translate_right(position, data):
	if data == 0:
		return position + Vector(z=1)
	elif data == 1:
		return position - Vector(z=1)
	elif data == 2:
		return position - Vector(x=1)
	else:
		return position + Vector(x=1)

def rotate_clockwise(data):
	if data == 0:
		return 3
	elif data == 1:
		return 2
	elif data == 2:
		return 0
	else:
		return 1

def rotate_anticlockwise(data):
	if data == 0:
		return 2
	elif data == 1:
		return 3
	elif data == 2:
		return 1
	else:
		return 0

def face_to_dataval(face):
	if face == 'x-':
		return 0
	elif face == 'x+':
		return 1
	elif face == 'z-':
		return 2
	elif face == 'z+':
		return 3
	else:
		print('Error: you hit the top face')
		return -1


def operation(world, position, data):
	#center block
	world.blocks[position] = Block(53, data)

	#left block
	new_position = translate_left(position, data)
	new_data = rotate_clockwise(data)
	
	world.blocks[new_position] = Block(53, new_data)
	
	#right block
	new_position = translate_right(position, data)
	new_data = rotate_anticlockwise(data)
	
	world.blocks[new_position] = Block(53, new_data)


def main():
	#API setup
	world = World()

	while True:
		#get recent sword hits
		hits = world.events.poll()
		
		for hit in hits:
			#get rotation
			position = hit.pos
			data = face_to_dataval(hit.face)
			
			#call the building function
			if data != -1:
				operation(world, position, data)


if __name__ == "__main__":
	main()
