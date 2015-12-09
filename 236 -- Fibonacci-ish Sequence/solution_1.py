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


#Functions for generating fibonacci sequence (dynamic)

def fib_rec(x, f_1=1):
	if x in fib_cache:
		return fib_cache[x]
	else:
		fib_cache[x] = fib_rec(x-1, f_1) + fib_rec(x-2, f_1)
		return fib_cache[x]


def fib_iter(x, f_1=1):
	if x == 0:
		return fib_cache[0]
	elif x == 1:
		return fib_cache[1]
	elif x-1 in fib_cache and x-2 in fib_cache:
		fib_cache[x] = fib_cache[x-1] + fib_cache[x-2]
		return fib_cache[x]
	for i in range(2,x+1):
		fib_cache[i] = fib_cache[i-1] + fib_cache[i-2]
	return fib_cache[x]


def fib_iter2(x):
	if x == 0:
		return fib_cache[0]
	elif x == 1:
		return fib_cache[1]
	else:
		temp = fib_cache[0] + fib_cache[1]
		fib_cache[0] = fib_cache[1]
		fib_cache[1] = temp
		return temp
		
		
#Testing ground 

n = int(sys.argv[1]) #Integer to search for
for f_1 in count(1): #Test cases for f_1 in natural numbers
	#fib_cache = {0:0, 1:f_1} #Initialize cache for fibonacci sequence generator 
	fib_cache = {0:0, 1:f_1}
	fib_generator = (fib_iter(x) for x in count(0)) #Either rec or iter	
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


'''
#Testing ground II (no functions)

import sys

n = int(sys.argv[1]) #Integer to search for
f_1 = 1
while True: #Test cases for f_1 in natural numbers
	#fib_cache = {0:0, 1:f_1} #Initialize cache for fibonacci sequence generator 
	a, b = 0, f_1
	while b < n:
		found = False
		a, b = b, a + b
	if b==n:
		print f_1
		break
	f_1 += 1
'''
