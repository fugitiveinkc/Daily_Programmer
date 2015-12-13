'''

Title: Chalenege #243 Jenny's Fruit Basket

Objective: Given input of fruit and price, find the possible combinations with repitition in Jenny's fruit basket that equals exactly $5.

Notes:
	-Learn to program product function on your own using recursion
	-Speed up program

'''

#Import necessary libraries

from math import ceil
from itertools import product


#Read in file with prices and set max

file = open('fruits.txt')
file_lines = [line.strip('\n').split(' ') for line in file]
prices = [float(line[1]) for line in file_lines]
print prices
max_price = int(raw_input('What is the maximum price? : '))
bounds = [int(ceil(max_price/price)) for price in prices]
print bounds

							
#Loop through every solution and see if it works (Problem: How to do this with n unknowns)	

basket_cache = {}
for soln in product(*tuple(range(bound) for bound in bounds)):
	if soln in basket_cache:
		if basket_cache[soln] == 500:
			print soln
		break
	elif sum(p*s for p,s in zip(prices, soln)) == 500:
		basket_cache[soln] = 500
		print soln	
	basket_cache[soln] = sum(p*s for p,s in zip(prices, soln))

