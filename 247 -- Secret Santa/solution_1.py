'''

Title: Challenge 247 -- Secret Santa

Objective: Give a list of names and families, construct a secret santa map without an family members getting each other and no loop backs.

Notes: Unvisited list is the tricky part here.

'''

#Import necessary libraries

from Node import node
import random
random.seed()


#Function to traverse names

def traversal(a_node, current_stack):
	unvisited.remove(a_node)
	current_stack.append(a_node)
	for name in current_stack:
		names.append(name.name)
	if not unvisited: #Checks to see if unvisited is empty
		if a_node in current_stack[0].family: #If final node connects back to origin and is family, then wrong.
			current_stack.pop()
			unvisited.append(a_node)
			return False
		return True
	elif set(a_node.family).issubset(set(unvisited)) and set(unvisited).issubset(set(a_node.family)): #If unvisited is the same set as the current nodes family.
		return False
	else: #A current node, loops through unvisited node
		copy_unvisited = unvisited[:] #Crucial: As unvisited is changing, you don't want each node to have a new unvisited list to check
		for member in copy_unvisited:
			if member.name not in a_node.family:
				if traversal(member, current_stack):
					return True
		current_stack.pop()
		unvisited.append(a_node)
		return False			


#Read in names

participants = open('names2.txt')
participants = [names.strip('\n').split(' ') for names in participants]
graph = []
for names in participants: #Creates nodes with name and family members
	for name in names:
		family = names[:]
		family.remove(name)
		graph.append(node(name, family))
	

#Create unvisited list

unvisited = graph


#Traverse and see path:

name = []
traversal(unvisited[random.randint(0,len(unvisited)-1)], name) #Selects random participant to start with to organize
name.append(name[0])
name = [x.name for x in name]
for x in range(len(name)-1):
	print name[x] + ' -> ' + name[x+1]
