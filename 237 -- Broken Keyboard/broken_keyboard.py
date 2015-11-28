'''


Title: Problem 237 -- Broken Keyboard

Goal: Given a set of keys that work on a keyboard, you want to emit the longest valid English language word you can make with those letters.

Notes:
	-You can use either enable1.txt on challenge or /usr/share/dict/words


'''

#--Solution 1 -- 11/27/2015--#


#Step 0: Read in broken keyboard settings to test

lines_to_read = int(raw_input())
broken_keyboards = [raw_input() for _ in range(lines_to_read)]


#Step 1: Open valid english words list

words = open('enable1.txt','r')
words = [line.strip('\r\n') for line in words]


#Step 2: Given a configuration for broken keyboard, find biggest word that combination can make

'''
1) Pick a keyboard configuration
2) Test each word in list with keyboard configuration
3) Print out rest and restart
'''

for keyboard in broken_keyboards:
	maximum_length, largest_word = 0, None
	for word in words:
		if len(word) > maximum_length and set(word).issubset(keyboard):
			maximum_length, largest_word = len(word), word
	print ' = '.join([keyboard, largest_word])	
			
		
		

