'''

Title: Verifying 3x3 magic squares

Objective: Given an input array that represents a 3x3 magic square, verify

Bonus: Do NxN magic squares and incomplete magic squares (Still need to do incomplete squares)

Assumption: All numbers are used from 1 to n^2, so no need to check that

Notes: Can numpy simplify this?  Also, how can recursion be used?

'''

def square_verifier(square, N):
    final_sum = (N*(N**2+1))/2
    for x in range(0, N**2, N): #Check rows
        row_sum = 0
        for i in range(N):
            row_sum += square[x + i]
        if row_sum != final_sum:
            return False
    for y in range(N): #Checks columns
        col_sum = 0
        for i in range(0, N**2, N): 
            col_sum += square[y + i]
        if col_sum != final_sum:
            return False
    return True
            

input_file = open('bonus_input.txt')
N = input('What is your dimension size? ')
magic_squares = tuple(eval(x.strip('\n')) for x in input_file)

verified_squares = []
for square in magic_squares:
    verified_squares.append(square_verifier(square, N))

for (square, verification) in zip(magic_squares, verified_squares):
    print str(square) + ' => ' + str(verification)
