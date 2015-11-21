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

raw_points = open('points.txt','r+')
number_of_points = 0
points = []
for index, line in enumerate(raw_points):
	if index == 0:
		number_of_points = int(line)
	else:
		line = line.strip('\n')
		x, y = line[1:-1].split(',')
		points.append((float(x), float(y)))		
	

#Method 1: Brute force		

smallest_distance = dist(points[0][0]-points[0][1], points[1][0]-points[1][1])
minimum_two_points = None
for p1 in points:
	for p2 in points:
		if p1 != p2:
			distance = dist(p1[0]-p2[0], p1[1]-p2[1])
			if distance < smallest_distance:
				smallest_distance = distance
				minimum_two_points = [p1, p2]
		else:
			continue

print minimum_two_points
