'''

Title: Challenge 247 -- Secret Santa

Objective: Give a list of names and families, construct a secret santa map without an family members getting each other and no loop backs.

Notes: I think it works?

'''

#Import necessary libraries

from Node import node
import random
random.seed()


#Function to traverse names

def traversal(a_node, current_stack):
	unvisited.remove(a_node)
	current_stack.append(a_node)
	if not unvisited: #Checks to see if unvisited is empty
		if a_node in current_stack[0].family: #If final node connects back to origin and is family, then wrong.
			current_stack.pop()
			unvisited.append(a_node)
			return False
		return True
	elif set(a_node.family).issubset(set(unvisited)) and set(unvisited).issubset(set(a_node.family)): #If unvisited is the same set as the current nodes family.
		return False
	else:
		for member in unvisited:
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
for names in participants:
	for name in names:
		family = names[:]
		family.remove(name)
		graph.append(node(name, family))
	

#Create unvisited list

unvisited = graph


#Traverse and see path:

name = []
traversal(unvisited[0], name)
name.append(name[0])
name = [x.name for x in name]
for x in range(len(name)-1):
	print name[x] + ' -> ' + name[x+1]
