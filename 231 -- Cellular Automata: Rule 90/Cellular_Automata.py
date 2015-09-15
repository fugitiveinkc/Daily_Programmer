'''

Title: Cellular Automata: Rule 90

Objective: Using Rule 90 (XOR left and right neighbors) in one dimension, print out next 25 steps.

Process:
	1) Read input
	2) Create row based on input
	3) Calculate new row input
	4) LOOP

Possible use of classes: Cellular automata type (rules imbedded)
	-Reason to use class: Useful to have a type in case I want to do other rules to it.

''' 

#Classes used

class cellular_automata:
	
	'''

	The cellular automata type has two input.  An initial list containing initial states (string of bits spaced with whitespace) and a step size number to indicate how many iterations to do.  Has a plot function and a rule90 function.  May be extended to have more rules

	'''

	def __init__(self, initial_input, step_size):
		self.initial_input = initial_input.split()
		self.step_size = step_size
		self.automation_data = []

	def rule90(self):
		input_row = self.initial_input
		for step in range(self.step_size):
			input_row.insert(0,"0") #Initial hidden bit
			input_row.append("0") #Ending hidden bit
			self.automation_data.append(input_row)
			new_row = []
			for index, bit in list(enumerate(input_row[1:len(input_row)-1])):
				new_bit = int(input_row[index]) ^ int(input_row[index+2])
				new_row.append(str(new_bit))
			input_row = new_row
				 
	def plot(self):
		for a in self.automation_data:
			row_string = ""
			for b in a:
				if b == "0":
					row_string += " "
				else:
					row_string += "x"
			print row_string
				
#Test cases

print "----------"
print "Test Case 1"
print "-----------"
test_1 = cellular_automata("1 1 0 1 0 1 0", 6)
test_1.rule90()
test_1.plot()

print "--------------------"
print "Serpinski's Triangle"
print "--------------------"
test_2 = cellular_automata("0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0", 26)
test_2.rule90()
test_2.plot()
	
	


