'''

Title: Challenge 247 -- Secret Santa

Objective: Give a list of names and families, construct a secret santa map without an family members getting each other and no loop backs.

'''


#Import necessary libraries

from Node import node
import random
random.seed()


#Function to traverse names

def traversal(a_node): #Error: Has the potential to link families and never end
	unvisited.remove(a_node)
	print a_node.name
	if not unvisited:
		return a_node.name
	else:
		#1) select name from unvisited
		#2) If name is in family, reselect
		#3) Otherwise, traverse with the new name
		while True:
			new_node = unvisited[random.randint(0,len(unvisited)-1)]
			if new_node.name not in a_node.family:
				break
		return a_node.name + ' ' + traversal(new_node)	


#Read in names

participants = open('names.txt')
participants = [names.strip('\n').split(' ') for names in participants]
graph = []
for names in participants:
	for name in names:
		family = names[:]
		family.remove(name)
		graph.append(node(name, family))
	

#Create unvisited list

unvisited = graph


#Traverse and see path:

path = traversal(unvisited[0]) #What if you started with a person with no family?
path = path.split(' ')
for index, name in enumerate(path):
	if index == len(path)-1:
		print name + ' -> ' + path[0]
	else:
		print name + ' -> ' + path[index+1] 
