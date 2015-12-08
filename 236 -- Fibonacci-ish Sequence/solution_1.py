'''

Title: Challenge #236 -- Fibonacci-ish Sequence

Objective: Give an integer n, find the lowest integer that the fib(1) can start at to generate a sequence that contains n.

Preliminary Conditions: f(0) = 0, f(1) = 1

Procedure:
	1) Take in integer to search for
	2) Set up look to start at f(1) = 1
	3) If n is found, then return f(1) as solution, otherwise, if the sequence exceeds n, break and go to the next case.
	4) Continue all this until solution is found.

Note:
	-Does not work for last challenge case: 123456789

'''


#Import necessary libraries

import sys
from itertools import count


#Function for generating fibonacci sequence (dynammic)

def fib(x, f_1=1):
	if x in fib_cache:
		return fib_cache[x]
	else:
		fib_cache[x] = fib(x-1, f_1) + fib(x-2, f_1)
		return fib_cache[x]


#Testing ground

n = int(sys.argv[1]) #Integer to search for
for f_1 in count(1): #Test cases for f_1 in natural numbers
	fib_cache = {0:0, 1:f_1} #Initialize cache for fibonacci sequence generator
	fib_generator = (fib(x, f_1) for x in count(0))	
	for f in fib_generator:
		found = False
		if n == f:
			found = True
			break
		elif f > n:
			break
	if found:
		print f_1
		break
	
