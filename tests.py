import lab10
import random

def main():
	
	print("######Testing lunar lander model######")
	test_lunar_lander = lab10.Lander(40, 0, 0)

	print("######Standard Input Test######")
	test_lunar_lander.thrust(random.randrange(1,90))
   
	print("######Zero Input Test######")
	test_lunar_lander.thrust(0)

	print("######Out Of Bounds Test######")
	test_lunar_lander.thrust(200)

	print("######Negative Input Test######")
	test_lunar_lander.thrust(-25)
	
	print("######Standard Input Test######")
	test_lunar_lander.turnlander(random.randrange(0,360))
    
	print("######Zero Input Test######")
	test_lunar_lander.turnlander(0)

	print("######Out Of Bounds Test######")
	test_lunar_lander.turnlander(400)
	
	print("######Negative Input Test######")
	test_lunar_lander.turnlander(-45)

	print("######Standard Input Test######")
	test_lunar_lander.crash(random.randrange(0,1000))
	
	print("######Zero Input Test######")
	test_lunar_lander.crash(0)

	print("######Out Of Bounds Test######")
	test_lunar_lander.crash(2000)
	
	print("######Negative Input Test######")
	test_lunar_lander.crash(-500)

main()