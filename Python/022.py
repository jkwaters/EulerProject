# Project Euler | Problem 22 | Jacob Waters
# What is the total of all the name scores in the file?
# For example, when the list is sorted into alphabetical order, COLIN, 
# which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
# So, COLIN would obtain a score of 938 × 53 = 49714.
# 871198282
# date : 2015.07.22

import re

def nameScore(data):
	names = (re.sub('"', '', open(data).readline()).split(',')).sort()
	for x in xrange(0,len(names)):
		names[x] = sum([(ord(char)-96) for char in names[x].lower()]) * (x+1)
	return sum(names)
	
print nameScore('022-data')