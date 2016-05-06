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

for line in input_file:
    symbol_count = {char:0 for char in line.strip('\n')}
    for char in line.strip('\n'):
        symbol_count[char] += 1
    print shannon_entropy(symbol_count, len(line.strip('\n'))) #Print shannon entropy

