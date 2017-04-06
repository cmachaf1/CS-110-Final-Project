import threading
import random


#Looping for constant functions, key press detection, and animation will be added later.
class Lander:
	cid = 0
	
	def __init__(self, initAlt, initX, initY):
		self.name = "Lunar Lander"
		self.fuel = 1000
		self.altitude = initAlt
		self.xcoord = initX
		self.ycoord = initY
		self.score = 0
		self.xvelocity = 0
		self.yvelocity = 0
		self.angle = 180
	
	
	def thrust (self, angle):
		#onKeyPress("up arrow")
		#threading.Timer(0.01666666666, thrust)			
		self.fuel += -1
		self.yvelocity += (1 - ((1/90)*abs(self.angle-90)))
		self.xvelocity += (1 - ((1/90)*self.angle))
	
	def turnlander (self, range):
		#onKeyPress("left arrow")
		#threading.Timer(0.033333333333, turnlander)
		self.angle += 1
		if (self.angle >= 180):
			self.angle = 180
		#onKeyPress("right arrow")
		#threading.Timer(0.033333333333, turnlander)
		self.angle += -1
		if (self.angle <= 0):
			self.angle = 0

	def crash (self, fuel):
		#playAnimation(Crash)
		fuelloss = random.randrange(200,400)
		fuel -= fuelloss
		print("Your lander crashed. \n  You lost", str(fuelloss) , "units of fuel.")
		