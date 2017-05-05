import random
import pygame
import math

class Lander (pygame.sprite.Sprite):
	cid = 0
	WHITE = (255,255,255)
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.WHITE = (255,255,255)
		self.name = "Lunar Lander"
		self.fuel = 1000
		self.score = 0
		self.xvelocity = 5
		self.yvelocity = 0
		self.pic = pygame.image.load("TheLander.png").convert()
		self.small = pygame.transform.scale(self.pic, (30,30))
		self.rect = pygame.Rect((100,100),(30,30))
		self.angle = 180
		self.landed = False
		self.accum = 0
		self.turnl = 0
		self.turnr = 0
		self.chars = 0
		self.rotated = self.small
		self.engine = 0
		
		
	def thrust (self, angle):			
		self.engine += 1
		if(self.engine==2):
			self.fuel += -1
			self.engine = 0
			self.yvelocity += (math.sin(math.radians(self.angle)))
			self.xvelocity += (math.cos(math.radians(self.angle)))
	
	def turnlander (self, range):
		if (range == "l"):	
			self.turnl += 1
			if (self.turnl == 1):
				self.angle += 1
				self.turnl = 0
				if (self.angle >= 180):
					self.angle = 180
					
		if (range == "r"):	
			self.turnr += 1
			if (self.turnr == 1):
				self.angle += -1
				self.turnr = 0
				if (self.angle <= 0):
					self.angle = 0


	def control(self):
		key = pygame.key.get_pressed()
		if key[pygame.K_q]:
			pygame.quit()
		elif key[pygame.K_LEFT]:
			self.turnlander ("l")
		elif key[pygame.K_RIGHT]:
			self.turnlander("r")
		elif key[pygame.K_UP]:
			self.thrust(self.angle)
	
	def crash (self, fuel):
		fuelloss = random.randrange(200,400)
		self.chars = fuelloss
		self.fuel -= fuelloss
		
	def respawn (self):
		self.rect.topleft = (50,50)
		self.xvelocity = 5
		self.yvelocity = 0
	
	def gravity (self):
		self.accum += 1
		if (self.accum == 20):
			self.yvelocity -= 1
			self.accum = 0
		
		
		