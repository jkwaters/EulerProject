# Project Euler | Problem 21 | Jacob Waters
# Evaluate the sum of all the amicable numbers under 10000
# 31626
# date : 2015.07.22

def amicableNumbersSum(n):
	sumList = []
	
	for x in xrange(2,n):
		factorX = sumOfFactors(x)
		if(x == sumOfFactors(factorX) and x != factorX):
			if (x not in sumList):
				sumList.append(x)
				sumList.append(factorX)
	
	return sum(sumList)

def sumOfFactors(n):
	sum = 1
	sqrtN = int(n**0.5)

	if (n == 1):
		return 1

	if(n == (sqrtN*sqrtN)):
		sum += sqrtN
		sqrtN -= 1

	for x in xrange(2,sqrtN+1):
		if (n % x == 0):
			sum += x + (n/x)

	return sum

print amicableNumbersSum(10000)
