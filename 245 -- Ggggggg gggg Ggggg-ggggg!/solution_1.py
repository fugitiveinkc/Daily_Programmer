'''

Title: Ggggggg gggg Ggggg-ggggg!

Objective: Give a few letters and a sentenced encoded in Ggggggg, find the original sentence.

Notes: Haven't done the compression part of the challenge but basically complete.

'''
#Necessary libraries

from itertools import count
import sys


#Read input and parse

file_input = open(str(sys.argv[1]))
lines = [line for line in file_input]
dict_line = lines[0].strip('\n').split(' ')
encoded_sentence = [lines[n].strip('\n').split(' ') for n in range(1,len(lines))]
decoder = {}
encoder = {}
for n in count(0, 2): #Can I make these one liners?
	decoder[dict_line[n+1]] = dict_line[n]
	encoder[dict_line[n]] = dict_line[n+1]
	if n == len(dict_line)-2:
		break


#Go through encoded sentence and decrypt (Any way to make this cleaner?)

decoded_sentence = ''
punctuation = ['!','(',')','?','/',',','\"','.','\'']
for sentence in encoded_sentence: #Pick a sentence to work on to decode
	for word in sentence: #Pick a word to work on to decode
		possible_letter, new_word = '', ''
		for character in word: #Go character by character and check with decoding dictionary
			possible_letter += character
			if character in punctuation:
				new_word += character
				possible_letter = ''
			elif possible_letter in decoder:
				new_word += decoder[possible_letter]
				possible_letter = ''
		decoded_sentence += new_word + ' '
	print decoded_sentence
	decoded_sentence = ''

