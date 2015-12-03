'''


Title: Challenge #243 [Easy] -- Abundant and Deficient Numbers

Objective:
	-Define a number as deficient if sum of divisors of the number is less than 2 times the number.
	-Define a number as abundant if sum of divisors of the number is more than 2 times the number.


'''

#Import necessary libraries

import sys


#Read input from command line

test_numbers = [int(x) for x in sys.argv[1:]]
print test_numbers


#Find deficient and abundant numbers

for n in test_numbers:
	sum_of_divisors = sum([x for x in range(1,n+1) if n%x == 0])
	if 2*n > sum_of_divisors:
		print str(n) + " deficient by " + str(2*n - sum_of_divisors)
	elif 2*n < sum_of_divisors:
		print str(n) + " abundant by " + str(sum_of_divisors - 2*n)
	else:
		print str(n) + " neither"


