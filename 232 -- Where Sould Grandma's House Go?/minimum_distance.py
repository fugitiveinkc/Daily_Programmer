'''

Title: Where Should Grandma's House Go?

Objective: Given a set of N cartesian coordinates, find the two points with the least distance between them.

Current thoughts:
	-Avoid saving the distances into memory.
	-Perhaps it's easier just to save the current distance and change it based on if another distance exceeds it.

'''
#Appropriate libraries

from math import sqrt
from math import hypot as dist 


#Read file of points in

def read_input(filename = 'points.txt'):
	raw_points = open(filename, 'r+')
	points = [eval(line) for line in raw_points]
	return points[1:]


#Method 1: Brute force		

def brute_force(points):
	smallest_distance = float("inf")
	minimum_two_points = None
	for index, p1 in enumerate(points):
		for p2 in points[index+1:]:
			if p1 != p2:
				distance = dist(p1[0]-p2[0], p1[1]-p2[1])
				if distance <= smallest_distance:
					smallest_distance = distance
					minimum_two_points = [p1, p2]
	return minimum_two_points


#Method 2: Recursion
#--Divide and conquer?



#--TESTING GROUND--#

if __name__ == "__main__":
	print brute_force(read_input())
