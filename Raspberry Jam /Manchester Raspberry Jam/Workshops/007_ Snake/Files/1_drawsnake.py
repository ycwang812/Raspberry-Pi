#Libraries
import pygame
from pygame.locals import *
import unicornhat as UH

import random
import time
import os
from time import sleep
from copy import deepcopy

#our extra code
import snakeutils

def draw_game(snake, food, gameover):
	print("draw_game not implemented")

def main():
	random.seed()
	pygame.init()
	quit_game = False

	#important game variables
	timebase = time.time()
	score = 0
	snake = []
	direction = 0
	food = [0, 0]

	placefood = True
	gameover  = False

	#before entering game loop, set up the start position
	startpos_x = random.randint(0,7)
	startpos_y = random.randint(0,7)
	snake.append([startpos_x, startpos_y])

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
				if (event.key == K_SPACE):
					#this helps me take photos
					sleep(5)
				if (event.key == K_w):
					if direction != 2:
						direction = 0
				elif (event.key == K_d):
					if direction != 3:
						direction = 1
				elif (event.key == K_s):
					if direction != 0:
						direction = 2
				elif (event.key == K_a):
					if direction != 1:
						direction = 3

		#place food if it is not currently placed
		if placefood == True:
			food = snakeutils.place_food(snake)
			placefood = False

		#move the snake
		temp = deepcopy(snake)	
		head_pos = temp[0]

		head_pos = snakeutils.movement(head_pos, direction)
		
		#shift the list and insert new head
		snake.reverse()
		snake.append(head_pos)
		snake.reverse()

		#if food wasn't ate, the old tail needs to be removed
		if snake[1] == food:
			placefood = True
		else:
			del snake[len(snake)-1]

		#finally, check the player isn't "dead"
		#out of bounds
		head = snake[0]
		if (head[0] < 0) or (head[0] > 7):
			gameover = True
		elif (head[1] < 0) or (head[1] > 7):
			gameover = True
		#snake eats its body
		for i in range (1, len(snake)):
			if snake[i] == snake[0]:
				gameover = True

		#All the game logic is complete
		#draw to output (Unicorn HAT)
		draw_game(snake, food, gameover)
		
		#Update score
		if gameover == False:
			newtime = time.time() - timebase
			newscore = (len(snake)*1000)+(int(newtime)*10)
			if (newscore != score):
				os.system('clear')
				print(newscore)
				score = newscore

		#wait for the next turn
		sleep(0.333)

		if gameover:
			sleep(0.667)
			quit_game = True

	print("Final Score: " + str(score))

if __name__ == "__main__":
	main()
