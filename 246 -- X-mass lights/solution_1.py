'''

Title: Challenge 246 -- X-mass lights

Objective: Given a number of hours as input, print out and draw a circuit containing the number of leds you can have.  

Assumptions:
	-Led: 1.7V, 20mA each
	-Battery: 9V, 1200mAh
	-Series of 5 leds work under voltage restriction

Notes:
	-Still need to complete the resistance part

'''

#--Solution 1 -- 12/26/2015--#


#Defined classes

class lights: #Used to create objecs that represent each individual circuit
	"""
	This class can be used to create separate lights objects given a specific number of hours.
	Input: hrs (integer with number of hours)
	Inherent variables: battery_life, led_count
	Methods: draw_circuit
	"""

	def __init__(self, hrs = 1):
		self.battery_life = 1200.0/hrs
		self.led_count = int(self.battery_life/20 * 5)
		self.hours = hrs		

	def draw_circuit(self): #Uses led notation to draw corresponding circuit based on input
		led_series = ''
		for l in range(int(self.led_count)):
			led_series += '--|>|-'
			if (l+1)%5 == 0:
				led_series += '-'
				print led_series
				led_series = ''
		if led_series:
			led_series += '-'
		print led_series


#--TESTING--#

hours = [1,4,6,8,12,20,100] #Test hours
light_objects = []
for hrs in hours: #Create objects with each of the test hours
	light_objects.append(lights(hrs))
for configuration in light_objects: #Print results
	print "For " + str(configuration.hours) + " hour(s): " + str(configuration.led_count) + " leds."
