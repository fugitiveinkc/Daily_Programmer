'''

Title: 233 -- Funny Plant

Goal: You have a plant who's fruit can feed 1 person for a whole week.  Fruits are only viable after 1 week.  As the weeks increase, the fruits produce 1 more fruit than the week before.  You are give a number of people and a number of fruit to start with.  Calculate the number of weeks you'll need to produce enough fruit for everyone.


'''

#--Solution 1 : 11/27/2015--#


#Necessary libraries

from itertools import count
from sys import argv


#Read input from command line (Direct for now)

number_of_people = int(argv[1])
number_of_plants = int(argv[2])


#Initialize number of plants

plants = [count() for i in range(number_of_plants)] #A list of generators


#Produce and plant plants until number of people is satisfied

for week in count(1):
	fruit_totals = 0
	for plant in plants: #Generates appropriate fruit amount
		fruit_totals += plant.next()
	if fruit_totals >= number_of_people: #Checks to see if enough food
		print "Number of weeks it'll take: " + str(week)
		break
	for x in range(fruit_totals): #Adds more plants based on the fruit produced
		plants.append(count(1))
	










