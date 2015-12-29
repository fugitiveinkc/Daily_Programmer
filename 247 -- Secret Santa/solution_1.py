'''

Title: Challenge 247 -- Secret Santa

Objective: Give a list of names and families, construct a secret santa map without an family members getting each other and no loop backs.

'''

#Import necessary libraries

import random
random.seed()

#Function to traverse names

	
#Read in names

participants = open('names.txt')
participants = [tuple(names.strip('\n').split(' ')) for names in participants]


#Create unvisited list

unvisited = [name for names in participants for name in names]


