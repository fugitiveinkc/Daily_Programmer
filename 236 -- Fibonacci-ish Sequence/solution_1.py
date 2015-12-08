'''

Title: Challenge #236 -- Fibonacci-ish Sequence

Objective: Give an integer n, find the lowest integer that the fib(1) can start at to generate a sequence that contains n.

Preliminary Conditions: f(0) = 0, f(1) = 1

Procedure:
	1) Take in integer to search for
	2) Set up look to start at f(1) = 1
	3) If n is found, then return f(1) as solution, otherwise, if the sequence exceeds n, break and go to the next case.
	4) Continue all this until solution is found.

'''

