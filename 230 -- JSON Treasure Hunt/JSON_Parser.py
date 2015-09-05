'''

Objective: Parse a JSON file and find the string "dailyprogrammer"

JSON_types: null, number, boolean, string, list, object

Summary: Program works, but isn't very elegant


'''

#Import JSON parsing library

import json

#A function that finds "dailyprogrammer"

def JSON_search(item, path=[]):
	if type(item) == dict:
		for key in item.keys():
			if JSON_search(item[key], path):
				path.append(key)
				return True
	elif type(item) == list:
		for (i, element) in list(enumerate(item)):
			if JSON_search(element, path):
				path.append(str(i))
				return True
	else:
		if item == "dailyprogrammer":
			return True


#Find pathway to "dailyprogrammer" in parsed JSON file


path = []
JSON_search(json.loads(open('challenge2.txt').read()), path)
path = path[::-1]


#Print path in arrow notation

print " -> ".join(path)
