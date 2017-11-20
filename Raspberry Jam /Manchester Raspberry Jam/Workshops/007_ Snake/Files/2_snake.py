#Libraries
import pygame
from pygame.locals import *
import unicornhat as UH

import random
from time import sleep
from copy import deepcopy

#our extra code
import snakeutils

def draw_game(snake, food, game_over):
	#if the player has lost, don't draw the game
	if game_over:
		for y in range(0,8):
			for x in range(0,8):
				UH.set_pixel(x, y, 50, 0, 0)
	else:
		#clear canvas
		for y in range(0,8):
			for x in range(0,8):
				UH.set_pixel(x, y, 0, 0, 0)
	
		#draw food (below snake)
		UH.set_pixel(food[0], food[1], 255, 0, 0)
			
		#draw snake
		for i in range(0, len(snake)):
			UH.set_pixel(snake[i][0], snake[i][1], 100, 100, 100)
	#update Unicorn HAT
	UH.show()

def main():
	random.seed()
	pygame.init()
	quit_game = False

	#important game variables
	snake = []
	direction = 0
	food = [0, 0]
	place_food = True
	game_over  = False

	#before entering game loop, set up the start position

	#get start position from external code
	direction = snakeutils.startdir(startpos_x, startpos_y)

	#finally, create a pygame window (required for keyboard input)
	pygame.init()
	screen = pygame.display.set_mode((480, 320))
	pygame.display.set_caption('Snake is running')
	pygame.mouse.set_visible(0)
	
	#main game loop
	while quit_game == False:

		#get key presses for player control
		for event in pygame.event.get():
			if (event.type == KEYUP) or (event.type == KEYDOWN):
				if (event.key == K_ESCAPE):
					quit_game = True
				#add player controls here

		#place food if it is not currently placed

		#find the new position of the head
		
		#the old tail needs to be removed (unless food was just ate)
		if snake[1] == food:
			place_food = True
		else:
			del snake[len(snake)-1]
		
		#shift the list and insert new head

		#finally, check the player hasn't lost:
		#out of bounds
		#snake eats its body

		#draw to output (Unicorn HAT)
		draw_game(snake, food, game_over)
		sleep(0.333) #change to adjust difficulty

if __name__ == "__main__":
	main()
