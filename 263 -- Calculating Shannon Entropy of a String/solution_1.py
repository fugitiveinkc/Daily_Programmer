'''

Title: Calculating Shannon Entropy of a String

Objective: Given an input string, calculate the shannon entropy of the string

Personal goals: Achieve more one liners and maybe find a way to use numpy?

'''

import math, sys

def shannon_entropy(symbol_count, N):
    frequencies = [symbol_count[symbol]/float(N) for symbol in symbol_count]
    return -1 * sum(freq * math.log(freq, 2) for freq in frequencies)

input_file = open(sys.argv[1])

for line in input_file: #Read lines from input
    line = line.strip('\n')
    symbol_count = dict()
    for char in line: #Create a dictionary with frequencies of each symbol in line
        if char in symbol_count.keys():
            symbol_count[char] += 1
        else:
            symbol_count[char] = 1
    print shannon_entropy(symbol_count, len(line)) #Print shannon entropy
