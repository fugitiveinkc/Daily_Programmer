'''

Title: Challenge 245 [Easy] Date Dilemma

Objective: Go through a file of dates with assorted ways of formatting and reformat so that it says each date as YYYY-MM-DD

'''

#Regular expressions library

import re


#Functions used

def reformat(date):
	delimiter = re.search('\W', date)
	split_date = date.split(delimiter.group())
	if re.match('\d\d\d\d', date): #Format is Y M D
		if len(split_date[1]) != 2: #Checks month format
			split_date[1] = '0' + split_date[1]
		if len(split_date[2]) != 2: #Checks day format
			split_date[2] = '0' + split+date[2]
		return '-'.join(split_date)
	else: #Format is M D Y
		if len(split_date[0]) != 2: #Checks month format
			split_date[0] = '0' + split_date[0]
		if len(split_date[1]) != 2: #Checks day format
			split_date[1] = '0' + split_date[1]
		if len(split_date[2]) != 4: #Checks year format
			split_date[2] = '20' + split_date[2]
		return '-'.join([split_date[2], split_date[0], split_date[1]])	#Rearranges to correct format


#First, read in file with dates and open output file to edit

dates = open('input.txt')
new_dates = open('output.txt', 'w')
dates = [line.strip('\n') for line in dates]


#Second, go through dates, detect format and reformat

for date in dates:
	new_date = reformat(date)
	print new_date
	new_dates.write(new_date + '\n')

dates.close()
new_dates.close()
