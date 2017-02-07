'''

Title: Rack management I
Objective: Given a series of 7 tiles and a word of choice, evaluate whether one can make the word of choice with the tiles.

Optional Bonus 1/2/3: Only completed option 1

Notes: Current method is inefficient, but works

'''

def scrabble(tiles, word):
	'''
	Takes each letters in the word and checks if there is a sufficient
	number of characters among the tiles.
	'''
	tiles = list(tiles)
	checked_letters = [] #Used to not check letters already verified in the word
	for letter in word:
		#Loop through word, see if enough letters or wildcards can make up for the number of letters in the word, then remove wildcards accordingly
		if checked_letters.count(letter) == 0: #Only executes if letter hasn't already been checked
			checked_letters.append(letter)
			if tiles.count(letter) >= word.count(letter):
				continue
			elif (tiles.count(letter) + tiles.count('?')) >= word.count(letter):
				[tiles.remove('?') for x in range(word.count(letter)-tiles.count(letter))]
			else:
				return "False"
	return "True"


print "First four test cases in the reddit description"
print scrabble("ladilmy", "daily") #true
print scrabble("eerriin", "eerie") #false
print scrabble("orrpgma", "program") #true
print scrabble("orrppma", "program") #false


print "First four test cases in optional bonus 1"
print scrabble("pizza??", "pizzazz") #true
print scrabble("piizza?", "pizzazz") #false
print scrabble("a??????", "program") #true
print scrabble("b??????", "program") #false
