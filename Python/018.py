# Project Euler | Problem 18 | Jacob Waters
# By starting at the top of the triangle below and moving to adjacent numbers on the row below
# find the maximum total from top to bottom of the triangle.
# 1074
# date : 2015.07.20

def maxPathSum(data):
	triangle = [[int(num) for num in line.split(' ')] for line in open(data)]
	for x in xrange(len(triangle)-2,-1,-1):
		for y in xrange(0,len(triangle[x])):
			triangle[x][y] += max(triangle[x+1][y], triangle[x+1][y+1])
	return triangle[0][0]

print maxPathSum('067-data')