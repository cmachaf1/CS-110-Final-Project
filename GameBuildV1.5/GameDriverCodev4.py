import pygame
import landerver3
import sqlite3
import terrainV2
import sys


def main():
	

	pygame.init()
	spaceship = landerver3.Lander()
	Clock = pygame.time.Clock()
	size = [600,500]
	Window = pygame.display.set_mode(size)
	pygame.display.set_caption('Lunar Lander')
	WHITE = (255,255,255)
	BLACK = (0,0,0)
	basicfont = pygame.font.SysFont("Arial", 18)
	moon = terrainV2.Terrain()
	pygame.draw.lines(Window, WHITE, False, moon.pointlist, 1)
	moveaccum = 0
	
	
	def Textshow(score):
		if (score==50):
			text = basicfont.render("Perfect Landing! Mission Success!", True, WHITE, BLACK)
		elif (score==25):
			text = basicfont.render("Good Landing! Could've gone better though...", True, WHITE, BLACK)
		elif (score==5):
			text = basicfont.render("Ouch! At least you landed...", True, BLACK, WHITE)
		elif (score==-1):
			text = basicfont.render("Game Over", True, WHITE, BLACK)
			score += 1
			pygame.quit()
		else:
			spaceship.crash(spaceship.fuel)
			text = basicfont.render("Your lander crashed. You lost " + str(spaceship.chars) + " units of fuel.", True, WHITE, BLACK)
		try:
			textrect = text.get_rect()
			textrect.centerx = Window.get_rect().centerx
			textrect.centery = Window.get_rect().centery
			Window.blit(text,textrect)
			spaceship.score += score
		except Exception as err:
			print ("Game Over")
		
		
	while True:
		for event in pygame.event.get():
			if event.type == 'QUIT':
				pygame.quit()
				sys.exit()
		
		thelist = spaceship.rect.collidelistall(moon.rects)
		
		Window.blit(spaceship.small, spaceship.rect)	
			
		if len(thelist) == 1:
			if (spaceship.fuel <= 0):
				Textshow(-1)
			else:	
				spaceship.landed == True
				Textshow(0)
				spaceship.respawn()
		elif(len(thelist) >= 2):
			if (spaceship.fuel <= 0):
				Textshow(-1)
			elif ((abs(spaceship.xvelocity) + abs(spaceship.yvelocity) < 10) and (80 <= spaceship.angle <= 100)):
				Textshow(50)
			elif ((abs(spaceship.xvelocity) + abs(spaceship.yvelocity) < 30) and (80 <= spaceship.angle <= 100)): 
				Textshow(25)
			elif ((abs(spaceship.xvelocity) + abs(spaceship.yvelocity) < 50) and (80 <= spaceship.angle <= 100)):
				Textshow(5)
			else:
				Textshow(0)
			spaceship.respawn()
		else:
			spaceship.score += 0
		
		
		
		fueltext = basicfont.render("Fuel:  " + str(spaceship.fuel),True, WHITE, BLACK)
		fueltextrect = fueltext.get_rect()
		fueltextrect.left = 0
		fueltextrect.centery = 15
		Window.blit(fueltext, fueltextrect)	
		
		scoretext = basicfont.render("Score:  " + str(spaceship.score),True, WHITE, BLACK)
		scoretextrect = scoretext.get_rect()
		scoretextrect.left = 0
		scoretextrect.centery = 35
		Window.blit(scoretext, scoretextrect)
		
		angletext = basicfont.render("Angle:  " + str(spaceship.angle),True, WHITE, BLACK)
		angletextrect = angletext.get_rect()
		angletextrect.left = 0
		angletextrect.centery = 55
		Window.blit(angletext, angletextrect)
		
		xveltext = basicfont.render("Horizontal Velocity:  " + str(spaceship.xvelocity),True, WHITE, BLACK)
		xveltextrect = xveltext.get_rect()
		xveltextrect.left = 0
		xveltextrect.centery = 75
		Window.blit(xveltext, xveltextrect)
			
		yveltext = basicfont.render("Vertical Velocity:  " + str(spaceship.yvelocity),True, WHITE, BLACK)
		yveltextrect = yveltext.get_rect()
		yveltextrect.left = 0
		yveltextrect.centery = 95
		Window.blit(yveltext, yveltextrect)
		
		moveaccum += 1
		if (moveaccum == 4):
			spaceship.rect.topleft = ((spaceship.rect.left + spaceship.xvelocity),(spaceship.rect.top - spaceship.yvelocity))
			moveaccum = 0
			
		if (spaceship.rect.right > 600):
			spaceship.rect.left = (0)
			
		if (spaceship.rect.left < 0):
			spaceship.rect.right = (600)
			
		if (spaceship.fuel <= 0 and spaceship.landed == True):
			Textshow(-1)
		
		spaceship.control()
		
		spaceship.gravity()
		
		try:
			pygame.display.flip()
		except Exception as err:
			print ("Game Quit")
		
		Window.fill(BLACK)
		
		pygame.draw.lines(Window, WHITE, False, moon.pointlist, 1)
		
		Clock.tick(60)
main()