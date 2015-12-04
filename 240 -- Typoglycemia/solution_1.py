'''


Title: Challenge #240 [Easy] Typoglycemia

Objective: Given a paragraph, scramble the innards of everyword.

Note: Maybe use regex to eliminate edge cases?

'''

#--Solution 1 -- 12/3/2015--#


#Useful libraries

import sys, random


#Read in paragraph and separate out

paragraph = open(sys.argv[1], 'r')
paragraph = [line.strip('\n').split(' ') for line in paragraph]
print paragraph


#Scramble

ending_punctuation = [',','.','!','?',':',';']
for line in paragraph:
	for index_in_line, word in enumerate(line):
		if len(word) <= 3: #No need to scramble words that are only three letters
			continue
		elif '\'' in word: #Handles cases like "doesn't"
			sample = random.sample(word[1:word.index('\'')-1], word.index('\'')-2)
			print sample
			word = word[0] + ''.join(sample) + word[word.index('\'')-1:]
			line[index_in_line] = word
		elif word[-1] in ending_punctuation and len(word) > 4: #Handles cases with ending punctuation
			sample = random.sample(word[1:len(word)-2], len(word)-3)
			word = word[0] + ''.join(sample) + word[len(word)-2:len(word)]
			line[index_in_line] = word
		else: #Handles normally if no punctuation and length is bigger than 3
			sample = random.sample(word[1:len(word)-1], len(word)-2)
			word = word[0] + ''.join(sample) + word[-1]
			line[index_in_line] = word


#Reassemble

for line in paragraph:
	line_reassembled = ' '.join(line)
	print line_reassembled


