'''

Title: Rack management I
Objective: Given a series of 7 tiles and a word of choice, evaluate whether one can make the word of choice with the tiles.

Optional Bonus 1/2/3: Not complete

Notes: Current method is inefficient, but works

'''

def scrabble(tiles, word):
	'''
	Takes each letters in the word and checks if there is a sufficient
	number of characters among the tiles.
	'''
	for letter in word:
		if tiles.count(letter) >= word.count(letter):
			continue
		else:
			return "False"
	return "True"

'''
Test cases in the reddit examples
scrabble("ladilmy", "daily") -> true
scrabble("eerriin", "eerie") -> false
scrabble("orrpgma", "program") -> true
scrabble("orppgma", "program") -> false
scrabble("ladilmy", "daily")
'''

print "First four test cases in the reddit description"
print scrabble("ladilmy", "daily")
print scrabble("eerriin", "eerie") 
print scrabble("orrpgma", "program")
print scrabble("orrppma", "program") 
