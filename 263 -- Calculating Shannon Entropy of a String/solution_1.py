'''

Title: Calculating Shannon Entropy of a String

Objective: Given an input string, calculate the shannon entropy of the string

Personal goals: Achieve more one liners and maybe find a way to use numpy?

'''

import math, sys

def shannon_entropy(symbol_count, N):
    current_sum = 0
    for symbol in symbol_count: #Loop is basically a sum
            frequency = symbol_count[symbol]/float(N)
            current_sum += frequency * math.log(frequency, 2)
    return -1*current_sum

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
