import random
#	DIRECTION is a number:
#	0	-	up
#	1	-	right
#	2	-	down
#	3	-	left


#Make sure the snake moves away from the wall when the game starts
def startdir(x, y):
	horizontal = -3.5 + x
	vertical = -3.5 + y
	
	#should move away from the sides
	if abs(horizontal) >= abs(vertical):
		if horizontal < 0:
			return 1
		else:
			return 3
	#should move away from the top/bottom
	else:
		if vertical < 0:
			return 2
		else:
			return 0


#get the new position for the snake head, based on 
def movement(pos, direction):
	if   direction == 0:
		pos[1] = pos[1] - 1
	elif direction == 1:
		pos[0] = pos[0] + 1
	elif direction == 2:
		pos[1] = pos[1] + 1
	else:
		pos[0] = pos[0] - 1	
	return pos


#places food randomly, in a clear space
def place_food(snake):
	x_prop = 0
	y_prop = 0
	allow = False

	#try random places until an empty one is found
	while allow == False:
		allow = True
		x_prop = random.randint(0,7)
		y_prop = random.randint(0,7)
		for piece in snake:
			if x_prop == piece[0]:
				if y_prop == piece[1]:
					allow = False
	#position is confirmed unoccupied
	return [x_prop, y_prop]
