import pygame
import Lander
import #GUI Name Here
import #terrain?

def main():
	
	#Initialization code here
	Lander = Lander.Lander(#Insert (x,y) and altitude here.)
	Clock = pygame.time.Clock()
	
	#Game Loop Code Here
	while True:
		for event in pygame.event.get():
			if event.type: == QUIT
				pygame.quit()
				sys.exit()
				
			if event.type == KEYDOWN
				if event.key == K_RIGHT or K_d
					Lander.turnlander(#INPUT HERE)
				if event.key == K_LEFT or K_a
					Lander.turnlander (#SECOND INPUT)
				if event.key == K_UP or K_w
					Lander.thrust()
					
			if lander.colliderect(terrain):
				if (Lander.xvelocity + Lander.yvelocity < #Small number)
					#Perfect Landing Code here
				elif (Lander.xvelocity + Lander.yvelocity < #Medium number)
					#Good Landing Code here
				elif (Lander.xvelocity + Lander.yvelocity < #Bigger number)
					#Rough Landing Code here
				else:
					crash(Lander.fuel)
				
			lander.gravity()
			clock.tick(60)