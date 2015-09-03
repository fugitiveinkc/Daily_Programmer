'''

Objective: Parse a JSON file and find the string "dailyprogrammer"

JSON_types: null, number, boolean, string, list, object

Summary: Program works, but isn't very elegant


'''

#Import JSON parsing library

import json

#A function that finds "dailyprogrammer"

def JSON_search(item, path=[]):

	if type(item) == dict: #Call when item is a dictionary
		for key in item.keys():
			path.append(key)
			if item[key] == "dailyprogrammer":
				return path
			else:
				path = JSON_search(item[key], path)
			if len(path) > 0:
				if path[-1] == "dailyprogrammer":
					return path
		path.pop() #Insures that if you've gone through the whole dictionary and no item are "dailyprogrammer", then remove the dict title itself from the path
		return path

	elif type(item) == list: #Call when item is a list
		for element in item:
			if element == "dailyprogrammer":
				path.append(item.index(element))
				path.append(element)
				return path
			elif type(element) == dict or type(element) == list:
				path.append(item.index(element))
				path = JSON_search(element, path)
			if path[-1] == "dailyprogrammer":
					return path
		path.pop() #Insures that if you've gone through the whole list and no items are "dailyprogrammer", then remove the list title itself from the path.
		return path			

	else: #If item is not list or dictionary, we can directly check here if it is "dailyprogrammer"
		if path[-1] == "dailyprogrammer":
			return path
		else:
			path.pop()
			return path
#Read in JSON file

json_file = open('challenge2.txt')
json_file = json_file.read()
json_parsed = json.loads(json_file)

#Find pathway to "dailyprogrammer" in parsed JSON file

path = JSON_search(json_parsed)[:-1]

#Print path in arrow notation

full_path = ""
for index in range(len(path)):
	if index != len(path)-1:
		full_path += str(path[index]) + " -> "
	else:
		full_path += str(path[index])
print full_path
