'''

Given a sequence of numbers, identify all the sequences that when subtracting the absolute difference of all successive numbers, you get all number between 1 to n-1.  Such a sequence is called a jolly jumpber.  Print JOLLY if true, otherwise NOT JOLLY.

Outline:
1) Read in numbers
2) Check two numbers
3) Add number to list
4) Make list into set and see if it is of n-1 length --> If true, you're done!
5) Continue process until very end.

Next goals:
1) Would like to compare the speeds of all three functions with much larger input.
2) Would like to analyze using big O.

'''

#Function for reading in file with test sequence (Not yet done)

#Format [N, sequence]
ts1 = [4,1,4,2,3]
ts2 = [5,1,4,2,-1,6]
ts3 = [4,19,22,24,21]
ts4 = [4,19,22,24,25]
ts5 = [4,2,-1,0,2]

def IsJolly(test_sequence, N): #Trial 1
	'''
	
	Takes in a test sequence and the sequence size.  
	Calculates if the difference between each successive number makes all
	the integers between 1 and the sequence size-1.

	Returns JOLLY if true
	Otherwise NOT JOLLY
	
	'''
	storage = []
	for i in range(0, N-1):
		successive_sum = abs(test_sequence[i] - test_sequence[i+1])
		if successive_sum >= 1 or successive_sum <= (N-1):
			storage.append(successive_sum)
		if len(set(storage)) == (N-1):
			return "JOLLY"
	return "NOT JOLLY"


def IsJolly_using_lists(test_sequence, N):
	'''

	Takes in a test sequence and the sequence size.
	Calculates if the difference between each successive number makes all
	the integers between 1 and the sequence size-1.

	Returns JOLLY if true
	Otherwise NOT JOLLY

 	This function was written to compare the speed of a similar function
	implemented with sets (see IsJolly_using_sets)
	
	'''
	reference_list = range(1,N)
	for i in range(N-1):
		current_value = abs(test_sequence[i] - test_sequence[i+1]) 
		try:
			reference_list.remove(current_value)
		except ValueError:
			pass
		if not reference_list:
			return "JOLLY"
	return "NOT JOLLY"
	

def IsJolly_using_sets(test_sequence, N):
	'''

	Takes in a test sequence and the sequence size.
	Calculates if the difference between each successive number makes all
	the integers between 1 and the sequence size-1.

	Returns JOLLY if true
	Otherwise NOT JOLLY

 	This function was written to compare the speed of a similar function
	implemented with lists (see IsJolly_using_lists)
	
	'''
	reference_list = set(range(1,N))
	for i in range(N-1):
		current_value = abs(test_sequence[i] - test_sequence[i+1]) 
		try:
			reference_list.discard(current_value)
		except ValueError:
			pass
		if not reference_list:
			return "JOLLY"
	return "NOT JOLLY"


if __name__ == "__main__": #Test cases
	print IsJolly_using_sets(ts1[1:], ts1[0])
	print IsJolly_using_sets(ts2[1:], ts2[0])
	print IsJolly_using_sets(ts3[1:], ts3[0])
	print IsJolly_using_sets(ts4[1:], ts4[0])
	print IsJolly_using_sets(ts5[1:], ts5[0])

