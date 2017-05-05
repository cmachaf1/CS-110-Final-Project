import pygame
import landerver3

class Controller:
	def __init__(self):
		self.text = "Useless"
	
	def controls(self):
		key = pygame.key.get_pressed()
		if key[pygame.K_q]:
			pygame.quit()
			sys.exit()
		if key[pygame.K_LEFT]:
			landerver3.turnlander ("l")
		elif key[pygame.K_RIGHT]:
			landerver3.turnlander("r")
		if key[pygame.K_UP]:
			landerver3.thrust(landerver3.angle)